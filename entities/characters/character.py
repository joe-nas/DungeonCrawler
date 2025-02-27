##############################################
# Base Class
##############################################


class Character:
    def __init__(self, name, hitpoints):
        self.name = name
        self.hitpoints = hitpoints
        # self.dexterity = dexterity


##############################################
# Hero
##############################################


class Hero(Character):
    def __init__(
        self, name, hitpoints, weapon=[], armor=[], backpack=[], bank_account=0
    ):
        super().__init__(name, hitpoints)
        self.weapon = weapon
        self.armor = armor
        self.backpack = backpack
        self.bank_account = bank_account

    def showBackpack(self):
        for i, item in enumerate(self.backpack):
            print(f"{i}: {item}")

    def showArmor(self):
        print(self.armor)

    def showWeapon(self):
        print(self.weapon)

    def pickUpItems(self, *items):
        for item in items:
            self.backpack.append(item)
            print(f"You picked up: {item}")

    def sellItems(self, *args):
        for i in args:
            item = self.backpack.pop(i)
            self.bank_account += item.price
            print(f"you sold your {item.name} for {item.price}")

        print(f"your have {self.bank_account} gold in your bank account.")


##############################################
# Enemy
##############################################


##############################################
# NPC
##############################################


class Shopkeeper(Character):

    pass
