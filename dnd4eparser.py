import re


# TODO assign each line to what piece of data it is and then pass those variables to a skill creation class
# maybe count number of lines and have a counter for the iteration to determine which line is which? feels sloppy but
# prolly would work. skill text has 10 lines of info
spellbook = []      # TODO save this skillbook as a file


class skill(object):
    def __init__(self, name, class_, flavor, category, action, weapon, special, target, attack, hit):
        self.name = name
        self.class_ = class_
        self.flavor = flavor
        self.category = category
        self.action = action
        self.weapon = weapon
        self.special = special
        self.target = target
        self.attack = attack
        self.hit = hit


with open('dnd4edump.txt', 'r') as rf:
    counter = 0
    lines = rf.readlines()
    rf.close()
    cleanlines = ['']
    special = False  # track if a skill has a special effect  # TODO do a separate iteration to determine sepcialness
    specialregex = re.compile(r'^Special:')  # to check if any lines are a special effect
    while cleanlines:
        for line in lines:  # could be a method, just removing the newlines
            line_ = line.strip()
            if len(line_) > 0 and len(cleanlines) < 10:
                cleanlines.append(line_)
                if specialregex.search(line):
                    special = True
            # if line == '\n':
            #     lines.remove(line)

        for line in cleanlines:
            if special and len(cleanlines) == 10:
                newskill = skill(*cleanlines)
                spellbook.append(newskill)
                cleanlines = []
                special = False
            if not special and len(cleanlines) == 9:
                print('not special')
                newskill = skill(cleanlines[0],
                                 cleanlines[1],
                                 cleanlines[2],
                                 cleanlines[3],
                                 cleanlines[4],
                                 cleanlines[5],
                                 None,
                                 cleanlines[6],
                                 cleanlines[7],
                                 cleanlines[8],
                                 )
                spellbook.append(newskill)
                cleanlines = []
# this can probably be a separate method

    def spells():
        i = 0
        while i < len(spellbook):      # this can be used to search spellbook for a specific skill by name
            print(
                spellbook[i].name + '\n' +
                spellbook[i].class_ + '\n' +
                spellbook[i].flavor + '\n' +
                spellbook[i].category + '\n' +
                spellbook[i].action + '\n' +
                spellbook[i].weapon + '\n' +
                spellbook[i].special + '\n' +
                spellbook[i].target + '\n' +
                spellbook[i].attack + '\n' +
                spellbook[i].hit
            )
            i += 1

spells()
# TODO support for skills <10 lines long, skills without a special: only have 9 lines
# interate through cleanlines, if  length = 10 (?) pass the list to skill() class and wipe cleanlines
# then continue iterating putting lines into cleanlines until length is reached again
# maybe make a big list of skills that can be searched by the name element of the skills
# making a change for git learning

