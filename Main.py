import random

Variable =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
C1 = int(input("De cuantos caracteres quiere su contraseña?"))
Password = ""

for i in range(C1):
    Password += random.choice(Variable)

print(Password)
