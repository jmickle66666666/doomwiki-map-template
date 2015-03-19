from omg import *
import things

wad_path = "C:/Users/Jerry/Downloads/numus/btsx_e1_99i9/btsx_e1.wad"
map = "MAP19"
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
	template = "mapdata|\nthings={0}|\nvertexes={1}|\nlinedefs={2}|\nsidedefs={3}|\nsectors={4}"
	return "===Map data===\n{{"+template.format(len(map.things),len(map.vertexes),len(map.linedefs),len(map.sidedefs),len(map.sectors))+"}}"
	
def write_secrets():
	for s in mape.sectors:
		if (s.type==9):
			f.write("# '''Sector "+str(mape.sectors.index(s))+"'''\n")
	
def write_statistics():
	f.write("== Statistics ==\n\n")
	f.write(mapdata(mape))
	f.write("\n\n===Things===\n\n{| {{prettytable}}")
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
		f.write("\n|}")

mape = mapedit.MapEditor(wad.maps[map])

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
#main description
f.write("'''"+map+": MAP NAME''' is the nth map in "+wad_path[wad_path.rfind("/")+1:]+". It was designed by Author, using the track Midi Name by Composer.")
#sections
f.write("\n== Walkthrough ==\n\n===Essential===\n\n===Other points of interest===\n\n===Secrets===\n")
write_secrets()
f.write("\n===Bugs===\n\n== Areas / Screenshots ==\n\n== Speedrunning ==\nThe records for this map on the [http://doomedsda.us Doomed Speed Demos Archive] are:\n\n{| {{prettytable}}\n!Run||Time||Player||Date||File||Notes\n|-\n|[[UV speed]]|| || || ||{{competnftp|**|**}}||\n|-\n|[[NM speed]]|| || || ||{{competnftp|**|**}}||\n|-\n|[[UV max]]|| || || ||{{competnftp|**|**}}||\n|-\n|[[NM100S]]||\n|| || ||{{competnftp|**|**}}||\n|-\n|[[UV -fast]]|| || || ||{{competnftp|**|**}}||\n|-\n|[[UV -respawn]]|| || || ||{{competnftp|**|**}}||\n|-\n|[[UV Tyson]]|| || ||\n||{{competnftp|**|**}}||\n|-\n|[[UV pacifist]]|| || || ||{{competnftp|**|**}}||\n|}\n\n== Deathmatch ==\n\n")
write_statistics()
f.write("\n\n== Technical Information ==\n\n== Inspiration and Development ==\n\n== Trivia ==\n\n== External links ==\n\n*")
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