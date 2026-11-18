temperature=45 #variable
name='Drin'
unit='F'

#Data Structures
students=['studenti1','studenti3','studenti3',6,0.676] #list

t1=(3,3,5,7,4) # e pandryshueshme
s1={3,3,5,7,3,3,4} #set - elemente unike
d1={'Edlira':False,'Rini':17,'Lirak':23} #dict -> key_values pairs
print(d1['Rini'])
print(type(d1['Edlira']))
print("-----"*5)

students.append(True)
for student in students:
    print(student)
print(students.index(2))

for key,value in d1.items():
    print(f"{key} - {value}")