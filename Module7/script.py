nr=int("41")
print(type(nr))

print(str(False))
print(bool(21))

#z=int('a3gaf5sh7') nuk funksionon
print(type(float('52.5')))

name=input("Enter your name:\n")
age=int(input(f"Please enter your age MR./Ms. {name}:\n"))
print(age)

try:
    print(50/0)
except ZeroDivisionError as e:
    print('Ka ndodhur nje gabim gjate ekzekutimit')



try:
    with open('./xyx2135.py') as o:
        result=o.readlines()
        print(result)
except FileNotFoundError as e:
    print('File nuk u gjet!')
finally:
    o.close()