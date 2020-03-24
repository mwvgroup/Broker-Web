Installation
============

The ``broker_web`` package runs against a Google Cloud backend. This means you
will need to install GCP tools in addition to the normal Python dependencies
associated with a Django website.

Python dependencies
-------------------


Source code for the website, including the necessary ``requirements.txt`` file,
is available on `GitHub`_. To download the code from this repository and
install the dependencies:

.. code-block::

   # Download project source code
   git clone https://github.com/mwvgroup/Broker-Web

   # Install Python dependencies with pip
   cd broker-tom
   pip install -r requirements.txt


GCP Dependencies
----------------

This site is built to run on GCP App Engine.
To access GCP resources you will need to install the ``gcloud`` command line
API which is available `here`_.
You will also need to install Google Cloud SQL Proxy so the website
can connect to the necessary SQL backends when running locally.

For Mac OS 64 bit, use:

.. code-block::

   curl -o cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.darwin.amd64
   chmod +x cloud_sql_proxy

For Linux 64 bit, use:

.. code-block::

   wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
   chmod +x cloud_sql_proxy


For other installations see the appropriate section of the
official `App Engine docs`_.

.. _GitHub: https://github.com/mwvgroup/Broker-Web
.. _here: https://cloud.google.com/sdk/docs/downloads-interactive
.. _App Engine docs: https://cloud.google.com/python/django/appengine](https://cloud.google.com/python/django/appengine