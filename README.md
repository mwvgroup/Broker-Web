Basic Django interface for the Pitt-Google Broker

## Installation

Download the code from this repository and install the dependencies

```bash
git clone https://github.com/mwvgroup/broker-tom
cd broker-tom
pip install -r requirements.txt
```

## Launching a Local (Demo) Version

To launch the application, run the following and follow the prompts:
```python
python broker_tom/manage.py migrate
python broker_tom/manage.py createsuperuser
python broker_tom/manage.py runserver
```

## Deployment Security Concerns

This repository is not configured for secure deployment without modification.
Please take the following steps before deployment

1. Update variables in `broker_tom/broker_tom/settings.py` under the comment `# SECURITY WARNING`.
1. Update `broker_tom/templates/recaptcha.html` to reflect the correct reCAPTCHA public key.
   This project uses reCAPTCHA V2 (see https://www.google.com/recaptcha)