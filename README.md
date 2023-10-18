ARVUTIL PEAVAD INSTALLITUD OLEMA:
Python https://www.python.org/downloads/
Node https://nodejs.org/en/download
Postgres https://www.postgresql.org/download/

POSTGRES:
Käivitage Postgres server nt pordil 5432 (default port)
Tehke seal andmebaas nimega ‘rik’, selleks võib kasutada Postico2 https://eggerapps.at/postico2/ (ainult MAC) või kui olete windows arvutil saab kasutada DBeaver https://dbeaver.io/download/
Saab ka terminali kasutada kirjutades:

- psql -U username
- CREATE DATABASE rik;

BACK-END:
Kopeeri github projekt IDE-s (nt VsCode) https://github.com/artjomTerminator01/rik_back.git

Failis alembic.ini 62 real on sqlalchemy.url – asetage see url enda andmebaasi urliga
Tehke sama failis database.py 6 real kus on DATABASE_URL

url peab olema järgmises formaadis: postgresql://%(DB_USER)s:%(DB_PASSWORD)s@{LOCALHOST URL}/%{DB_NAME}

näidis salasõnata – postgresql://postgres@localhost:5432/rik
näidis salasõnaga - postgresql://postgres:qwerty123@localhost:5432/rik

Olles projekti kaustas kirjutage terminali

- Kui olete windows masinal siis peate endale looma ka Virtual environment
  python -m venv /path/to/new/virtual/environment  
  https://docs.python.org/3/library/venv.html

- pip install -r /path/to/requirements.txt
  https://www.freecodecamp.org/news/python-requirementstxt-explained/#:~:text=requirements.txt%20is%20a%20file,environment%20and%20makes%20collaboration%20easier.
- alembic upgrade head
  https://alembic.sqlalchemy.org/en/latest/tutorial.html
- uvicorn main:app --reload
  https://www.uvicorn.org/

FRONT-END:
Kopeeri github projekt IDE-s (nt VsCode) teises aknas
https://github.com/artjomTerminator01/rik_front.git

Terminal:
1- npm install - https://docs.npmjs.com/cli/v8/commands/npm-install
2- npm start - https://create-react-app.dev/docs/getting-started/

RAKENDUS:
Andmebaasis on lisatud 3 inimest migratsiooni käigus, rakenduse testimiseks tehke firma valmis vajutades ‘CREATE COMPANY’ navbaris. Pärast firma loomist saate seda näha avalehel ka vajutades firma nimele olete navigeeritud firma vaatele. Selle vaadel on nupp ‘CHANGE MEMBERSHIP’ mis navigeerib lehele kus sate lisada vee osanike või muuta olemasolevate osanike kapitaali.
