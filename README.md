# Movies Info with Flask and Vue #

## Project Setup ##

Tools needed:

- yarn
- pipenv
- postgres

### Seed the database ###

To populate the database, you're gonna need to create `movies_db`, the `movies_user` with password `12345678` and run the sql file located on the `backend/data` folder:

- createuser -dlW movies_user && createdb -O movies_user movies_db && psql -d movies_db -f ./data/dump.sql

### Install dependecies on both projects ###

For the SPA:

Navigate to the `frontend` folder and install the dependecies with yarn:

- cd frontend && yarn install

For the server side application:

Navigate to the `backend` folder, install the dependecies, enter the virtual environment and set the adequate environment variables:

- cd backend && pipenv install

### Run the project ###

To start the SPA in development mode, run the following command inside the `frontend` folder:

- yarn serve

To start the API in development mode, run the following commnd inside the `backend` folder:

- pipenv shell && export FLASK_ENV=development && export FLASK_APP=run.py && flask run

### Extras ###

You can find the Swagger documentation for the API accessing the followeing address http://localhost:5000
