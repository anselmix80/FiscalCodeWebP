# FiscalCode WEB: Your Personal Tax Code Calculator

FiscalCode WEB is a comprehensive and user-friendly web application designed to:

- **Calculate your Italian tax code (codice fiscale) quickly and accurately:** Simply input your name, surname, birth date, place of birth, and gender, and the application will calculate your unique Italian tax code based on official ISTAT data.

- **Determine your age:** In addition to calculating your tax code, the application will also display your age based on the birth date you provide.

- **Check the weather forecast:** While calculating your tax code, you can also check the weather forecast for your city.

- **Shell commands:** The application also supports shell commands for retrieving data from Istat and generating Fiscal Code with AdE rules and also retrieve weather forecast.

- **Advanced functionality:** Behind the scenes, the application utilizes a NoSQL database to store Italian municipality data and the configurations required to access weather forecasts. The backend is developed using Python, Django, and Django Rest Framework, while the frontend is built with Vue.js for a modern and reactive user interface.

## Table of Contents

- [FiscalCode WEB: Your Personal Tax Code Calculator](#fiscalcode-web-your-personal-tax-code-calculator)
  - [Table of Contents](#table-of-contents)
  - [Pre-Requisites](#pre-requisites)
  - [Installation](#installation)
  - [ENVIRONMENT Configuration (.env file)](#environment-configuration-env-file)
  - [Features](#features)
  - [Utilities](#utilities)
  - [Contributing](#contributing)
  - [License](#license)
  - [API example](#api-example)
  - [VUE components](#vue-components)
  - [SERVICE URLs](#service-urls)
  - [NOTE](#note)

## Pre-Requisites

- Python 3.9+
- Node.js 18+
- npm
- Docker

## Installation

1. Clone the repository: `git clone https://github.com/anselmix80/FiscalCodeWeb.git`
2. **DEV Installation:**
   1. **DEV: ACTIVATE VIRTUAL ENVIRONMENT**
        - `python -m venv venv`
        - `source venv/bin/activate`
   2. **DEV: BACKEND**
        - `cd backend`
        - `pip install -r requirements.txt`
        - Set up any environment variables or configurations:
          - Edit the `.env` file in the backend directory, see details below
        - Configure Django backend environment:
           - `python manage.py makemigrations`
           - `python manage.py makemigrations api`
           - `python manage.py makemigrations weather`
           - `python manage.py migrate --no-input`
        - Create superuser:
           - `python manage.py createsuperuser --noinput`
        - Populate initial data:
           - `python scripts/initial_data.py`
        - Run the backend server:
           - `python manage.py runserver`
   3. **DEV: FRONTEND**
      - `cd frontend`
      - `npm install`
      - `npm run dev &`

3. **PROD Installation:**
   1. run `./startDoc.sh`

## ENVIRONMENT Configuration (.env file)

These are the parameters for **backend .env** file:

- DJANGO_SUPERUSER_USERNAME -> Set Django superuser username
- DJANGO_SUPERUSER_PASSWORD -> Set Django superuser password
- DJANGO_SUPERUSER_EMAIL=  -> Set Django superuser email # Optional
- SECRET_KEY -> Set Django secret key
- URL=[https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv](https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv)
- INPUT_FILENAME=commons.csv
- INPUT_FILENAME_WEATHER=weather_icon.csv
- OUTPUT_FILENAME=output.csv
- DB_FILE=db.sqlite3
- TABLE_NAME=api_common
- TABLE_NAME_WEATHER=weather_icon_weather
- SERVER_DEV -> Must be the name of your development server
- WEATHER_KEY -> You have to create a free account [weatherapi](https://www.weatherapi.com/pricing.aspx) to get one
- LOG_LEVEL=INFO
- LOG_BACKUP_COUNT=5
- LOG_MAX_BYTES=1048576

**Remember:
DJANGO_SUPERUSER_EMAIL, SECRET_KEY, SERVER_DEV and WEATHER_KEY are mandatory and must be set**

These are the parameters for **frontend .env** file:

- VITE_APP_ROOT_API= [http://10.5.0.7:8080/api/](http://10.5.0.7:8080/api/)
- VITE_APP_ROOT_WEATHER= [http://10.5.0.7:8080/weather/](http://10.5.0.7:8080/weather/)

## Features

- You can use the web interface frontend to calculate your tax code quickly and easily.

  ![Alt text](/images/app.jpg "app")

- You can also use the shell commands (from cmd folder) to retrieve data from Istat and generate Fiscal Code with AdE rules.

  Example usage: `python fiscal_code.py R Mario Rossi 01/01/1970 Roma M` R is a flag to force to retrieve data from ISTAT.
  
  ![Alt text](/images/cmd.jpg "cmd")

- You can also use the shell commands to retrieve weather forecast
  Example: `python weather.py` remeber to add the weather key inside weather.py
  
  ![Alt text](/images/weather.jpg "weather")

- You can also use directly the API to retrieve data from Istat and generate Fiscal Code with AdE rules.

  Example usage: `curl -X POST -H "Content-Type: application/json" -d '{"name": "Mario", "surname": "Rossi", "date": "1970-01-01", "city": "Roma", "sex": "M"}' http://10.5.0.7:8080/api/fc/`

- You can also use directly the API to retrieve data

  ![Alt text](/images/api.jpg "api")

## Utilities

**Cleanup Docker:**

- `docker compose down --volumes --remove-orphans --rmi all`
- `docker system prune -a -f`

**Cleanup App data and cache:**

- Inside the `backend/scripts` directory, run the command `./clean_up.sh`

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request

## License

This project is licensed under the [MIT License](LICENSE).

## API example

{

    "name": "Mario",
    "surname": "Rossi",
    "date": "1970-01-01",
    "city": "Roma",
    "sex": "M"

}

## VUE components

npm create vue@lates web

npm install vue-select@beta

npm install bootstrap

npm install axios

## SERVICE URLs

<http://10.5.0.7:8080/api/fc/> --> rest api

<http://10.5.0.7:8080/admin/> --> admin

<http://localhost:8080/> --> home page

<http://10.5.0.7:8080/weather/> --> weather api

## NOTE

Remember in .env to set SERVER_DEV to the name of your development server otherwise it will run as a production server
