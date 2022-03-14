#!/usr/bin/python3
"""test"""
from models import *
from models.user import User

# creation of a User
user = User(first_name="almendra", last_name="tostada", password="hola1234", whatsapp=123456789)
user.save()

storage.save()
print("OK")
