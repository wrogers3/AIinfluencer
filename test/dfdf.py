import random
import string

test = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

print(test)