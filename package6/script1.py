from emoji import emojize,LANGUAGES
import pandas
print(emojize('Python is :thumbs up: , :snake: , :red_heart:',variant="emoji_type",language='en'))
print(emojize(':pulgar_hacia_arriba:',languages='es'))

df=pandas.DataFrame({"name":['Ernes','Edlira','Rini','Olti'],'age':[17,15,16,18],'gender':['M',"F","M",pandas.NA]})

print(df["name"][2])

