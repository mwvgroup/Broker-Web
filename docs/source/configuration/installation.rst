Installation
============

This page provides instructions for downloading the necessary dependancies and
deploying the website against a remote or local database.

Python dependencies
-------------------

The broker website is packaged as the ``broker_web`` Python package, which
is available on `GitHub`_. To download the code from this repository and
install the dependencies:

.. code-block:: bash

   # Download project source code
   git clone https://github.com/mwvgroup/Broker-Web

   # Install Python dependencies with pip
   cd Broker-Web
   pip install -r requirements.txt


GCP Dependencies
----------------

The broker website is built to run in the cloud using App Engine.
If you intend to run the website against a local development database,
this step can be skipped. If you intend to run the website
using GCP resources you will need to install the ``gcloud`` command line
tool which is available `here`_.

You will also need to install the Google
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

.. _GitHub: https://github.com/mwvgroup/Broker-Web
.. _here: https://cloud.google.com/sdk/docs/downloads-interactive
.. _App Engine docs: https://cloud.google.com/python/django/appengine](https://cloud.google.com/python/django/appengine