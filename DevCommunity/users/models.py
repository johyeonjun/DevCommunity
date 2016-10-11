from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CoreUser(models.Model):
    
    user_no = models.PositiveIntegerField(primary_key = True, blank=False, null=False, db_column= 'user_no')
    name = models.CharField(max_length=10, blank=False, default='')
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,db_column= 'email')
    password = models.CharField(max_length=128, blank=False, null=False, db_column= 'password')
    profile_img =models.CharField(max_length=100, blank=False, null=False, db_column= 'profile_img')
    job=models.CharField(max_length=10, blank=False, null=False, db_column= 'job')
    gender=models.CharField(max_length=5, blank=False, null=False, db_column= 'gender')
    admin_yn = models.BooleanField(null=False, default = False,  db_column = 'admin_yn')
    login_yn = models.BooleanField(null=False, default = False,  db_column = 'login_yn')
    create_datetime = models.BooleanField(null=False, default = False,  db_column = 'create_datetime')
    last_login_datetime = models.BooleanField(null=False, default = False,  db_column = 'last_login')
    
class Meta:
    managed = True
    db_table = 'CoreUser'
def __unicode__(self):
        return self.nickname