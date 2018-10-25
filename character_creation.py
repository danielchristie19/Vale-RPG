import random

class Role():
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "b"

class Inventory():
	def __init__(self):
		self.items = {}

	def add(self, item_name, item_description):
		self.items[item_name] = item_description


class Player():
	def __init__(self, name, role):
		self.name = name
		self.role = Role(role)

	def roll_stats(self):
		if self.role.name == "Voidweaver":
			self.VIT = random.randint(2, 9)
			self.END = random.randint(5, 9)
			self.STR = random.randint(3, 6)
			self.DEX = random.randint(4, 7)
			self.INT = random.randint(5, 11)
			self.MaxHP = 10 + self.VIT
			self.CurrentHP = self.MaxHP
			self.Stamina = self.END + self.STR
			self.Mana = self.END + self.INT

		if self.role.name == "Weaponmaster":
			self.VIT = random.randint(2, 9)
			self.END = random.randint(5, 9)
			self.STR = random.randint(3, 6)
			self.DEX = random.randint(4, 7)
			self.INT = random.randint(5, 11)
			self.MaxHP = 10 + self.VIT
			self.CurrentHP = self.MaxHP
			self.Stamina = self.END + self.STR
			self.Mana = self.END + self.INT

		if self.role.name == "Trickster":
			self.VIT = random.randint(2, 9)
			self.END = random.randint(5, 9)
			self.STR = random.randint(3, 6)
			self.DEX = random.randint(4, 7)
			self.INT = random.randint(5, 11)
			self.MaxHP = 10 + self.VIT
			self.CurrentHP = self.MaxHP
			self.Stamina = self.END + self.STR
			self.Mana = self.END + self.INT

	def equip():
		if self.role.name == "Voidweaver":
			self.inventory = Inventory()


	def __str__(self):
		return "Name: {}\nRole: {}\nHP: {}/{}\nSTR: {}\nDEX: {}\nINT: {}\n".format(self.name, self.role.name, self.CurrentHP, self.MaxHP, self.STR, self.DEX, self.INT)

def choose_role():
	dick = {"1":"Voidweaver",
			"2":"Weaponmaster"
			"3":"Trickster"}
	role = input("Choose a role.\n-Voidweaver\nWeaponmaster\nTrickster\n")
	if role in dick:
		role = dick[role]
	return role

def choose_name():
	return input("Greetings adventurer. What is your name?\n")

#############################################################
player = Player(choose_name() ,choose_role())
player.roll_stats()
print(player)
