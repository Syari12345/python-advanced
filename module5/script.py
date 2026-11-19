def greet(emri):
    print(f"Hello {emri}!")

student1='Drini'
students=['Drini','Edlira','Ernesi','Olti',"Syari"]

for student in students:
    greet(student)

print("___________"*3)

def power(nr:int, pow:int)->int:
    return nr**pow

result=power(pow=3,nr=5) #implicite
print(result)

def rectangle_area(a:float,b:float)->float:
    area = a*b #kjo variabel nuk ka scope jasht funksionit
    return round(area,2)

print("Siperfaqja e drejtkendeshit eshte: ",rectangle_area(a=10.0,b=4.5),"njesi katrore")

def circle_area(radius=5.5): #vlera by defaulte parametrit merre vetem ne raste kur nuk i dergojm argument
    global pi #global ka scope edhe jasht funksionit
    pi=3.14
    return pi*(radius**2)

rrethi1=circle_area(10.33)
print("Vlera e konstantes pi eshte: ",pi)
print(rrethi1)



def n(numri1:int, numri2:int)->int:
    return numri1*numri2

rezultati=n(numri1=15,numri2=20)
print("Rezultati eshte: ",rezultati)


