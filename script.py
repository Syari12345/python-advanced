from typing import Dict,List

pcs:Dict[int,'str'|List[str]]={3:'Lenovo',
                               4:'HP',
                               5:['msi','Dell999*    _']
                               }

for key,value in pcs.items():
    if type(value)==list:
        for brand in value:
            print(f"Per pc nr,{key}, eshte brendi: {brand}")
        else:
            print(f"Per pc nr.{key}, eshte brendi: {value}")


example='PythonListMethodsExplained'
example=example.lower()
count:{str,int}={}
for char in example:
    if char not in count.keys():
        count[char]=1
    else:
        count[char]+=1

#--------------
qytetet:List[str|int]=['Prishtina','New York',"Prizreni","Tirana","Shkupi"]
print(qytetet.index('Prizreni'))
for i in range(5):
    qytetet.append(f"Elementi nr,{i}")
print(qytetet.count("Elementi nr.3"))
qytetet.insert(1,5)
print(qytetet)