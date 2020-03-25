Deployment
==========

These instructions will allow you to deploy a version of the PGB website.

.. important:: Unless manually configured otherwise, deployments run against
   the project's official SQL backend in GCP. This includes locally running
   server instances. Use admin capabilities with care.

Environmental Variables
-----------------------

The following table outlines environmental variables that can be used to
configure standard Django settings. Note that at least one of ``DEBUG`` or
``ALLOWED_HOSTS`` must be set for the app to run. For convenience, these can
be specified in a ``.env`` file placed into the project's root directory.
However, the application will specifically ignore ``.env`` files when running
on the deployment server.

+-----------------------+---------------------------------------------+---------------------------------+
| Variable              | Description                                 | Required                        |
+=======================+=============================================+=================================+
| ``SECRET_KEY``        | Django secret key                           | Yes                             |
+-----------------------+---------------------------------------------+---------------------------------+
| ``DEBUG``             | Whether to run in debugging mode            | If ``ALLOWED_HOSTS`` is not set |
+-----------------------+---------------------------------------------+---------------------------------+
| ``ALLOWED_HOSTS``     | Block requests except from these domains    | If ``Debug`` is not ``true``    |
+-----------------------+---------------------------------------------+---------------------------------+
| ``DB_USER``           | SQL backend username                        | Yes                             |
+-----------------------+---------------------------------------------+---------------------------------+
| ``DB_PASSWORD``       | SQL backend password                        | Yes                             |
+-----------------------+---------------------------------------------+---------------------------------+

Running a Local Server
----------------------

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

.. code-block:: python

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