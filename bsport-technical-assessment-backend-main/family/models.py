from django.db import models
from user.models import User

# defines the characteristics of what we want to store
# ORM : Object-Relational Mapping. Python classes get converted into tables directly : persistance is managed by Django

# Create your models here.
class Family(models.Model):
    # user = models.CharField(max_length=255)
    # father = models.CharField(max_length=255, null=True)
    # mother = models.CharField(max_length=255, null=True)

    # one-to-one relationship between a User and a Family
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="family")

    # ForeignKey fields to the User
    # on_delete=models.SET_NULL : User can have a father and mother. Can be nullable (null=True) and optional (blank=True)
    father = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="children_father")
    mother = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="children_mother")

    # simple integer
    father_relationship_rank = models.PositiveIntegerField(blank=True, null=True, choices=((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")))
    mother_relationship_rank = models.PositiveIntegerField(blank=True, null=True, choices=((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")))
    
    # FK to User
    relationship = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="partner")

    def __str__(self):
        return self.user