from django.db import models

# Create your models here.
class LoginManager(models.Model):
    def reg_validator(self,postData):
        errors = {}
        email_filter = User.objects.filter(email = postData["email"])
        if len(postData['first_name']) <2:
            errors['firstnameerror'] = "First Name must be longer than two charcters"
        if len(postData['last_name']) <2:
            errors['lastnameerror'] = "Last Name must be longer than two charcters"
        if len(postData['email_filter'])>0:
            errors['emailused'] = "The email you entered is in use"
        if postData['password'] != postData['repassword']:
            errors['passnomatch'] = "your passwords do not match"


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    repassword = models.CharField(max_length=100)

    def __str__(self):
       return self.first_name + " " + self.last_name+ " "  + self.email + " " + self.password +" "+ self.repassword
# First Name - required; at least 2 characters; letters only
# Last Name - required; at least 2 characters; letters only
# Email - required; valid format
# Password - required; at least 8 characters; matches password confirmation