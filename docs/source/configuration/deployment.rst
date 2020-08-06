Deployment
==========

The PGB website supports database configurations for three scenarios:

1. Running locally against a local database
2. Running locally against the deployment database in the cloud
3. Full deployment to the cloud

This page provides instructions for all three scenarios.

GCP Dependencies
----------------

The broker website is built to run in the cloud using App Engine.
If you intend to run the website against a local development database,
this step can be skipped. If you intend to run the website
using GCP resources you will need to install the ``gcloud`` command line
tool which is available `here`_. You will also need to install the Google
Cloud SQL Proxy so the website can connect to the necessary SQL backends
when running locally.

For Mac OS 64 bit, use:

.. code-block:: bash

   curl -o cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.darwin.amd64
   chmod +x cloud_sql_proxy

For Linux 64 bit, use:

.. code-block:: bash

   wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
   chmod +x cloud_sql_proxy


For other installations see the appropriate section of the
official `App Engine docs`_.

.. _App Engine docs: https://cloud.google.com/python/django/appengine](https://cloud.google.com/python/django/appengine

Running Against The Cloud
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

.. important:: The following section is provided for reference only. All
   updates to the official website should be performed via
   continuous deployment.

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
