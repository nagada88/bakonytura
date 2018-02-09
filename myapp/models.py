from django.db import models
from django.http import HttpResponse

class Entry(models.Model):

   content = models.TextField()
   author  = models.CharField(max_length = 50)
   date    = models.CharField(max_length = 50)

   class Meta:
      db_table = "entry"
      