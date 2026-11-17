for nr in range(100):
    print(nr)
#numeron 0...99

print("------------"*4)
for i in range(1,11):
    print(i) #numeron prej nr te pare deri tek i dyti-1


print("------------"*4) #beje ne total 4 "------------"
for step in range(0,15,3):
    print(step) #numeron prej nr te pare deri tek i dyti -1 por kalon per aq sa e keni stepin
    #0, 5, 10



    seasons=["Spring", "Summer", "Autumn", "Winter",
             "Spring", "Summer", "Autumn", "Winter",
             "Spring","Summer","Autumn","Winter", ]

for season in seasons:
print(season) #iteration over list

print("------------"*)
for i in range(0,len(seasons),5):
      print(seasons[i])


print("------------"*4)
word="computer works for us!"
words=word.split(" ")
for c in words:
    #if c.isalpha(): #isalpha printon vetem shkronja pa hapsir ose !.
        print(c)



logs=["Execute1","Execute2","Execute3","Error","Execute4","Execute5","Execute6"]
for log in logs:
    if log=="Error":
       #break   e thyen ciklin
    continue #vazhdo ciklin duke injoruar kete hap
else:
    print(log)




