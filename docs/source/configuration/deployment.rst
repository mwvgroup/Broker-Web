Deploying to App Engine
=======================

The production version of the website is hosted in the cloud using
`GCP App Engine <https://console.cloud.google.com/appengine>`_.
This page outlines instructions for deploying new versions of the website
source code to the cloud.

Updating Static Files
---------------------

Static files are updated in the cloud separately from deploying
changes to the source code. This includes pushing source code changes via
continuous deployment. Static files can be synced against a local
version of the project by running:

.. code-block:: bash

   gsutil -m rsync -r broker_web/static gs://[BUCKET_NAME]/static

Manual Deployment
-----------------

.. important:: The following section is provided for reference only. All
   updates to the official website should be performed via
   continuous deployment as outlined later in this document.

Deployment settings should be configured using the ``app.yaml`` file. The
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

Application versions can be deployed manually using the ``gcloud`` API. The
command below will automatically use the ``app.yaml`` file located in the
working directory.

.. code-block:: bash

   gcloud app deploy


Continuous Deployment
---------------------

.. note:: The TLDR of this section is to submit a pull request against the
   ``appengine-staging`` branch of the project repository. A new version of
   the website will start building automatically.

Similar to when deploying manually, an ``app.yaml`` configuration file must
be created to store deployment settings. However, instead of storing the file
locally, the file should be save to a GCP bucket. This file persists across
deployments and only needs to be replaced if you are changing the website's
deployment settings.
You will also need a ``cloudbuild.yml`` file to configure the website build
process. A version controlled copy of this file should be included with
the website's source code.

To trigger a new build, merge a pull request into the ``appengine-staging``
branch of the projet's repository. The new build will be automatically
triggered and it's progress can be tracked in
`Cloud Build <https://console.cloud.google.com/cloud-build/>`_.
If you run into deployment errors, the
`GCP docs <https://cloud.google.com/source-repositories/docs/quickstart-triggering-builds-with-source-repositories>`_
may be of some help.
