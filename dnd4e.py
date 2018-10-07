import os
import pprint

# Amount of experience required for each level
expTable = {
    1: 0,
    2: 1000,
    3: 2250,
    4: 3750,
    5: 5500,
    6: 7500,
    7: 10000,
    8: 13000,
    9: 16500,
    10: 20500,
    11: 26000,
    12: 32000,
    13: 39000,
    14: 47000,
    15: 57000,
    16: 69000,
    17: 83000,
    18: 99000,
    19: 119000,
    20: 143000,
    21: 175000,
    22: 210000,
    23: 255000,
    24: 310000,
    25: 375000,
    26: 450000,
    27: 550000,
    28: 675000,
    29: 825000,
    30: 1000000
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
            'strength': (int(strength) - 10) / 2,
            'con': (int(con) - 10) / 2,
            'dex': (int(dex) - 10) / 2,
            'intel': (int(intel) - 10) / 2,
            'wis': (int(wis) - 10) / 2,
            'cha': (int(cha) - 10) / 2
        }
        self.initiative = (int(self.stats['dex']) - 10) / 2 + (int(self.level) / 2)

        # Defenses
        self.AC = 10 + (int(self.level) / 2)  # will need to be expanded upon for armor/light armor/magic armor
        self.fortitude = 0
        self.reflex = 0
        self.will = 0

        self.inventory = {}  # Dictionary to store inventory items and count

        # sets level to correct value with exp entered on creation
        while self.totalexp >= expTable[self.level + 1]:
            self.level += 1
        self.halflevel = int(self.level / 2)

    # will let you choose an atwill at correct level ups, and data for atwills will be stored in spellbook.txt
    def add_atwill(self, *atwills):
        for atwill in atwills:
            self.atwills.append(atwill)

    # will let you choose an encounter power at correct level ups, and data will be stored in spellbook.txt
    def add_encounter(self, *encounters):
        for encounter in encounters:
            self.encounters.append(encounter)

    # will let you choose a daily power at correct level ups, and data will be stored in spellbook.txt
    def add_daily(self, dailies):
        for daily in dailies:
            self.dailies.append(daily)

    # enter exp gained, notify when a new level is reached and notify user of perks for that level.
    # todo take class and powerTable info into account notifies to add powers at correct levels
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

    def update_stats(self, strength, con, dex, intel, wis, cha):  # TODO run this after leveling up/changing stats
        """
        Used to update stats of character and their non-AC defanses
        :param strength:
        :param con:
        :param dex:
        :param intel:
        :param wis:
        :param cha:
        :return:
        """
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

    def view_inventory(self):
        """
        This prints the inventory so the user can see what they have
        :return:
        """
        length = 0  # this is kind of redundant with using pprint, but could use this to print w/o curly braces
        for k, v in self.inventory:
            if len(k) > length:
                length = len(k)
        pprint.pprint(self.inventory)

    def add_inventory(self, *items):
        """
        Adds a new item and count to inventory
        :param items:
        :return:
        """
        for item in items:
            count = int(input('How many ' + item + ' are you adding?'))
            self.inventory[item] = count
            print(str(count) + ' ' + item + ' have been added to your inventory')

    # Inventory functions, TODO item effects
    def modify_inventory(self, item_='', reduction=0):
        """
        Lowers or increases the amount of an item in inventory
        :param item_:
        :param reduction:
        :return:
        """
        if not item_:
            item_ = input("What item would you like to modify?")
        if not reduction:
            reduction = input("How many would you like to add/remove from inventory?")
        if item_ in self.inventory:
            if reduction == self.inventory:
                remove_inventory(item_)
            else:
                self.inventory[item_] -= int(reduction)
        elif item_ not in self.inventory:
            print(item_ + ' not found in inventory')

    def remove_inventory(self, item_=''):
        """
        Removes an item from the inventory list
        :param item_:
        :return:
        """
        if not item_:
            item_ = input("What item would you like to remove?")
        if item_ in self.inventory:
            del self.inventory[item_]
        else:
            print("Item not found in inventory")


def add_character():
    """
    Gets information for a character from the user
    :return:
    """
    name = ''
    char_class = ''
    exp = 0
    strength = 0
    con = 0
    dex = 0
    intel = 0
    wis = 0
    cha = 0
    race = ''
    subrace = ''
    nosub = False
    if not name:
        name = input("Character name: ")
    if not char_class:
        char_class = input("Character class: ")
    if not exp:
        exp = int(input("Current experience: "))
    if not strength:
        strength = str(input("Character strength: "))
    if not con:
        con = str(input("Character constitution: "))
    if not dex:
        dex = str(input("Character dexterity: "))
    if not intel:
        intel = str(input("Character intellect: "))
    if not wis:
        wis = str(input("Character wisdom: "))
    if not cha:
        cha = str(input("Character charisma: "))
    if not race:
        race = input("Character race: ")
    if not subrace:
        subrace = input("Character subrace (none if not applicable): ")
    if subrace == 'none':
        subrace = None
        nosub = True
    if name and char_class and exp and strength and con and dex and intel and wis and cha and race:
        if subrace or nosub:
            global character
            character = CharCreate(name, char_class, exp, strength, con, dex, intel, wis, cha, race, subrace)


def menu():
    choice = ''
    while choice != 'exit':
        choice = input("Welcome to dnd4e.py! \n"
                       "What would you like to do?\n"
                       "Please make a selection or exit\n"
                       "1. Add a character\n"
                       "2. View character information\n"
                       "3. Modify a character\n"
                       )
        if choice == '1':
            add_character()
        elif choice == '2':
            print(character.stats)
        elif choice == '3':
            print("you modify a character here")
        elif choice == 'exit':
            break
        else:
            print("Invalid selection")
# TODO save selected skills
# TODO provide information on skills (from spellbook.txt ideally)
# TODO Save session notes
# TODO make a menu

# medium term goals
# TODO Save information to a file
# TODO open a previously saved character


# long term goals
# TODO GUI??
# TODO compare class and level with powerTable and prompt for a new power if match
# TODO Figure out powers for each class per level
# TODO increase HP, get HP per level based on class/have player enter it when creating character
# TODO Track & reset skill usages

# some kind of map interaction maybe? idk what it would do
menu()