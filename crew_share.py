#LC crew share
import random
print("Yondu Udonta and his crew arrive at the Iron Lotus after several weeks of plundering various places around the galaxy. The crew has been in space for nearly six months and they are ready for a night of celebration. Yondu doesn't want to divvy up the plunder just yet, so he gives each crew member 3 units and sends them off to the Iron Lotus. After the crew has gone, he counts what's left and decides how to split it up among the crew.")
crew_members= int(input("how many crew members are there (this includes Yondu and Peter):"))
units= random.randint(500,5000)
print(f"there are {units} units")
yondu_cut=round(units*0.13, 2)
print(f"Yondu's cut is {yondu_cut}")

peter_cut=round((units-yondu_cut)*0.11, 2)
print(f"Peter's cut is {peter_cut}")

leftovers=units-(yondu_cut + peter_cut)

crew_cut=round(leftovers/crew_members , 2)
print(f"each crew member gets {crew_cut} units")




