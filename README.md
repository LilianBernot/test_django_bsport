New model : 

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


At first, easy table : 
Family : 
- user : type User, PK 
- mother / father : type User, FK
- mother_relation_rank / fath... : type int
- relationship : type User, FK



Can check a user on : 
family/users/{email}
Code to find it is really bad : when asking for User.objects.get(email=email), I have the error "" 'str' does not support 'get' "" or something close


Constraints :

* A User have a father (nullable) : done
* A User have a mother (nullable) : done
* User can be in a relationship. Only user in a relationship can have children : user can have only one child for now (complication doing the form), if he says he has a child but is not in relationship, the form tells him it is impossible.
* A User have, for mother and father (separately) a "relationship rank" from 1 to 5 : wouldlike to change the database but with a reduced model, done
* You can not touch the `user/` app, except for the relationship link.

Tasks : 

* Build the necessary model changes to store this new information : missing multiple children (only one child)
* Add a viewset to add / edit children of couple of users.
    * only the authenticated user can add/edit their children : to do
    * only `is_staff==True` users can add user without any parent : to do
* Implement 100% coverage testing.