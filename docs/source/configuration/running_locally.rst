Running Locally
===============

A development version of the website can be run locally in two configurations:

1. Running locally against a local database
2. Running locally against the deployment database in the cloud

The first configuration should be the default when developing. Working
against the deployment database is rarely necessary and should be undertaken
with care.

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
