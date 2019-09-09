from art import *

i = 1
while i < 100:
    j = 1
    count = 0
    while j <= i:
        if i % j == 0:
            count += 1
        j += 1
    if count == 2:
        print(i)
    i += 1
print("primtal räknades ut!")
tprint("Primtal")
