import numpy as np
import pandas as pd
import string
#verify that Csv file is recognized with ';' delimiter or ',' . it may defer from a system to another
data = pd.read_csv('MentalConversationalData.csv',delimiter=';')
print(data.columns)

def preprocess(chaine):
    q=chaine.replace(']','')
    q=q.replace('[','')
    q=q.replace('"','')
    q=q.split(',')
    return q
liste_q_a=[]

for index, row in data.iterrows():
    q=preprocess(row['patterns'])

    a= preprocess(row['responses'])
 #   print(type(q))
    for qi in q:
        for ai in a:
            liste_q_a.append([qi,ai])


print(len(liste_q_a))


data2=[]
for i in range(len(liste_q_a)-1):
    q = '[User] : ' + liste_q_a[i][0]
    a=  '[Bot] : '+ liste_q_a[i][1]
    data2.append(q)
    data2.append(a)
with open('mentalhealthdialog.txt','w') as f:
    for element in data2:
        try:
            f.write(element)
            f.write('\n')
        except:
            pass


