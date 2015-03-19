from omg import *
import things

wad_path = "C:/Users/Jerry/Downloads/zdoom-2.7.1/DOOM2.WAD"
map = "MAP01"

wad = WAD(wad_path)

def get_thing_info(map,thing_id):
	

def thing_line(thing_id,itytd,hmp,uv):
	thing = things.get(thing_id)
	link=""
	thingname = thing[1]
	thingplural = thing[2]
	thinglink = thing[3]
	if (thinglink == thingname):
		link = "[["+thingname+"]]"
	else:
		link = "[["+thinglink+"|"+thingname+"]]"
	
	name = ""
	if (thingname in thingplural):
		name = thingplural
		name.replace(thingname,link)
		link = name
	return "||"+link+"||"+str(itytd)+"||"+str(hmp)+"||"+str(uv)

def mapdata(map):
	template = "===Map data===\n{{mapdata|\nthings={0}|\nvertexes={1}|\nlinedefs{2}|\nsidedefs{3}|\nsectors{4}}}"
	return template.format(len(map.things),len(map.vertexes),len(map.linedefs),len(map.sidedefs),len(map.sectors))
	
mape = mapedit.MapEditor(wad.maps["MAP01"])
	
f = open('mapdata.txt','w')
f.write("== Statistics ==\n")
f.write(mapdata(mape))
f.write("\n\n===Things===")
#monsters

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