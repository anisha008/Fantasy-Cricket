import sqlite3
fancr=sqlite3.connect("FantasyCricket.db")
curcricket=fancr.cursor()
curcricket.execute("""CREATE table Match (
Player TEXT,
Scored INTEGER,
Faced INTEGER,
Fours INTEGER,
Sixes INTEGER,
Bowled INTEGER,
Maiden INTEGER,
Given INTEGER,
Wkts INTEGER,
Catches INTEGER,
Stumping INTEGER,
RunOut INTEGER)""")
curcricket.execute("""CREATE table Stats(
Player TEXT,
Matches INTEGER,
Runs INTEGER,
[100s] INTEGER,
[50s] INTEGER,
Value INTEGER,
Ctg TEXT)""")
curcricket.execute("""CREATE table Teams(
Name TEXT,
Players TEXT,
Value INTEGER)""")

sql="select * from Match"
curcricket.execute(sql)
cr=curcricket.fetchall()
if(cr):
    for x in cr:
        print (x)
        
z=input("Add more Players?(Y/N):")
while(z=='y' or z=='Y'):
    row=[input("Player:")]
    row.append(int(input("Give Score:")))
    row.append(int(input("Give Faced:")))
    row.append(int(input("Give foures:")))
    row.append(int(input("Give Sixes:")))
    row.append(int(input("Give Bowled:")))
    row.append(int(input("Give Maiden:")))
    row.append(int(input("Give Given:")))
    row.append(int(input("Give Wkts:")))
    row.append(int(input("Give Catches:")))
    row.append(int(input("Give Stumping:")))
    row.append(int(input("Give RunOut:")))

    try:
        curcricket.execute("INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wkts,Catches,Stumping,RunOut)VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
        fancr.commit()
        print("Records added successfully in Matchg table")
    except:
        print("Error in Operation")
        fancr.rollback()

    print("Player info for Stats")
    row.append(int(input("Total Matches played")))
    row.append(int(input("Give Runs:")))
    row.append(int(input("Give 100s:")))
    row.append(int(input("Give 50s:")))
    row.append(int(input("Give Value:")))
    row.append(input("Give category as BAT,BOW,AR,WK:"))

    try:
        curcricket.execute("INSERT INTO Stats(Player,Matches,Runs,[100s],[50s],Value,Ctg)VALUES(?,?,?,?,?,?,?)",(row[0],row[12],row[13],row[14],row[15],row[16],row[17]))
        fancr.commit()
        print("Record added successfully in Stats Table")
    except:
        print("Error in Operation")
        fancr.rollback()
    z=input("Add more Players info?(Y/N):")
print("Bye Bye")
fancr.close()



