# Cabin Reservations Scraper

A script that logins to the river homes owner portal, and extracts all data from the unit reservations table, and writes it into a json file

## Setup  

1. Setup virtual environment, install dependencies, and create *credentials.py*

    ```bash
    #create a new virtual env inside the directory
    $ python3 -m venv env

    #activate the environment
    $ source env/bin/activate

    #install dependencies
    (env)
    $ pip install -r requirements.txt

    #create credentials.py (to store EMAIL & PIN)
    (env)
    $ touch credentials.py
    ```

2. Add EMAIL & PIN variables in *credentials.py*

    ```python
    EMAIL = 'name@example.com'
    PIN = '5555'
    ```

## Usage
Just run the *scraper.py*! (Make sure you have the virtual environment activated)

```bash
(env)
$ python3 scraper.py
```
- The first time you run the script, a new file, *reservations.json*, will be created
- If *reservations.json* already exists, the script will rewrite with the most recent data every time you run the script

## Notes
Deactivating the virtual environment: 

```bash
(env)
$ deactivate
```