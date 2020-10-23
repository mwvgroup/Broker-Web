Deploying to App Engine
=======================

The production version of the website is hosted in the cloud using
`GCP App Engine <https://console.cloud.google.com/appengine>`_.
This page outlines instructions for deploying new versions of the website
source code to the cloud.

Updating Static Files
---------------------

Static files are updated in the cloud separately from changes to the source
code. Static files can be synced against a locally checked out version
of the project source code by running:

.. code-block:: bash

   # Synchronize static files in the storage bucket
   gsutil -m rsync -r broker_web/static gs://[BUCKET_LOCATION]/static

Manual Deployment
-----------------

.. important:: The following section is provided for reference only. All
   updates to the official website should be performed via
   continuous deployment as outlined later in this document.

Application versions can be deployed manually using the ``gcloud`` API:

.. code-block:: bash

   # Deploy the new source code
   gcloud app deploy

Deployment settings should be configured using the a ``app.yaml`` file. The
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


Continuous Deployment
---------------------

