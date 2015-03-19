#template (thing_id,name,plural,link)
#example (3001,"Imp","Imps","Imp")

list = []
allthings = []

class Thing(object):
	def __init__(self,thing_id,count):
		self.thing_id = thing_id
		self.itytd_count = count[0]
		self.hmp_count = count[1]
		self.uv_count = count[2]
		
	def get_total_count(self):
		return self.itytd_count + self.hmp_count + self.uv_count
	
	def to_wiki_line(self):
		if (self.get_total_count() == 0): return ""
		thing = get(self.thing_id)
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
			name = name.replace(thingname,link)
			link = name
		return "||"+link+"||"+str(self.itytd_count)+"||"+str(self.hmp_count)+"||"+str(self.uv_count)
		
def add(thing_id,name,plural="",link=""):
	if (plural == ""):
		plural = name+"s"
	if (link == ""):
		link = name
	list.append((thing_id,name,plural,link))

def get(thing_id):
	for i in list:
		if (i[0] == thing_id): return i

#powerups
add(2023,"Berserk")
add(2026,"Computer Map")
add(2014,"Health Bonus","Health Bonuses")
add(2024,"Invisibility","Invisibilities","Partial Invisibility")
add(2022,"Invulnerability","Invulnerabilities")
add(2045,"Light Amplification Visor")
add(83,"Megasphere")
add(2013,"Soul Sphere")
add(2015,"Armor Bonus","Armor Bonuses")
add(2019,"Blue Armor")
add(2018,"Green Armor")
add(2012,"Medikit")
add(2025,"Radiation Suit")
add(2011,"Stimpack")
powerups=(2023,2026,2014,2024,2022,2045,83,2013,2015,2019,2018,2012,2025,2011)
#weapons
add(2006,"BFG 9000")
add(2002,"Chaingun")
add(2005,"Chainsaw")
add(2004,"Plasma Gun")
add(2003,"Rocket Launcher")
add(2001,"Shotgun")
add(82,"Super Shotgun")
weapons=(2006,2002,2005,2004,2003,2001,82)
#ammunition
add(2007,"Ammo Clip")
add(2048,"Box of Ammo","Boxes of Ammo")
add(2046,"Box of Rockets","Boxes of Rockets")
add(2049,"Box of Shells","Boxes of Shells")
add(2047,"Energy Cell","","Energy Cell (Doom)")
add(17,"Energy Cell Pack")
add(2010,"Rocket")
add(2008,"Shotgun shells","Shotgun shells")
add(8,"Backpack")
ammo=(2007,2048,2046,2049,2047,17,2010,2008,8)
#keys
add(5,"Blue Keycard")
add(40,"Blue Skull Key")
add(13,"Red Keycard")
add(38,"Red Skull Key")
add(6,"Yellow Keycard")
add(39,"Yellow Skull Key")
keys=(5,40,13,38,6,39)
#monsters
add(68,"Arachnotron")
add(64,"Arch-Vile")
add(3003,"Baron of Hell")
add(3005,"Cacodemon")
add(65,"Heavy Weapon Dude")
add(72,"Commander Keen")
add(16,"Cyberdemon")
add(3002,"Demon")
add(3004,"Zombieman","Zombiemen")
add(9,"Shotgun Guy")
add(69,"Hell Knight")
add(3001,"Imp")
add(3006,"Lost Soul")
add(67,"Mancubus","Mancubi")
add(71,"Pain Elemental")
add(66,"Revenant")
add(58,"Spectre")
add(7,"Spiderdemon")
add(84,"Wolfenstein SS")
monsters=(68,64,3003,3005,65,72,16,3002,3004,9,69,3001,67,71,66,58,7,84)
#other
add(2035,"Barrel")
others=[2035]
















