
'''
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def readDataFile():
    first = open("01_Steps.csv", 'rt')
    data = pd.read_csv(first)
    data = data.drop(columns=['date'])
    
    data = data.drop(labels=[129, 130, 131, 132, 133, 134, 135, 136, 159, 160, 161, 162, 163, 164, 274, 275, 
                      276, 277, 278, 279, 280, 297, 298, 370, 371, 926, 928, 1002, 1019, 1061, 1235,
                      1502, 1503, 1505, 1506, 1507, 1789])
    
    second = open("02_Sleep.csv", 'rt')
    data2 = pd.read_csv(second)
    
    data2 = data2.drop(labels=[129, 130, 131, 132, 133, 134, 135, 136, 159, 160, 161, 162, 163, 164, 274, 275, 
                      276, 277, 278, 279, 280, 297, 298, 370, 371, 926, 928, 1002, 1019, 1061, 1235,
                      1502, 1503, 1505, 1506, 1507, 1789])
    
    data2 = data2.drop(columns=['date', 'start', 'stop']).astype(int)
    sleepTimes = data2['deepSleepTime']+data2['shallowSleepTime']+data2['wakeTime']
    data = pd.concat([data, sleepTimes], axis=1)
    
    return data, sleepTimes

data,sleepTimes = readDataFile()

X_train, X_test, y_train, y_test = train_test_split(data.drop('calories', axis=1), data['calories'])

LinReg = LinearRegression(normalize=True)
LinReg.fit(X_train, y_train)

pred = LinReg.predict(X_test)

score = LinReg.score(X_train, y_train)

'''
print("ok")