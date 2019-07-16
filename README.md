# REST API with Flask and Python that represents items

The repository consist of 2 branches:
1) [Master](https://github.com/brechka/REST_API);
2) [REST_API_init](https://github.com/brechka/REST_API/tree/REST_API_init).

**Master branch** - the main code. Contains the final version of REST API with using PostgreSQL for storing objects. 
Branch contains a few **Heroku** required files for deploying APP. We used PostgreSQL instead of SQLite due to a loosing data 
in case of destroying Dyno (has a limited running time). We'he also deployed our App on **Digital Ocean** public server.
App includes user registration and authentication. Besides storing items also was added a concept of stores.

**REST_API_init branch** contains the initial, simple version of code that represents items. It includes persistent 
storage of Items to a SQLite database and user registration and authentication. 


## Master branch

The REST API was built using Python, Flask, Flask-RESTful and PostgreSQL. PostgreSQL was used due to Also were used uWSGI 
that provides multi-threading and auto restarting after failure as well as psycopg2. SQLAlchemy uses psycopg2 to 
communicate with PostgreSQL.

REST API lets users register and log in, as well as create stores and items. There are two folders: models 
and resources (with item.py, store.py, and user.py files in both folders) and run.py, app.py, db.py, 
blacklist.py, sequrity.py and a few Heroku required files (Procfile, requirements.txt, runtime.txt, uwsgi.ini).

A Model is a representation of what our application deals with internally. Whenever two parts of application 
communicate with one another, they'll do so mainly by using Models.

A Resource is what defines how clients will interact with REST API. In the resource are defined the endpoints 
where clients will have to send requests with required data. Resources use Models to communicate with other parts 
of the application and to interact with the database.


## Usage

**API deployed to Heroku**

Using the following URL in Postman, you can try the Rest API with the resources defined in the app.py file.
(if you enter this URL in browser, you will recieve a 404 Error because path wasn't determined)

```
https://itemstores-restful-api.herokuapp.com/
```

**API deployed to DigitalOcean**

Using our server URL in Postman, you can try the Rest API with the resources defined in the app.py file.

```
http://165.22.21.98
```


## Description

###### [run.py](https://github.com/brechka/REST_API/blob/master/run.py)

run.py is used for running App in Heroku.

###### [app.py](https://github.com/brechka/REST_API/blob/master/app.py)

In app.py Flask application is initialized and configured. API resources is also seted up.

###### [db.py](https://github.com/brechka/REST_API/blob/master/db.py)

Database Python object is created, so all other files import the database variable from this file.

###### [security.py](https://github.com/brechka/REST_API/blob/master/sequrity.py)

The file provides user authentication, creation a JWT-token and returning it to user.


**Heroku files**

Some files was added to tell Heroku how to run the App.

###### [runtime.txt](https://github.com/brechka/REST_API/blob/master/runtime.txt)

The files contains what language and version was used for the application.

###### [requirements.txt](https://github.com/brechka/REST_API/blob/master/requirements.txt)

The files specifies all the dependencies of the project. So to run the APP Heroku with using pip installs the 
following packages:

```
Flask
Flask-RESTful
Flask-JWT
Flask-SQLAlchemy
uwsgi
psycopg2
```

###### [uwsgi.ini](https://github.com/brechka/REST_API/blob/master/uwsgi.ini)

Configuration file. Necessary for running a Python app with using uWSGI. This file is used to tell uWSGI how to 
create and run a service.

Module starts application (will be called by procfile):

```
module = run:app
```

###### [Procfile](https://github.com/brechka/REST_API/blob/master/Procfile)

This file tells Heroku to use uWSGI for running our App (run uWSGI process with uwsgi.ini file):

```
web: uwsgi uwsgi.ini
```


**Models folder**

###### [item.py](https://github.com/brechka/REST_API/blob/master/models/item.py)

The ItemModel contains a definition of what data application deals with, and ways to interact with that data. 
Essentially it is a class with four properties:

- *id;*
- *name;*
- *price;*
- *store_id.*

Methods in the class can be used to find items by name, save them to the database, or retrieve them. 

###### [store.py](https://github.com/brechka/REST_API/blob/master/models/store.py)

The StoreModel is another definition of data application deals with. It contains two properties:

- *id;*
- *name.*

Because every ItemModel has a store_id property, StoreModels are able to use SQLAlchemy to find the ones 
that have a store_id equal to the StoreModel's id. It can do that by using SQLAlchemy's db.relationship().

###### [user.py](https://github.com/brechka/REST_API/blob/master/models/user.py)

The UserModel contains 3 properties:

- *id;*
- *username;*
- *password.*


**Resources folder**

###### [item.py](https://github.com/brechka/REST_API/blob/master/resources/item.py)

The resources/item.py defines an Item and ItemList resources which can be used to retrieve one or multiple items 
at once via the API.

###### [store.py](https://github.com/brechka/REST_API/blob/master/resources/store.py)

The Store resource defines how users can get, create and delete stores. StoreList resource is defined to retrieve 
all stores in our API.
As we run APP using SQLite, the restriction of creating a store before creating an item does not apply. You could 
give an item a store_id of a store that doesn't exist, and SQLite would accept it. But for fully-fledged database, 
such as PostgreSQL or MySQL, the restriction works, so the id of the store and the store_id of the item must match.

###### [user.py](https://github.com/brechka/REST_API/blob/master/resources/user.py)

These resource allows user to sign up.




