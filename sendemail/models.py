from django.db import models

#from django.db import models

class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sender_email = models.EmailField()