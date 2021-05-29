# Django-GraphQL 

Returns the bank's subclass data based on its search of bank name and bank state using django-graphene.

## Approach to solve the problem
* Creating a server using django and then connecting it with the postgres backend.
* Adding all the required tables and views in the backend and inserting all the data.
* ```python manage.py inspectdb --include-views``` will generate the updated ```models.py``` file according to the changed database.
* After updating ```models.py``` in the django app, externally install graphene for django to avail graphql api service and included it in the ```settings.py```'s ```INSTALLED_APPS``` list.
* Gave a pointer to the schema for graphql endpoint.
* Defining graphql endpoint in ```urls.py```.
* Creating queries and mutations (not needed in current problem).
* Implemented search on multiple fields query.

## Tools/Tech used
* Django
* Django graphene
* PostgreSQL
* Heroku
* Postman

> For the crazy ones to explore its deployed [here](https://bank-branches-gql.herokuapp.com/gql/) and the testcases of the post requests are [here](https://www.postman.com/collections/53d5225e8a68bfb4f909).
