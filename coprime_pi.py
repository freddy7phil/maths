import random
import math

count = 0

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1
    
for num in range(1,1000000):
    if coprime(random.randrange(1,120), random.randrange(1,120)) is True:
       count+=1

print "Count: %d" % (count)

pi_Approx = float(math.sqrt(6/(float(count) / float(1000000))))

print "pi Approximation: %f" % (pi_Approx)
