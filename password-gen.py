import random
import string
import sys


default_value = 20

def randomStringDigits(stringLength=default_value):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

try:
    n=int(sys.argv[-1])

except ValueError:
    n= default_value

print(randomStringDigits(n))
