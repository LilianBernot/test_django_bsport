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