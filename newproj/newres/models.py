from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Logindata(models.Model):
    emailid=models.EmailField(unique=True)
    password=models.CharField(max_length=100)

    def __str__(self):
            return str(self.emailid)

class Userdata(models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    year_of_study=models.CharField(max_length=100)
    contactno=models.PositiveIntegerField()
    group=models.CharField(max_length=100)

    def __str__(self):
            return str(self.user_id)



class Question(models.Model):
    question = models.CharField(max_length=450,unique=True)
    question_id=models.PositiveIntegerField()
    user_id=models.ForeignKey(Userdata,on_delete=models.CASCADE)
    choice1=models.CharField(max_length=450,null=True)
    choice2=models.CharField(max_length=450,null=True)
    choice3=models.CharField(max_length=450,null=True)
    choice4=models.CharField(max_length=450,null=True)
    selectedchoice=models.CharField(max_length=450,null=True)

    def __str__(self):
        return str(self.question)
