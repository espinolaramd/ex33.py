#Diego Espinola
#13.10.19
#While Loops

i=0
numbers=[]

while i<6:
    print(f"A the top i is {i}")
    numbers.append(i)

    i= i+1
    print("Numbers now: ", numbers)
    print(f"At tge bottom i is {i}")
print("The numbers: ")

for num in numbers:
    print(num)
