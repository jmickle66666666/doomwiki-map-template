from omg import *
import things, sys

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
    output = ""
    for s in mape.sectors:
        if (s.type==9):
            output += "# '''Sector "+str(mape.sectors.index(s))+"'''\n"
    return output
    
def write_statistics():
    output = ""
    output += "== Statistics ==\n\n"
    output += mapdata(mape)
    output += "\n\n===Things===\n\n{| {{prettytable}}"
    #monsters
    if (len(monsters)>0):
        output += "\n!Monsters||[[I'm Too Young To Die|ITYTD]] and [[Hey, Not Too Rough|HNTR]]||[[Hurt Me Plenty|HMP]]||[[Ultra-Violence|UV]] and [[Nightmare!|NM]]"
        for m in monsters:
            if (m.get_total_count() > 0):
                output += "\n|-\n"+m.to_wiki_line()
        output += "\n|-"
    #powerups
    if (len(powerups)>0):
        output += "\n!Powerups||ITYTD and HNTR||HMP||UV and NM"
        for m in powerups:
            if (m.get_total_count() > 0):
                output += "\n|-\n"+m.to_wiki_line()
        output += "\n|-"
    #weapons
    if (len(weapons)>0):
        output += "\n!Weapons||ITYTD and HNTR||HMP||UV and NM"
        for m in weapons:
            if (m.get_total_count() > 0):
                output += "\n|-\n"+m.to_wiki_line()
        output += "\n|-"
    #ammunition
    if (len(ammo)>0):
        output += "\n!Ammunition||ITYTD and HNTR||HMP||UV and NM"
        for m in ammo:
            if (m.get_total_count() > 0):
                output += "\n|-\n"+m.to_wiki_line()
        output += "\n|-"
    #keys
    if (len(keys)>0):
        output += "\n!Keys||ITYTD and HNTR||HMP||UV and NM"
        for m in keys:
            if (m.get_total_count() > 0):
                output += "\n|-\n"+m.to_wiki_line()
        output += "\n|-"
    #other
    if (len(others)>0):
        output += "\n!Other||ITYTD and HNTR||HMP||UV and NM"
        for m in others:
            if (m.get_total_count() > 0):
                output += "\n|-\n"+m.to_wiki_line()
        output += "\n|}"
    return output

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "Usage: dwiki.py wad_path.wad MAPxx (or ExMx)"
        sys.exit()

    wad_path = sys.argv[1]
    map = sys.argv[2]
    output_path = "output.txt"

    wad = WAD(wad_path)

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
        
    
    #main description
    
    text = ""
    
    text += "'''"+map+": MAP NAME''' is the nth map in "+wad_path[wad_path.rfind("/")+1:]+". It was designed by Author, using the track Midi Name by Composer."
    # sections
    text += "\n== Walkthrough ==\n\n===Essential===\n\n===Other points of interest===\n\n===Secrets===\n"
    text += write_secrets()
    text += "\n===Bugs===\n\n== Areas / Screenshots ==\n\n== Speedrunning ==\nThe records for this map on the [http://doomedsda.us Doomed Speed Demos Archive] are:\n\n{| {{prettytable}}\n!Run||Time||Player||Date||File||Notes\n|-\n|[[UV speed]]|| || || ||{{competnftp|**|**}}||\n|-\n|[[NM speed]]|| || || ||{{competnftp|**|**}}||\n|-\n|[[UV max]]|| || || ||{{competnftp|**|**}}||\n|-\n|[[NM100S]]||\n|| || ||{{competnftp|**|**}}||\n|-\n|[[UV -fast]]|| || || ||{{competnftp|**|**}}||\n|-\n|[[UV -respawn]]|| || || ||{{competnftp|**|**}}||\n|-\n|[[UV Tyson]]|| || ||\n||{{competnftp|**|**}}||\n|-\n|[[UV pacifist]]|| || || ||{{competnftp|**|**}}||\n|}\n\n== Deathmatch ==\n\n"
    text += write_statistics()
    text += "\n\n== Technical Information ==\n\n== Inspiration and Development ==\n\n== Trivia ==\n\n== External links ==\n\n*"
    
    
    f = open(output_path,'w')
    f.write(text)
    f.close()

