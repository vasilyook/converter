# Converter

This app converts your currency.

![python](https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white) ![django](https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white)

## Installation 
### Install Requirements
```pip install -r requirements.txt```

### Add API-KEY
Copy .env.example to .env. 
Get your API-KEY from [API Ninjas](https://api-ninjas.com/)
Put your API-KEY to .env
    
### Start Up Server (Windows)
```py manage.py runserver```

The application should be available at 
http://127.0.0.1:8000/converter/api/rates?from=EUR&to=RUB&value=1 
through your browser

You can edit in url:
from - having currency
to - wanted currency
value - amount
