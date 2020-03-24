# Broker-Web
Website for the Pitt-Google Broker

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

This site is built to run on the App Engine standard environment. To access GCP resources you will need to install the `gcloud` command line API which is available  [here](https://cloud.google.com/sdk/docs/downloads-interactive). You will also need to install Google Cloud SQL Proxy so the website can connect to the necessary SQL backends when running locally. 

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

For other installations see the appropriate section of [https://cloud.google.com/python/django/appengine](https://cloud.google.com/python/django/appengine).

## Configuration

Full documentation on configuring Django applications for App Engine is available in the [Google Docs](https://cloud.google.com/python/django/appengine). Notes are provided here if configuring an environment from scratch. Many of these steps only need to be performed once. If you are developing against the official Pitt-Google Broker GCP project (currently `ardent-cycling-243415`) then these these steps should have already been taken and this section can be skipped.

#### Configure GCP

First configure a Storage Bucket for publicly hosting static files:

1. Create a bucket for hosting static files.
   ```bash
   gsutil mb -p [PROJECT_NAME] -c [STORAGE_CLASS] -l [BUCKET_LOCATION] -b on gs://[BUCKET_NAME]/
   ```
   
2. Make the bucket publicly readable
   ```bash
   gsutil defacl set public-read gs://broker-web-static
   ```

Next configure the Cloud SQL backend for the website:

1. Enable the Cloud SQL Admin API.

   ```bash
   gcloud services enable sqladmin
   ```

2. Create a Cloud SQL instance.

   ```bash
   gcloud sql instances create [INSTANCE_NAME] --tier=[MACHINE_TYPE] --region=[REGION]
   ```

3. Create a database on the Cloud SQL instance.

   ```bash
   gcloud sql databases create [DATABASE_NAME] --instance=[INSTANCE_NAME]
   ```

4. Create a new user account that your application will user to access the database.

   ```bash
   gcloud sql users create [USER_NAME] --instance=[INSTANCE_NAME] --password=[PASSWORD]
   ```

#### Configure the Django Application


1. Use the Cloud SDK to fetch the connection name of your instance. The connection name will be listed in the format  `[PROJECT_NAME]:[REGION_NAME]:[INSTANCE_NAME]`.

   ```bash
   gcloud sql instances describe [INSTANCE_NAME]
   ```

2. Make sure the database settings in the Django application point to the new database you just created. In general, the settings should look like the following:

   ```python
   # broker_web/settings.py
   
   if os.getenv('GAE_APPLICATION', None):
       # Running on production App Engine, so connect to Google Cloud SQL using
       # the unix socket at /cloudsql/<your-cloudsql-connection string>
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.mysql',  # Assuming you are using MySQL
               'HOST': '/cloudsql/[CONNECTION_NAME]',
               'NAME': '[DATABASE_NAME]',
               # You'll probably want to set the auth data in your environment
               'USER': '[DATABASE_USER]',  
               'PASSWORD': '[DATABASE_PASSWORD]',
           }
       }
   
   else:
       # Running locally so connect to Cloud SQL via the proxy.
       # To start the proxy see https://cloud.google.com/sql/docs/mysql-connect-proxy
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.mysql',
               'HOST': '127.0.0.1',
               'PORT': '3306',
               'NAME': '[DATABASE_NAME]',
               # Here is an example using django-environ
               'USER': env.str('DB_USER'),
               'PASSWORD': env.str('DB_PASSWORD'),
           }
       }
   ```

3. Launch the SQL proxy so your local application can connect to the SQL database in GCP.
   ```bash
   ./cloud_sql_proxy -instances "[REGION_NAME]"=tcp:3306
   ```

4. Make the necessary database migrations and set up an admin account.

   ```bash
   python manage.py migrate --sync-db 
   python manage.py createsuperuser
   ```

5. Add your public recaptcha key to `broker_web/templates/recaptcha.html`

## Launching a Local Version


#### Environmental Variables

The following table outlines environmental variables that can be used to configure standard DJANGO settings. These can be configured manually, or specified in a file `broker_web/.env`. 

| Variable         | Example                                                |
| ---------------- | ------------------------------------------------------ |
| `SECRET_KEY`     | `"b9ch7q*1ael5p-6n3432$a3ds9ksgm$e9hgm5zba^5c%82d!)8"` |
| `DEBUG`          | `true`                                                 |
| `ALLOWED_HOSTS`  | `example_domain.com,example_2.com`                     |
| `CONTACT_EMAILS` | `admin1@mail.com,admin2@mail.com`                      |

At least one of `DEBUG` or `ALLOWED_HOSTS` must be set for the app to run. Additionally, the `USER` and `PASSWORD` variables must be set to represent your authentication settings for the MySQL backend.

#### Running a Local Server

Start by launching the SQL proxy so the application can connect to the cloud.

```bash
./cloud_sql_proxy -instances "ardent-cycling-243415:us-east1:broker-web"=tcp:3306
```

Next, launch the web application via the management script:

```bash
python broker_web/manage.py runserver  # Run the web server
```

## Deploying a New Version to Production

Application versions can be deployed manually using `gcloud`:

1. Synchronize static files in the storage bucket

   ```bash
   gsutil -m rsync -r broker_web/static gs://[BUCKET_LOCATION]/static
   ```
   
2. Deploy the new source code

   ```bash
   gcloud app deploy
   ```


## Deployment Security Concerns

This repository is not configured for secure deployment without modification.
Please take the following steps before deployment

1. Update `broker_tom/templates/recaptcha.html` to reflect the correct reCAPTCHA public key.
   This project uses reCAPTCHA V2 (see https://www.google.com/recaptcha)
1. For debugging, the captcha verification can be turned off by disabling certain javascript features in browser. Move captcha verification to serverside. 
