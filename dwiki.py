from omg import *
import things

wad_path = "C:/Users/Jerry/Downloads/zdoom-2.7.1/DOOM2.WAD"
map = "MAP01"
output_path = "C:/Users/Jerry/Documents/junk/mapdata.txt"

wad = WAD(wad_path)

def get_thing_count(map,thing_id):
	count = [0,0,0]
	for t in map.things:
		if (t.type == thing_id):
			if (t.multiplayer == False):
				if (t.easy == True):
					count[0]+=1
				if (t.medium == True):
					count[1]+=1
				if (t.hard == True):
					count[2]+=1
	return count

def mapdata(map):
	template = "===Map data===\n{{mapdata|\nthings={0}|\nvertexes={1}|\nlinedefs{2}|\nsidedefs{3}|\nsectors{4}}}"
	return template.format(len(map.things),len(map.vertexes),len(map.linedefs),len(map.sidedefs),len(map.sectors))
	
mape = mapedit.MapEditor(wad.maps["MAP01"])

monsters = []
for i in things.monsters:
	if (get_thing_count(mape,i) > 0):
		monsters.append(things.Thing(i,get_thing_count(mape,i)))
	
powerups = []
for i in things.powerups:
	if (get_thing_count(mape,i) > 0):
		powerups.append(things.Thing(i,get_thing_count(mape,i)))
	
weapons = []
for i in things.weapons:
	if (get_thing_count(mape,i) > 0):
		weapons.append(things.Thing(i,get_thing_count(mape,i)))
	
ammo = []
for i in things.ammo:
	if (get_thing_count(mape,i) > 0):
		ammo.append(things.Thing(i,get_thing_count(mape,i)))
	
keys = []
for i in things.keys:
	if (get_thing_count(mape,i) > 0):
		keys.append(things.Thing(i,get_thing_count(mape,i)))
	
others = []
for i in things.others:
	if (get_thing_count(mape,i) > 0):
		others.append(things.Thing(i,get_thing_count(mape,i)))
	
f = open(output_path,'w')
f.write("== Statistics ==\n")
f.write(mapdata(mape))
f.write("\n\n===Things===\n{| {{prettytable}}")
#monsters
if (len(monsters)>0):
	f.write("\n!Monsters||[[I'm Too Young To Die|ITYTD]] and [[Hey, Not Too Rough|HNTR]]||[[Hurt Me Plenty|HMP]]||[[Ultra-Violence|UV]] and [[Nightmare!|NM]]")
	for m in monsters:
		if (m.get_total_count() > 0):
			f.write("\n|-\n"+m.to_wiki_line())
	f.write("\n|-")
#powerups
if (len(powerups)>0):
	f.write("\n!Powerups||ITYTD and HNTR||HMP||UV and NM")
	for m in powerups:
		if (m.get_total_count() > 0):
			f.write("\n|-\n"+m.to_wiki_line())
	f.write("\n|-")
#weapons
if (len(weapons)>0):
	f.write("\n!Weapons||ITYTD and HNTR||HMP||UV and NM")
	for m in weapons:
		if (m.get_total_count() > 0):
			f.write("\n|-\n"+m.to_wiki_line())
	f.write("\n|-")
#ammunition
if (len(ammo)>0):
	f.write("\n!Ammunition||ITYTD and HNTR||HMP||UV and NM")
	for m in ammo:
		if (m.get_total_count() > 0):
			f.write("\n|-\n"+m.to_wiki_line())
	f.write("\n|-")
#keys
if (len(keys)>0):
	f.write("\n!Keys||ITYTD and HNTR||HMP||UV and NM")
	for m in keys:
		if (m.get_total_count() > 0):
			f.write("\n|-\n"+m.to_wiki_line())
	f.write("\n|-")
#other
if (len(others)>0):
	f.write("\n!Other||ITYTD and HNTR||HMP||UV and NM")
	for m in others:
		if (m.get_total_count() > 0):
			f.write("\n|-\n"+m.to_wiki_line())
	f.write("\n|-")
f.close()
#template

# == Statistics ==
# ===Map data===
# {{mapdata|
  # things=69|
  # vertexes=383|
  # linedefs=370|
  # sidedefs=529|
  # sectors=59|
  # vertexbefore=316}}

# ===Things===
# {| {{prettytable}}
# !Monsters||[[I'm Too Young To Die|ITYTD]] and [[Hey, Not Too Rough|HNTR]]||[[Hurt Me Plenty|HMP]]||[[Ultra-Violence|UV]] and [[Nightmare!|NM]]
# |-
# ||[[Imp]]s||1||7||17
# |-
# ||[[Trooper]]s||8||12||10
# |-
# !Powerups||ITYTD and HNTR||HMP||UV and NM
# |-
# ||[[Stimpack]]s||5||5||5
# |-
# ||[[Medikit]]s||3||3||3
# |-
# ||[[Health bonus]]es||8||8||8
# |-
# ||[[Armor bonus]]es||1||1||1
# |-
# ||[[Green armor]]s||1||1||1
# |-
# !Weapons||ITYTD and HNTR||HMP||UV and NM
# |-
# ||[[Shotgun]]s||1||1||1
# |-
# ||[[Rocket launcher]]s||1||1||1
# |-
# ||[[Chainsaw]]s||1||1||1
# |-
# !Ammunition||ITYTD and HNTR||HMP||UV and NM
# |-
# ||[[Clip]]s||2||2||2
# |-
# ||[[Shell]]s||1||1||1
# |}