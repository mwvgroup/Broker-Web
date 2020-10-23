Installation and Setup
======================

This page provides instructions for downloading, configuring, and running
a local copy the website.

Python Dependencies
-------------------

The broker website is packaged as the ``broker_web`` Python package, which
is available on `GitHub`_. To download the code from this repository and
install the dependencies, use:

.. code-block:: bash

   # Download project source code
   git clone https://github.com/mwvgroup/Broker-Web

   # Install Python dependencies with pip
   pip install -r Broker-Web/requirements.txt

Local Database
--------------

The source code expects you to have already established a MySQL database for
storing user and website data. If this database is not already available on
your local machine, you can create a user and databases for development
as shown below.

.. important:: It is strongly recommended for security reasons that you use
   a dedicated set of credentials when developing. This means the username
   and password for your local database should be different from any
   credentials you may have for the deployed database.

.. code-block:: mysql

   $ mysql -u root -p
   mysql> CREATE DATABASE [DB_NAME];
   mysql> CREATE USER '[DB_USER]'@'localhost' IDENTIFIED BY '[DB_PASSWORD]';
   mysql> GRANT ALL PRIVILEGES ON [DB_NAME].* TO 'DB_USER'@'localhost';
   mysql> FLUSH PRIVILEGES;
   mysql> quit;

You should repeat the above process twice: Once for the database you
wish to develop against, and once to set permissions for the database
you want to run tests against. The testing database has the same name
of the development database prefixed with the word ``'test_'``.

.. code-block:: mysql

   $ mysql -u root -p
   mysql> CREATE DATABASE test_[DB_NAME];
   ...

Environmental Variables
-----------------------

The following table outlines environmental variables that can be used to
configure standard Django settings. The ``ALLOWED_HOSTS`` variable
must be set for the app to run if ``DEBUG`` is set to ``False`` (the default).

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
| ``CONTACT_EMAILS``    | List of developer contact emails         | No                              |
+-----------------------+------------------------------------------+---------------------------------+

You will also need to specify various environmental variables for configuring
your database connection.

+---------------------------+------------------------------------------+----------------------------------+
| Variable                  | Description                              | Required                         |
+===========================+==========================================+==================================+
| ``DB_NAME``               | Name of the MySQL database for user data | No (Default = ``web_backend``)   |
+---------------------------+------------------------------------------+----------------------------------+
| ``DB_USER``               | MySQL username                           | Yes                              |
+---------------------------+------------------------------------------+----------------------------------+
| ``DB_PASSWORD``           | MySQL password                           | Yes                              |
+---------------------------+------------------------------------------+----------------------------------+
| ``DB_HOST``               | Database host connection                 | For local database only          |
+---------------------------+------------------------------------------+----------------------------------+
| ``DB_PASSWORD``           | Port number to connect on                | For local database only          |
+---------------------------+------------------------------------------+----------------------------------+
| ``TEST_NAME``             | Name of the MySQL database used in tests | No (Default = ``text_[DB_NAME]``)|
+---------------------------+------------------------------------------+----------------------------------+
| ``ZTF_ALERTS_TABLE_NAME`` | Name of the Bigquery table with ZTF alert| No (Default = ``text_[DB_NAME]``)|
|                           | data ingested by the broker pipeline.    |                                  |
+---------------------------+------------------------------------------+----------------------------------+

.. note:: For convenience, environmental variables can be specified in a
   ``.env`` file
   placed into the project's root directory. However, **the application will
   ignore ``.env`` files when running on the deployment server**.


.. _GitHub: https://github.com/mwvgroup/Broker-Web
.. _here: https://cloud.google.com/sdk/docs/downloads-interactive

Running a Local Instance
------------------------

With your databases created and environmental variables defined, you can configure
the database schema using the management script:

.. code-block:: bash

   python manage.py makemigrations
   python manage.py migrate --run-syncdb

At this point, it is also useful to create an admin account for the website:

.. code-block:: bash

   python manage.py createsuperuser

Finally, a local server for the website can then be launched in standard Django fashion:

.. code-block:: bash

   python manage.py runserver