# einzelhandeltogo

## Model Draft

`Driver`

* User {name, email, ...}
* Phone Number
* GPS Position {longitude, latitude}
* Status {available, unavailable, idle}

`Buyer`

* User {name, email, ...}
* Phone Number
* Address
* Postal Address {street, city, province, code}

`Seller`

* User {name, email, ...}
* Company Name
* Phone Number
* Postal Address {street, city, province, code}
* Shop Categories {names, icons}
* Products
* Status (open, closed, idle)

`Transaction`
* Created [timestamp]
* Loaded
* Delivered
* Driver
* Buyer
* Seller
* Transaction Content

## Brainstorming Results

Technologie-Stack

* Webapp
  * Frontend: Angular (Christopher, Philipp)
  * Middleware: Django (Max, Christoph)
  * Datenbank: Postgres


Features
* Matching von Einzelhandel mit Taxis anhand von Nähe zu Geschäft
  * Taxifahrer wird automatisch der Bestellung basierend auf Standort ausgewählt
  * Taxifahrer bekommt Mitteilung und Ziele angezeigt
  * Integration von GPS-Positionierung Laden & Fahrer
  * Taxifahrer kann Profil pflegen
* Händler können Profil (allg. Beschreibung, Links, Kontakt) anlegen und Leistungen anbieten
* Kontaktdaten von Händlern werden veröffentlicht und können von Interessenten eingesehen werden
  * Händler legt Bestellung als zu transporierendes Paket an
* Browsing-Feature für Kunden ("Stöbern")
  * Location-based recommendation
* Sicherstellung dass das Produkt wirklich ankommt
  * Foto, Barcode, ...
  * Kontaktlose Bestätigung (via bluetooth) durch Käufer
* Optional: Abwicklung Kaufprozess

*Source: https://yourpart.eu/p/wirvscorona*

## How to run the project

First time setup
* install Python 3
* install pgAdmin 4
* configure user `etg` with password `etg`
* create database named `etg`
* in project directory create virtual environment `Windows: python -m venv venv`
* one time migration at the beginning `python manage.py migrate`
* create superuser `python manage.py createsuperuser`

For running project
* activate virtual environment `Windows: .\venv\Scripts\activate`
* install requirements `Windows: pip install -r requirements.txt`
* run migrations `python manage.py migrate`
* run server `python manage.py runserver`
* find service @ 127.0.0.1:8000
* find admin interface @ 127.0.0.1:8000/admin
* find endpoint description @ 127.0.0.1:8000/swagger
