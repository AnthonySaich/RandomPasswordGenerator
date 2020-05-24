import random
s = 'abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@£$%^&*()?|'
passwordlen = 16
for i in range(10):
    password = "".join(random.sample(s,passwordlen))
    print (password)
