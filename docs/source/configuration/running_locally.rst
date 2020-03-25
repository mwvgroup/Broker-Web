Launching a Local Version
=========================

These instructions will allow you to deploy a local version of the PGB website
which runs against the websites full deployment SQL backend in GCP.

Environmental Variables
-----------------------

The following table outlines environmental variables that can be used to
configure application settings. Note that at least one of ``DEBUG`` or
``ALLOWED_HOSTS`` must be set for the app to run. For convenience, these can
be specified in a ``.env`` file placed into the project's root directory.
However, the application will specifically ignore ``.env`` files when running
on the deployment server.

+-----------------------+---------------------------------------------+---------------------------------+
| Variable              | Example                                     | Required                        |
+=======================+=============================================+=================================+
| ``SECRET_KEY``        | ``"b9ch7q*1ael5p..."``                      | Yes                             |
+-----------------------+---------------------------------------------+---------------------------------+
| ``DEBUG``             | ``true``                                    | If ``ALLOWED_HOSTS`` is not set |
+-----------------------+---------------------------------------------+---------------------------------+
| ``ALLOWED_HOSTS``     | ``example_domain.com,example_domain_2.com`` | If ``Debug`` is not ``true``    |
+-----------------------+---------------------------------------------+---------------------------------+
| ``DB_USER``           |                                             | Yes                             |
+-----------------------+---------------------------------------------+---------------------------------+
| ``DB_PASSWORD``       |                                             | Yes                             |
+-----------------------+---------------------------------------------+---------------------------------+
| ``CONTACT_EMAIL``     | ``admin1@mail.com``                         | No                              |
+-----------------------+---------------------------------------------+---------------------------------+
| ``MJ_APIKEY_PUBLIC``  | ``admin1@mail.com,admin2@mail.com``         | No                              |
+-----------------------+---------------------------------------------+---------------------------------+
| ``MJ_APIKEY_PRIVATE`` | ``admin1@mail.com,admin2@mail.com``         | No                              |
+-----------------------+---------------------------------------------+---------------------------------+


Running a Local Server
----------------------

1. Configure environmental variables as defined in the previous section.

2. Start by launching the SQL proxy so the application can connect to the cloud.

.. code-block::

   ./cloud_sql_proxy -instances "ardent-cycling-243415:us-east1:broker-web"=tcp:3306

3. Next, launch the web application via the management script:

.. code-block::

   python broker_web/manage.py runserver  # Run the web server

