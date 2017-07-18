from django.test import TestCase
import time
import random
from datetime import datetime

# Create your tests here.

string = time.strftime("%H%M%S") + str(random.randint(1000, 9999))
print string


