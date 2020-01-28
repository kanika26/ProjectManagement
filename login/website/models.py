from django.db import models

# Create your models here.
class userlogin(models.Model):
    id = models.AutoField(primary_key=True)
    empid = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    is_usertype = models.CharField(max_length=20)
    #is_employee = models.BooleanField(default=False)

    class Meta:
        db_table = "login"

    def __str__(self):
        return self.username

class project(models.Model):
    Pid = models.AutoField(primary_key=True)
    Pname = models.CharField(max_length=500)
    Pdescription = models.CharField(max_length=3000)
    Cname = models.CharField(max_length=300)
    Cdetails = models.CharField(max_length=4000)
    Pdeadline = models.DateField()
    Pstartdate = models.DateField()
    Pmanagedby = models.CharField(max_length=400)
    Pcontract = models.CharField(max_length=2000)
    Ptextresource = models.CharField(max_length=6000)
    Pstatus = models.IntegerField()

    class Meta:
        db_table = "project"

    def __str__(self):
        return str(self.Pname)


class task(models.Model):
    Tid = models.AutoField(primary_key=True)

    Ttitle = models.CharField(max_length=3000)
    Pid = models.IntegerField()
    Tstatus = models.IntegerField()

    Tttechnology = (
        ('JAVA', 'JAVA'),
        ('PYTHON', 'PYTHON'),
        ('MATLAB', 'MATLAB'),
        ('JULIA', 'JULIA'),
        ('R', 'R')
    )
    Ttechnology = models.CharField(max_length=100, choices=Tttechnology)
    Tassignedto = models.IntegerField()
    Tassignedby = models.CharField(max_length=600)
    Tassigneddate = models.DateField()
    Tdeadline = models.DateField()

    class Meta:
        db_table = "task"

    def __str__(self):
        return str(self.Pid) + "    " + self.Ttitle



class message(models.Model):
    Mid = models.AutoField(primary_key=True)
    sender_username = models.CharField(max_length=3000)
    receiver_username = models.CharField(max_length=3000)
    content = models.CharField(max_length=45000)

    class Meta:
        db_table = "message"

    def __str__(self):
        return str(self.Mid)





