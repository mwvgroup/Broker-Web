Deploying a New Version to Production
=====================================

Application versions can be deployed manually using the ``gcloud`` API:

.. code-block::

   # Synchronize static files in the storage bucket
   gsutil -m rsync -r broker_web/static gs://[BUCKET_LOCATION]/static

   # Deploy the new source code
   gcloud app deploy


Deployment settings can be configured using the a ``app.yaml`` file. The
official ``app.yaml`` docs can be found `here`_. At a minimum, your settings
for deployment should include the following:

.. code-block::

   runtime: python37

   entrypoint: gunicorn -b :$PORT broker_web.main.wsgi

   env_variables:
     SECRET_KEY: '[YOUT-SECRET-KEY]'
     STATIC_URL: 'https://storage.googleapis.com/[BUCKET-NAME]/static/'
     DB_USER: [SQL-DB-USERNAME]
     DB_PASSWORD: [SQL-DB-PASSWORD]
     ALLOWED_HOSTS: [OFFICIAL-PGB-WEBSITE-DOMAIN],

   handlers:
     - url: /static
       static_dir: static


.. _here: https://cloud.google.com/appengine/docs/standard/python/config/appref