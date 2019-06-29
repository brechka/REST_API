REST API with Flask and Python that represents items

The repository consist of 3 branches:
1) Master;
2) REST_API_init;
3) REST_API_SQLAlchemy

1) Master branch contains the final version of REST API with using SQLAlchemy for storing objects 
   to a relational database. It also includes user registration and authentication. Besides storing items also 
   was added a concept of stores.
   Branch contains a few Heroku required files for deploying APP on the internet. Due to a limit space and hours
   that Heroku provided we use PostgreSQL instead of SQLAlchemy. Limit for rows in this DB is 10000 (not for 
   production application).

2) REST_API_init branch contains the initial version of code that represents items. It includes persistent storage 
   of Items to a SQLite database and user registration and authentication.

3) REST_API_SQLAlchemy contains the code REST API with using SQLAlchemy for storing objects to a relational database,
   user registration and authentication. Files was devided into 2 packages: models and resources. 