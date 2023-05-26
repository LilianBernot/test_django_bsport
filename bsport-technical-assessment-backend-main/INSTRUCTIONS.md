# Bsport technical assessment - Backend

## General

### How to run

This project is built with docker-compose, django, and django rest framework. You only need to have docker-compose working in your computer for it to run.

Run with :

```sh
docker-compose up 
```

Prepare / apply database migrations with :

```sh
docker-compose run --rm api ./manage.py makemigrations
docker-compose run --rm api ./manage.py migrate
```

### Structure

We currently have a very basic app containing only one model, overriding the AbstractUser interface from Django base admin models.

The configuration of the project is located in `general/` and the "applicative" code is in only one app : `user/`.

We want here to build an app to manage families of users.

## Tasks

The assessment is divided in 2 levels. Your level is defined in the email you received from the interview.

In the end your project will be run with `docker-compose` to check it. You will have to return a git repository.

### Level 1

Create a new app named `family`. This app will contains all the necessary structure to build a family of user.

Constraints :

* A User have a father (nullable).
* A User have a mother (nullable).
* User can be in a relationship. Only user in a relationship can have children.
* A User have, for mother and father (separately) a "relationship rank" from 1 to 5.
* You can not touch the `user/` app, except for the relationship link.

Tasks : 

* Build the necessary model changes to store this new information.
* Add a viewset to add / edit children of couple of users.
    * only the authenticated user can add/edit their children.
    * only `is_staff==True` users can add user without any parent.
* Implement 100% coverage testing.


### Level 2

We now want to add some extra small features to this app.

Tasks :

**Ancestor relationship**

* Add a new field `ancestor_relationship_rank` on each user, computed as the average rank of relationship of mother/father, and 1/2 ponderated with the average relationship rank of parents with grandparents, 1/4 ponderated with average relationship rank of grandparents with great-grandparents, etc.
* Make sure this average is always consistent at the database-level.
* Think about the performance : this should run as fast as possible.

**Async task**

* As an added security, schedule an async task, running regularly, that will check the consistency of these ranks. This task should be parallelized as much as possible (CPU consumption on the database should be maxed-out). We recommend celery.
* Send an email with django email sender system, when all checks are done. This email should contains all information for debugging (exception raised, if any, stacktrace, etc.).
* Adapt the docker-compose to run it.

**Inconsistency**

* Implement the most robust check possible to avoid a User to be the parent/mother of one of his ancestor (aka avoid cycle in the ancestor DAG).

_Do not forget to keep 100% test coverage._

### Level 3

We now want to put this system to production. In order to do so we want to adapt some things to our project.

Tasks :

**Deploying**

* Implement a "real" server in front of django to run your code.
* Configure it and be ready to explain the overriden parameters.
* Stay with docker-compose.
* Keep the possibility to run everything with runserver locally.

**Healthcheck**

* Implement healthchecks status endpoint on all services running.
* Add a simple service running the healthchecks regularly (30s), and exposing an endpoint `/status/` that lists all failing service at last run.


**Caching**

* Add a caching system on `GET` endpoint.
* The cache should be invalidated every 5 min.
* The cache should be invalidated on any modification on the requested resource.

**Load test**

* Implement a load test to monitor the overall performance
* Where do you think is the danger ? What kind of monitoring would like to implement regarding this issue ?
