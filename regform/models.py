from django.db import models

# Create your models here.

class User(models.Model):
  first_name = models.CharField(max_length=150,
                               verbose_name='first_name')
  date_of_birth = models.DateField(verbose_name="Имя участника конференции", name='first_name')
  date_of_birth = models.DateField(verbose_name="Дата рождения", name='dob')
