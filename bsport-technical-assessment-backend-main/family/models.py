from django.db import models
from user.models import User
from django.contrib.auth.models import BaseUserManager


# defines the characteristics of what we want to store
# ORM : Object-Relational Mapping. Python classes get converted into tables directly : persistance is managed by Django

class MyFamilyManager(BaseUserManager):
    def create_family(self, user, father, mother, father_relationship_rank, mother_relationship_rank, is_in_relationship, relationship, child):
        """
        Creates and saves a Family with the given email, father, mother, father_relationship_rank, mother_relationship_rank, is_in_relationship, relationship, child
        """

        if not user:
            raise ValueError("Users must have an email address")

        user = self.model(
            user=user,
        )

        user.father = father 
        user.mother = mother 
        user.father_relationship_rank = father_relationship_rank
        user.mother_relationship_rank = mother_relationship_rank
        
        user.is_in_relationship = is_in_relationship
        user.relationship = relationship
        user.child = child

        user.save(using=self._db)

        return user


# Create your models here.
class Family(models.Model):
    # user = models.CharField(max_length=255)
    # father = models.CharField(max_length=255, null=True)
    # mother = models.CharField(max_length=255, null=True)

    # one-to-one relationship between a User and a Family
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="family")

    # ForeignKey fields to the User
    # on_delete=models.SET_NULL : User can have a father and mother. Can be nullable (null=True) and optional (blank=True)
    father = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="father")
    mother = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="mother")

    # simple integer
    father_relationship_rank = models.PositiveIntegerField(blank=True, null=True, choices=((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")))
    mother_relationship_rank = models.PositiveIntegerField(blank=True, null=True, choices=((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")))
    
    # simple boolean 
    is_in_relationship = models.BooleanField(default=False)

    # FK to User
    relationship = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="partner")

    # ManyToManyField allows having multiple children who can be part of multiple families
    children = models.ManyToManyField(User, blank=True, related_name="children")

# for now we will just try to implement the thing with only one child
    child = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="child")

    # have to turn it into comment otherwise I can't delete a family
    # def __str__(self):
    #     return self.user

    objects = MyFamilyManager()

# maybe will help to find the family
    USERNAME_FIELD = "user" 