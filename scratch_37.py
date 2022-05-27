#randomised customer reference generator
import random
import string
#create random string for variable v taken as
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_uppercase

    v = input("Enter Customer Name:")
    n = len(v)
    u = v.upper()
    a = ''.join(random.choice(u) for j in range(length))
    result_str = a+v.upper()+''.join(random.choice(u) for i in range(n))
    print("Customer Reference Number is:", result_str)

get_random_string(4)
