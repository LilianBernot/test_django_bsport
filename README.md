Use : 
To launch the project, launch "docker-compose up".


This project tries to answer the following constraints and tasks. A little comment has been written to describe what has been done : 

Constraints :
* A User have a father (nullable) 
* A User have a mother (nullable) 
* User can be in a relationship. Only user in a relationship can have children : user can have only one child (complication doing the form), if he says he has a child but is not in relationship, the form tells him it is impossible.
* A User have, for mother and father (separately) a "relationship rank" from 1 to 5 : the ideal would be to develop the database described at the bottoom of the page. Currently, it is stored in the "Family" table as a simple int.
* You can not touch the `user/` app, except for the relationship link.

Tasks : 
* Build the necessary model changes to store this new information : missing multiple children (only one child)
* Add a viewset to add / edit children of couple of users.
    * only the authenticated user can add/edit their children : can change it's relationship status, partner and child
    * only `is_staff==True` users can add user without any parent : to do
* Implement 100% coverage testing.


To answer to the "authentication" problem, has been studied the auth module of Django but time has been missing to implement it.


Here is the db model that has been developped : 

Family : 
- user : type User, PK 
- mother / father : type User, FK
- mother_relation_rank / fath... : type int
- is_in_relationship : type Bool
- relationship : type User, FK
- child : type User, FK


Model which would be the best to develop : 

Family : 
- user_id = primary key 
- father_id = type User.id foreign key, can be null 
- mother_id = type User.id foreign key, can be null
- relationship_id = foreign key

Parent : 
- user_id = type User.id, foreign key 
- parent_id = type User.id, foreign key 
- rank = int between 1 and 5 
(user, parent) is the primary key of the table 

Relationship :
- relation_id = primary key 
- in_relation = boolean
- partner_id = type User.id, foreign key 
- children_list_id = type User.id, foreign key. Set to null if in_relation = false


The idea to build the "Parent" and "Relationship" tables is to be able to have "side-to"side" relation. For now, if we have a user id, we can have his parents and partner but the contrary is impossible. The proposed relational model would respect a good scheme.


