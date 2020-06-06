Deployment
==========

The PGB website supports database configurations for three scenarios:

1. Running locally against a local database
2. Running locally against the deployment database in the cloud
3. Full deployment to the cloud

This page provides instructions for all three scenarios.

Running Locally
---------------

1. Configure environmental variables as defined in the previous section.

2. If not already available, create the ``web_backend`` database in MySQL. The
   ``python manage.py migrate`` command ensures that your local database
   follows the same schema as the database used in production.

.. code-block:: bash

   mysql.server start
   mysql -u root -e 'create database web_backend;'
   python broker_web/manage.py migrate

3. Next, launch the web application via the management script:

.. code-block:: bash

   python broker_web/manage.py runserver  # Run the web server


Running against the cloud
-------------------------

1. Configure environmental variables as defined in the previous section.

2. Start by launching the SQL proxy so the application can connect to the cloud.

.. code-block:: bash

   ./cloud_sql_proxy -instances "ardent-cycling-243415:us-east1:broker-web"=tcp:3306

3. Next, launch the web application via the management script:

.. code-block:: bash

   python broker_web/manage.py runserver  # Run the web server


Deploying to App Engine
-----------------------

Application versions can be deployed manually using the ``gcloud`` API:

.. code-block:: bash

   # Synchronize static files in the storage bucket
   gsutil -m rsync -r broker_web/static gs://[BUCKET_LOCATION]/static

   # Deploy the new source code
   gcloud app deploy


Deployment settings can be configured using the a ``app.yaml`` file. The
official ``app.yaml`` docs can be found `here`_. At a minimum, your settings
for deployment should include the following:

.. code-block:: yaml

   runtime: python37

   entrypoint: gunicorn -b :$PORT broker_web.main.wsgi

   env_variables:
     SECRET_KEY: '[YOUR-SECRET-KEY]'
     STATIC_URL: 'https://storage.googleapis.com/[BUCKET-NAME]/static/'
     DB_USER: [SQL-DB-USERNAME]
     DB_PASSWORD: [SQL-DB-PASSWORD]
     ALLOWED_HOSTS: [OFFICIAL-PGB-WEBSITE-DOMAIN]

   handlers:
     - url: /static
       static_dir: static


.. _here: https://cloud.google.com/appengine/docs/standard/python/config/appref
