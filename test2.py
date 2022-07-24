import sqlite3
import joblib  
from datetime import date

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()

test = [0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.0000, 0.00000]
modelload = joblib.load("model.sav")

def calculate_age(born):
    today = date.today()
    if float(today.month) > float(born[5:7]):
        return float(today.year) - float(born[0:4])
    else:
        return float(today.year) - float(born[0:4]) - 1

while(1):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    cur.execute('SELECT * FROM Auth_patient')
    list = cur.fetchall()
    for i in range(len(list)):
        #print((list[i][0]))
        if list[i][7] == 'Male':
            test[0] = 1.0000

        test[1] = (calculate_age((list[i][6])))
        test[2] = float(list[i][17])
        test[3] = float(list[i][16])

        if (list[i][10]) == 'Oui':
            test[4] = 1.0000

        if (list[i][18]) == 'privé':
            test[5] = 2.0000

        if (list[i][18]) == 'gouvernement':
            test[5] = 0.0000

        if (list[i][18]) == 'indépendant':
            test[5] = 3.0000

        if (list[i][18]) == 'Pas encore':
            test[5] = 1.0000

        test[6] = float(list[i][8])

        test[7] = float(list[i][9])

        if (list[i][11]) == 'Inconnu':
            test[8] = 0.0000

        if (list[i][11]) == 'Jamais fumeur':
            test[8] = 2.0000

        if (list[i][11]) == 'Actuellement fumeur':
            test[8] = 3.0000

        if (list[i][11]) == 'ex fumeur':
            test[8] = 1.0000

        #print(modelload.predict([test]))
        if (int(modelload.predict([test]))!=list[i][12]):
            print(test)
            sql = "UPDATE Auth_patient SET stroke=? WHERE username = ?"
            value=(int(modelload.predict([test])),list[i][0])
            cur.execute(sql,value)
            con.commit()
            #print("changed")




