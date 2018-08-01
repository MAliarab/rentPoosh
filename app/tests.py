# from django.test import TestCase
import datetime
import hashlib
# from app.models import User

# ppp = "111111"
#
# passw = hashlib.md5()
# passw.update(ppp.encode("utf-8"))
# print(passw.hexdigest())
# # name  = User.objects.filter(password=passw)
#
# # print(name)

i = datetime.datetime.today()
end = i+datetime.timedelta(days=4)

print(end)
print(i)