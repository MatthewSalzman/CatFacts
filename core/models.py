from django.db import models

# Create your models here.

class Fact(models.Model):
    fact = models.CharField(max_length=1000)
    used = models.BooleanField(default=False)
    def __str__(self):
        return self.fact




#Email stuff
class Header(models.Model):
    header = models.CharField(max_length=300)
    def __str__(self):
        return self.header


class Footer(models.Model):
    footer = models.CharField(max_length=300)

    def __str__(self):
        return self.footer


class Email(models.Model):
    first_name = models.CharField(blank=True, max_length=40)
    email_address = models.CharField(max_length=40)
    def __str__(self):
        return self.email_address