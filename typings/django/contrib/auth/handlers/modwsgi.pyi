from _typeshed import Incomplete
from django import db as db
from django.contrib import auth as auth

UserModel: Incomplete

def check_password(environ, username, password): ...
def groups_for_user(environ, username): ...
