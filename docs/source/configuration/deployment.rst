Deployment
==========

The PGB website supports database configurations for three scenarios:

1. Running locally against a local database
2. Running locally against the deployment database in the cloud
3. Full deployment to the cloud

This page provides instructions for all three scenarios.

Environmental Variables
-----------------------

The following table outlines environmental variables that can be used to
configure standard Django settings. Note that at least one of the ``DEBUG`` or
``ALLOWED_HOSTS`` variables must be set for the app to run.

+-----------------------+------------------------------------------+---------------------------------+
| Variable              | Description                              | Required                        |
+=======================+==========================================+=================================+
| ``SECRET_KEY``        | Django secret key                        | Yes                             |
+-----------------------+------------------------------------------+---------------------------------+
| ``DEBUG``             | Whether to run in debugging mode         | Must be ``True`` if             |
|                       |                                          | ``ALLOWED_HOSTS`` is not set    |
+-----------------------+------------------------------------------+---------------------------------+
| ``ALLOWED_HOSTS``     | Block requests except from these domains | If ``Debug`` is not ``true``    |
+-----------------------+------------------------------------------+---------------------------------+
| ``CONTACT_EMAILS``    | List of developer contact emails         | no                              |
+-----------------------+------------------------------------------+---------------------------------+

If you are running against the official project database, you will also need
to specify the database username and password.

+-----------------------+------------------------------------------+---------------------------------+
| Variable              | Description                              | Required                        |
+=======================+==========================================+=================================+
| ``DB_USER``           | SQL backend username                     | For GCP only                    |
+-----------------------+------------------------------------------+---------------------------------+
| ``DB_PASSWORD``       | SQL backend password                     | For GCP only                    |
+-----------------------+------------------------------------------+---------------------------------+

For convenience, environmental variables can be specified in a ``.env`` file
placed into the project's root directory. However, the application will
specifically ignore ``.env`` files when running on the deployment server.

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
     ALLOWED_HOSTS: [OFFICIAL-PGB-WEBSITE-DOMAIN],

   handlers:
     - url: /static
       static_dir: static


.. _here: https://cloud.google.com/appengine/docs/standard/python/config/appref
