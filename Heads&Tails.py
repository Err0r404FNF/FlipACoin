#Heads&Tails
import random
import time

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

n = random.randint(0,1)
if n==0:
    print("Heads")
    time.sleep(10)

if n==1:
    print("Tails")
    time.sleep(10)

a=input("Press the Space key to close or wait 10 seconds. Program made by Vancouver_ (Err0r404FNF) On GitHub.")

if a==" ":
    exit()