from django.db import models




# Create your models here.
class SendMail(models.Model):
    receiver = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    namereceiver = models.CharField(max_length=200)

    def __str__(self):
        return self.receiver
