import sqlite3
fancr=sqlite3.connect("FantasyCricket.db")
curcricket=fancr.cursor()
curcricket.execute("SELECT * FROM Match")
x=curcricket.fetchall()
def pointscalculation(x):
    points=0.0
    Scored=x[1]
    try:
        StrikeRate = float(x[1])/float(x[2])
    except:
        StrikeRate = 0
    Fours =float(x[3])
    Sixes=float(x[4])
    twos=int((Scored-4*Fours - 6*Sixes)/2)
    Wickets=10*(float(x[8]))
                
    try:
        EconomyRate=float(x[7])/(float(x[5])/6)
    except:
        EconomyRate=0
    Fielding=float(x[9])+float(x[10])+float(x[11])
    points +=(Fours + 2*Sixes + 10* Fielding +twos +Wickets)
    if Scored > 100:
        points+=10
    elif Scored >= 50:
        points+=5
    if StrikeRate >1:
        points+=4
    elif StrikeRate >=0.8:
        points +=2
    if Wickets >5:
        points+=10
    elif Wickets >3:
        points+=5
    if EconomyRate >=3.5 and EconomyRate<=4.5:
        points+=4
    elif EconomyRate>=2 and EconomyRate <3.5:
        points +=7
    elif EconomyRate<2:
        points+=10
    return points
PlayerPoints={}
for i in x:
    PlayerPoints[i[0]]=pointscalculation(i)
print(PlayerPoints)
                           
