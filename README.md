# proxy-service-provider
Proxy Service Provider is an applcation to fetch proxies from different proxy provider site (HTTP(s) Proxies) and perform Functional test by configuring Proxy in OS Network Level to ensure the anonymality at core level

## Installation

### Create a Virtual Environment
Create a new environment for this project using conda

```shell
virtualenv -p python3 env
source env/bin/activate
```


### Now Install the Dependencies

Install Initial Dependencies

```shell
pip install -r requirements.txt

```

### Execute the following command to run the Django REST Framework Project


```shell
python manage.py runserver --settings=proxy_service_provider.settings.core

```

### For executing the frontend, go inside the frontend project directory and execute following command.


```shell
npm run install

npm run serve

```
