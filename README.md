# Q-CTRL Back-end Engineering Challenge


## Scope

The Technical Challenge required to implement a Restful API using Django and PostgreSQL database.

## Table of Contents

- Software and Packages
- Environment Setup
- API Documentation
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

## Software and Packages

- Python 3.8
- Django 3.0
- djangorestframework 3.11.0
- psycopg2 2.8.4
- pylint-django 2.0.13

## Environment Setup

1. To get Started we first setup a virtual env for our django project. Any packages installed will be localized in this virtual environment.. 

Run the following in your terminal:
```
         pip install pipenv
```
```
         pipenv shell
```


2. Install the required Software and packages.

##Database Setup

Initially backed by sqllite, we have to change the database configurations to postgreSQL as required by this project. 
We can change the database settings from ./settings.py. 
 qctrl_api-->./settings.py
```        
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'postgres',
        'PASSWORD': '********',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## run test

```
    python manage.py test
```
## run application server

```
    python manage.py runserver
```

## API Documentation

Description|HTTP Method|Endpoint|Status|Test
---|---|---|---|---
Create a control|POST|/control/|success|tested
List all Controls|GET|/control/|success|tested
Search|GET|/control/?q=query/|success|NA
Get specific control|GET|/control/id|success|tested
Update specific control|UPDATE|/control/id/|success|tested
Delete specific control|DELETE|/control/id/|success|tested
Upload bulk CSV|PUT|/control/file/|NA|NA
Download all as CSV|GET|/control/file/|NA|NA

## Contributing

See [Contributing](https://github.com/qctrl/.github/blob/master/CONTRIBUTING.md).

## Credits

See [Contributors](https://github.com/qctrl/back-end-challenge/graphs/contributors).

## License

See [LICENSE](LICENSE).
