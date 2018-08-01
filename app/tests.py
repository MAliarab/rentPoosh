# from django.test import TestCase

# Create your tests here.
from passlib.handlers.pbkdf2 import pbkdf2_sha1

passw = "m2fan6320"
enc = pbkdf2_sha1.__hash__(passw)
print(enc)

enc2 = pbkdf2_sha1.__hash__(passw)

print(enc == passw)