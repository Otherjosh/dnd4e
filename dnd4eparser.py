import re


spellbook = []      # TODO save this skillbook as a file
special = False
specialregex = re.compile(r'^Special:')  # to check if any lines are a special effect
skillinfo = []
debug = False  # Debug toggle, will show additional text to see flow if set to True


# This is just being used as a data structure, doesn't need to be a class/object
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
                if debug:
                    print(lines_[i])
                global special
                special = True
        except IndexError:
            pass
        i += 1


with open('dnd4edump.txt', 'r') as rf:
    lines = striplines(rf.read().splitlines())
    if debug:
        print('with loop')
    rf.close()


while lines:
    if debug:
        print('while loop')
    checkspecial(lines)
    if special:
        if debug:
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
        if debug:
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
        if not debug:
            print('================\n' +
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
        if debug:
            print('================' +
                  'name: ' + spellbook[i].name + '!\n' +
                  'class: ' + spellbook[i].class_ + '!\n' +
                  'flavor: ' + spellbook[i].flavor + '!\n' +
                  'category: ' + spellbook[i].category + '!\n' +
                  'action: ' + spellbook[i].action + '!\n' +
                  'weapon: ' + spellbook[i].weapon + '!\n' +
                  'special: ' + spellbook[i].special + '!\n' +
                  'target: ' + spellbook[i].target + '!\n' +
                  'attack: ' + spellbook[i].attack + '!\n' +
                  'hit: ' + spellbook[i].hit
                  )
        i += 1
    if debug:
        print(lines)

spells()


# This commit doesn't show the Hit line for the final skill, but has correct looking output