GCP Configuration
=================

Full documentation on configuring Django applications for App Engine is
available in the official `App Engine docs`_. Notes are provided here for those
configuring an environment from scratch. These steps only need to be performed
once. If you are developing against the official Pitt-Google Broker GCP
project then these these steps should have already been taken.

Static File Storage
-------------------

You will need to configure a GCP Storage Bucket for publicly hosting
static files (images, CSS, etc.). This can be from the
`console webpage <https://console.cloud.google.com/storage/>`_
or from the command line as shown below. :

1. Create a bucket for hosting static files. Default values for the storage class
   and bucket location should be sufficient, but can be specified if desired.

.. code-block:: bash

   gsutil mb -p [PROJECT_NAME] -c [STORAGE_CLASS] -l [BUCKET_LOCATION] -b on gs://[BUCKET_NAME]/


2. Make sure the bucket is publicly readable.

.. code-block:: bash

   gsutil defacl set public-read gs://broker-web-static

Cloud SQL
---------

The website will pull data from the broker pipeline to populate page content
as necessary. However, a dedicated Cloud SQL database is also used to store
website and user data. You can use the console
`SQL interface <https://console.cloud.google.com/sql/>`_
to create this database, or accomplish it from the command line:

1. Start by making sure the Cloud SQL Admin API is enables.

.. code-block:: bash

   gcloud services enable sqladmin


2. Create a Cloud SQL instance.

.. code-block:: bash

   gcloud sql instances create [INSTANCE_NAME] --tier=[MACHINE_TYPE] --region=[REGION]


3. Create a database on the Cloud SQL instance.

.. code-block:: bash

   gcloud sql databases create [DATABASE_NAME] --instance=[INSTANCE_NAME]


4. Create a new user account that your application will user to access the database.

.. code-block:: bash

   gcloud sql users create [USER_NAME] --instance=[INSTANCE_NAME] --password=[PASSWORD]


The Django Application
----------------------

Once Cloud SQL is configured, you will need to create the necessary database
tables. The management script packaged with the website's source code
automates this process.
You will need to connect to the Cloud SQL database and migrate
database models from the Django application into the database.

1. Use the Cloud SDK to fetch the connection name of your instance.
   The connection name will be listed in the format
   ``[PROJECT_NAME]:[REGION_NAME]:[INSTANCE_NAME]``.

.. code-block:: bash

   gcloud sql instances describe [INSTANCE_NAME]

2. Make sure the database settings in the Django application
   (``broker_web/main/settings.py``) point to the new database you just
   created. In general, the settings should look like the following:

.. code-block:: bash

   # broker_web/settings.py

   if os.getenv('GAE_APPLICATION', None):
       # Running on production App Engine, so connect to Google Cloud SQL using
       # the unix socket at /cloudsql/<your-cloudsql-connection string>
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.mysql',  # Assuming you are using MySQL
               'HOST': '/cloudsql/[CONNECTION_NAME]',
               'NAME': '[DATABASE_NAME]',
               # You'll probably want to set the auth data in your environment
               'USER': '[DATABASE_USER]',
               'PASSWORD': '[DATABASE_PASSWORD]',
           }
       }

   else:
       # Running locally so connect to Cloud SQL via the proxy.
       # To start the proxy see https://cloud.google.com/sql/docs/mysql-connect-proxy
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.mysql',
               'HOST': '127.0.0.1',
               'PORT': '3306',
               'NAME': '[DATABASE_NAME]',
               # Here is an example using django-environ
               'USER': env.str('DB_USER'),
               'PASSWORD': env.str('DB_PASSWORD'),
           }
       }
   ```

3. Launch a SQL proxy so a a Django application running from your local machine
   can connect to the GCP SQL database. Instructions on downloading the
   ``cloud_sql_proxy`` application are available
   `here <https://cloud.google.com/sql/docs/mysql/sql-proxy>`_.


.. code-block:: bash

   ./cloud_sql_proxy -instances "[REGION_NAME]"=tcp:3306


4. Make the necessary database migrations and set up an admin account.

.. code-block:: bash

   python manage.py migrate --run-syncdb
   python manage.py createsuperuser

5. As a final step you will need to configure the `Recaptcha`_ service which
   is used to protect against bots. Make sure to add the appropriate public
   recaptcha key to ``broker_web/templates/recaptcha.html``

.. _App Engine docs: https://cloud.google.com/python/django/appengine](https://cloud.google.com/python/django/appengine
.. _Recaptcha: https://www.google.com/recaptcha/
