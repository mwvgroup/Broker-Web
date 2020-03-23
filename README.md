# Django based website for the Pitt-Google Broker

## Installation

#### Python dependencies

To download the code from this repository and install the dependencies:

```bash
# Download project source code
git clone https://github.com/mwvgroup/broker-tom

# Install Python dependencies with pip
cd broker-tom
pip install -r requirements.txt
```

#### GCP Dependencies

This site is built to run on the App Engine standard environment. To access
GCP resources you will need to install the `gcloud` command line API which is
available  [here](https://cloud.google.com/sdk/docs/downloads-interactive).
You will also need to install Google Cloud SQL Proxy so the website can
connect to the necessary SQL backends when running locally. 

For Mac OS 64 bit, use: 

```bash
curl -o cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.darwin.amd64
chmod +x cloud_sql_proxy
```

For Linux 64 bit, use:

```bash
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
chmod +x cloud_sql_proxy
```

For other installations see [https://cloud.google.com/python/django/appengine](https://cloud.google.com/python/django/appengine).

## Configuration

Full documentation on configuring remote and local environments is available
in the [Google Docs](https://cloud.google.com/python/django/appengine).
Please refer to the official Google docs if configuring an environment from
scratch. If you are developing against the official Pitt-Google Broker
GCP project, then these steps have already been taken for you. However, you
will need to setup a user name and password for the application's SQL
instance [here](https://console.cloud.google.com/sql/instances). The
relevant instance is the MySQL `broker-web` database.

### Environmental Variables

The following table outlines environmental variables that can be used to 
configure standard DJANGO settings. These can be configured manually, or
specified in a file `broker_web/.env`. 

| Variable         | Example                                                |
|------------------|--------------------------------------------------------|
| `SECRET_KEY`     | `"b9ch7q*1ael5p-6n3432$a3ds9ksgm$e9hgm5zba^5c%82d!)8"` |
| `DEBUG`          | `true`                                                 |
| `ALLOWED_HOSTS`  | `example_domain.com,example_2.com`                     |
| `CONTACT_EMAILS` | `admin1@mail.com,admin2@mail.com`                      |


At least one of `DEBUG` or `ALLOWED_HOSTS` must be set for the app to run.
Additionally, the `USER` and `PASSWORD` variables must be set to represent
your authentication settings for the MySQL backend.

## Launching a Local Version

Start by launching the SQL proxy so the application can connect to the cloud.

```bash
./cloud_sql_proxy -instances "ardent-cycling-243415:us-east1:broker-web"=tcp:3306
```

Next, launch the web application via the management script:

```bash
python broker_web/manage.py runserver  # Run the web server
```

## Deployment Security Concerns

This repository is not configured for secure deployment without modification.
Please take the following steps before deployment

1. Update `broker_tom/templates/recaptcha.html` to reflect the correct reCAPTCHA public key.
   This project uses reCAPTCHA V2 (see https://www.google.com/recaptcha)
1. For debugging, the captcha verification can be turned off by disabling certain javascript features in browser. Move captcha verification to serverside. 
