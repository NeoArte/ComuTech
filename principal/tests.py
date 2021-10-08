from django.test import TestCase
from datetime import time, timedelta, date

# Create your tests here.
print(date.today() < date.today() + timedelta(days=5))
