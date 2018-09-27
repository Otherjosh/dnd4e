import os

# Amount of experience required for each level
expTable = {
    1:0,
    2:1000,
    3:2250,
    4:3750,
    5:5500,
    6:7500,
    7:10000,
    8:13000,
    9:16500,
    10:20500,
    11:26000,
    12:32000,
    13:39000,
    14:47000,
    15:57000,
    16:69000,
    17:83000,
    18:99000,
    19:119000,
    20:143000,
    21:175000,
    22:210000,
    23:255000,
    24:310000,
    25:375000,
    26:450000,
    27:550000,
    28:675000,
    29:825000,
    30:1000000
}
# table to track what levels each class gains powers for levelup notifications. Currently doesn't have real data
powerTable = {
    'class':[1,3,4,5,6,8],
    'class2':[2,5,8,29]
}
# table to track race perks
raceTable = {

}
# table to track subrace perks
subraceTable = {

}
totalExp = 0        # this should end up being an element in character creator class
level = 1           # this should end up being an element in character creator class


# TODO  make a class to create character objects and store character data ************ very important **********
class CharCreate(object):
    def __init__(self, name, char_class, exp, strength, con, dex, intel, wis, cha, race, subrace=None):
        self.name = name
        self.race = race
        self.subrace = subrace
        self.charclass = char_class
        self.totalexp = exp
        self.atwills = []
        self.dailies = []
        self.encounters = []
        self.feats = []
        self.level = 1
        self.stats = {
            'strength': strength,
            'con': con,
            'dex': dex,
            'intel': intel,
            'wis': wis,
            'cha': cha
        }
        self.statmods = {
            'strength': int((strength - 10) /2),
            'con': int((con - 10) /2),
            'dex': int((dex - 10) /2),
            'intel': int((intel - 10) /2),
            'wis': int((wis - 10) /2),
            'cha': int((cha - 10) /2)
        }
        self.initiative = int((self.stats[dex] - 10)/2) + int(self.level/2)

        # Defenses
        self.AC = 10 + int(self.level/2)  # will need to be expanded upon for armor/light armor/magic armor
        self.fortitude = 0
        self.reflex = 0
        self.will = 0

        # sets level to correct value with exp entered on creation
        while self.totalexp >= expTable[self.level + 1]:
            self.level += 1
        self.halflevel = int(self.level / 2)

    # will let you choose an atwill at correct level ups, and data for atwills will be stored in spellbook.txt
    def add_atwill(self, atwill):
        self.atwills.append(atwill)

    # will let you choose an encounter power at correct level ups, and data for atwills will be stored in spellbook.txt
    def add_encounter(self, encounter):
        self.encounters.append(encounter)

    # will let you choose a daily power at correct level ups, and data for atwills will be stored in spellbook.txt
    def add_daily(self, daily):
        self.dailies.append(daily)

    # enter exp gained, notify when a new level is reached and notify user of perks for that level.
    # todo take class and powerTable info into account notifys to add powers at correct levels
    def add_exp(self, exp):
        self.totalexp += exp
        if self.totalexp >= expTable[self.level +1]:
            self.level += 1
            print('Congrats! You reached level ' + str(self.level))
            if self.level % 4 == 0:
                print('Select two stats and increase them by one!')
            if self.level % 2 == 0:
                print('Don\'t forget to update your half-levels!')
                print('Gain a feat!')
            elif self.level == 11:
                print('Increase all of your stats by 1!')
                print('Gain a feat!')
                print('Check your feats and powers for improvements!')
                print('Paragon path time, select a paragon path!')
            elif self.level == 21:
                print('Increase all of your stats by 1!')
                print('Gain a feat!')
                print('Check your feats and powers for improvements!')
                print('Epic path time, select an Epic path!')

    # used to update stats of the characters and non-AC defenses
    def update_stats(self, strength, con, dex, intel, wis, cha):
        self.stats = {
            'strength': strength,
            'con': con,
            'dex': dex,
            'intel': intel,
            'wis': wis,
            'cha': cha
        }
        if self.stats['strength'] > self.stats['con']:
            self.fortitude = 10 + int(self.level / 2) + self.statmods['strength']
        elif self.stats['con'] >= self.stats['strength']:
            self.fortitude = 10 + int(self.level / 2) + self.statmods['con']

        if self.stats['dex'] > self.stats['intel']:
            self.reflex = 10 + int(self.level / 2) + self.statmods['dex']
        elif self.stats['intel'] >= self.stats['dex']:
            self.reflex = 10 + int(self.level / 2) + self.statmods['intel']

        if self.stats['wis'] > self.stats['cha']:
            self.will = 10 + int(self.level / 2) + self.statmods['wis']
        elif self.stats['cha'] >= self.stats['wis']:
            self.will = 10 + int(self.level / 2) + self.statmods['cha']


# TODO get character info from user
# TODO Save information to a file
# TODO open a previously saved character
# TODO Track & reset skill usages
# TODO wizards skills are weird af, gotta figure that out
# TODO increase HP, get HP per level based on class/have player enter it when creating character
# TODO Figure out powers for each class per level
# TODO compare class and level with powerTable and prompt for a new power if match
# TODO save selected skills
# TODO provide information on skills (from spellbook.txt ideally)
# TODO Save session notes
# TODO store & save inventory & item effects and manage inventory
# TODO make a menu
# some kind of map interaction maybe? idk what it would do
