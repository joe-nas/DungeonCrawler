##############################################
# Base Class
##############################################


class Item:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price


##############################################
# Armor
##############################################


class Armor(Item):
    def __init__(self, name, size, price, armor_value):
        super().__init__(name, size, price)
        self.armor_value = armor_value

    def __str__(self):
        return f"A {self.size} {self.name}, worth {self.price} gold. Prevents {self.armor_value} damage."


##############################################
# Weapon
##############################################


class Weapon(Item):
    def __init__(self, name, size, price, attack_value):
        super().__init__(name, size, price)
        self.attack_value = attack_value

    def __str__(self):
        return f"A {self.size} {self.name}, worth {self.price} gold. Causes {self.attack_value} damage."


##############################################
# Potion
##############################################


class Potion(Item):
    def __init__(self, name, size, stat, price=1, value=0, duration=0):
        super().__init__(name, size, price)
        self.stat = stat
        self.value = value
        self.duration = duration

    def __str__(self):
        description = f"A {self.name} potion, that increases your {self.stat} by {self.value} for {self.duration} rooms. Can be sold for {self.price} gold"
        match self.stat:
            case "armor":
                return description
            case "attack":
                return description
            case "health":
                return f"A {self.name} potion. Restores {self.value} {self.stat}. Can be sold for {self.price} gold"


healthpotion = Potion("health", "laegr", "armor", 1, 1, 1)
print(healthpotion)
