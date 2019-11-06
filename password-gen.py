import random
import string
import sys


default_value = 20
help = False

def randomStringDigits(stringLength=default_value):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

try:
    arg = sys.argv[-1]
    if arg in ["--help","-h"]:
        help =True
    else:
        n=int(arg)

except ValueError:
    n= default_value

if help:
    print("------password-generator----------")
    print("* password-gen n generate a random password with a length n")
    print("* the default value is n=20")
else:
    print(randomStringDigits(n))
