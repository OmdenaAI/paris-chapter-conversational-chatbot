
import numpy as np
import pandas as pd
import string
#verify that Csv file is recognized with ';' delimiter or ',' . it may defer from a system to another
data = pd.read_csv('cousnel_dataset_prprocessed.csv',delimiter=',')


questions=data['questionText'].tolist()
answers=data['answerText'].tolist()
print(len(answers), len(questions))
data2=[]
for i in range(len(questions)-1):
    q = '[User] : ' +str(questions[i])
    a=  '[Bot] : '+ str(answers[i])
    data2.append(q)
    data2.append(a)
with open('councel.txt','w') as f:
    for element in data2:
        try:
            f.write(element)
            f.write('\n')
        except:
            pass



