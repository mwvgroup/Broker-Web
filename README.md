# Django based website for the Pitt-Google Broker

## Installation

Download the code from this repository and install the dependencies

```bash
git clone https://github.com/mwvgroup/broker-tom
cd broker-tom
pip install -r requirements.txt
```

## Environmental Variables

The following table outlines environmental variables that can be used to 
configure standard DJANGO settings. These can be configured manually, or
specified in a file `broker_web/.env`. At least one of `DEBUG` or 
`ALLOWED_HOSTS` must be set for the app to run.

| Variable         | Example                                                |
|------------------|--------------------------------------------------------|
| `SECRET_KEY`     | `"b9ch7q*1ael5p-6n3432$a3ds9ksgm$e9hgm5zba^5c%82d!)8"` |
| `DEBUG`          | `true`                                                 |
| `ALLOWED_HOSTS`  | `example_domain.com,example_2.com`                     |
| `CONTACT_EMAILS` | `admin1@mail.com,admin2@mail.com`                      |

## Launching a Local Version

To launch the application, run the following and follow the prompts:

```bash
export DJANGO_DEBUG=true  # Must be set unless DJANGO_ALLOWED_HOSTS is set
python broker_web/manage.py migrate --run-syncdb  # Build back end database
python broker_web/manage.py createsuperuser  # Add an admin account so you can access all features
python broker_web/manage.py runserver  # Run the web server
```

## Deployment Security Concerns

This repository is not configured for secure deployment without modification.
Please take the following steps before deployment

1. Update variables in `broker_tom/broker_tom/settings.py` under the comment `# SECURITY WARNING`.
1. Update `broker_tom/templates/recaptcha.html` to reflect the correct reCAPTCHA public key.
   This project uses reCAPTCHA V2 (see https://www.google.com/recaptcha)
1. For debugging, the captcha verification can be turned off by disabling certain javascript features in browser. Move captcha verification to serverside. 
