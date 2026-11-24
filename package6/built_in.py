import os #operating system
import json #javascript object notation
import datetime # ka te beje me daten dhe kohen
import re #regular expression
#paketa te gatshme ne python

print(os.path.isfile('./module2.py'))
for item in os.listdir('./'):
    if os.path.isfile(f'./{item}'):
        print(item)

print(datetime.date.isoweekday(datetime.date.today()))

