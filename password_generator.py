import random;

lower = "abcdefghijklmnopqrstuvwxz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols="[]{}!@#$%^&*()_-"

all = lower+upper+numbers+symbols
length = 9

print("".join(random.sample(all,length)))