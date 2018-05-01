from django.db import models
import datetime
import bcrypt


class User(models.Model):
	username = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250)
	email = models.CharField(max_length=250, unique=True)
	password = models.CharField(max_length=150)

	