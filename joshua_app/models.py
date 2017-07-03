from __future__ import unicode_literals

from django.db import models

class Resume_Item(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    sur_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now=False)
    telephone = models.IntegerField()
    email = models.CharField(max_length=100)
    address = models.TextField()
    work_history = models.TextField()


    def __unicode__(self):
        return self.first_name
