import re


# TODO assign each line to what piece of data it is and then pass those variables to a skill creation class
# maybe count number of lines and have a counter for the iteration to determine which line is which? feels sloppy but
# prolly would work. skill text has 10 lines of info
spellbook = []      # TODO save this skillbook as a file

special = False
specialregex = re.compile(r'^Special:')  # to check if any lines are a special effect
skillinfo = []


class Skill(object):
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


# removes empty lines
def striplines(lines_):
    for line in lines_:
        if len(line) == 0:
            lines_.remove(line)
    return lines_


def checkspecial(lines_):
    i = 0
    while i < 9:
        try:
            if re.match(specialregex, lines_[i]):
                print(lines_[i])
                global special
                special = True
        except IndexError:
            pass
        i += 1


with open('dnd4edump.txt', 'r') as rf:
    lines = striplines(rf.read().splitlines())
    print('with loop')
    rf.close()


while lines:
    print('while loop')
    checkspecial(lines)
    if special:
        print('special = True')
        while len(skillinfo) < 10:
            skillinfo.append(lines.pop(0))
            if len(skillinfo) == 10:
                newskill = Skill(*skillinfo)
                spellbook.append(newskill)
                special = False
        skillinfo = []
        continue

    if not special:
        print('not special')
        while len(skillinfo) < 9:
            try:
                line_ = lines.pop(0)
            except IndexError:
                break
            skillinfo.append(line_)
            if len(skillinfo) == 9:
                newskill = Skill(skillinfo[0],
                                 skillinfo[1],
                                 skillinfo[2],
                                 skillinfo[3],
                                 skillinfo[4],
                                 skillinfo[5],
                                 'No special effects',
                                 skillinfo[6],
                                 skillinfo[7],
                                 skillinfo[8],)
                spellbook.append(newskill)
                special = False
        skillinfo = []
        continue


def spells():
    i = 0
    while i < len(spellbook):      # this can be used to search spellbook for a specific skill by name
        print('================' +
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

