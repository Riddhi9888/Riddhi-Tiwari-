# han
print("*"*60)
temp="ONE DAY IN MY PARENTES LIFE"
print(temp)
print("*"*60)

input("enter your parent name:")
input("enter your occupation:")
input("enter your Relation:")
bool(input("works on weekend?"))

print("="*60)
print("*"*60)

officework=float(input("enter your office work:"))
travillinghours=float(input("enter your travilling hours:"))
householdingworkhours=float(input("enter your house holding hours:"))
Excersicehours=float(input("enter your Excersice hours:"))
sleepinghours=float(input("enter your sleeping hours:"))

print("="*60)
print("*"*60)

Totalwork=officework+travillinghours+householdingworkhours
print("Total work:",Totalwork)

totaloccupiedhours=officework+travillinghours+householdingworkhours+Excersicehours+sleepinghours
print("total occupied hours:", totaloccupiedhours)

Freetime=24-Totalwork
print("Free time:",Freetime)

Dayutilisedtime=(Totalwork/24)*100
print("Day utilised time:",Dayutilisedtime)

print("*"*60)
