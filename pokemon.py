class Pokemon:
	def __init__(self, name, level, element, max_health, current_health, is_knocked_out):
		self.name = name
		self.level = level
		self.element = element
		self.max_health = max_health
		self.current_health = current_health
		self.is_knocked_out = is_knocked_out

	def advantage(self, poke):
		if self.element == 'fire' and poke.element == 'grass':
			return True
		elif self.element == 'water' and poke.element == 'fire':
			return True
		elif self.element == 'grass' and poke.element == 'water':
			return True

	def disadvantage(self, poke):
		if self.element == 'fire' and poke.element == 'water':
			return True
		elif self.element == 'water' and poke.element == 'grass':
			return True
		elif self.element == 'grass' and poke.element == 'fire':
			return True

	def dead(self):
		if self.current_health <= 0:
			self.is_knocked_out = True
	
	def alive(self):
		if self.current_health == 0:
			self.is_knocked_out = False
			print(f"{self.name} is revived!")

	def lose_health(self, amount):
		self.current_health -= amount
		self.dead()
		string = f"{self.name} took {amount} damage!" if self.current_health > 0 else f"{self.name} took {amount} damage and fainted!"
		print(string) 
		
	def regain_health(self, amount):
		self.alive()
		self.current_health += amount
		print(f"{self.name} has gained {amount} HP!")

	def attack(self, poke):
		print(f"{self.name} attacked!")
		if self.advantage(poke):
			print('Attach was super effective!')
			poke.lose_health(self.level * 2)
		elif self.disadvantage(poke):
			print('Attach was not that effective...')
			poke.lose_health(self.level // 2)
		else:
			poke.lose_health(self.level)

	def __repr__(self):
		return f'{self.name}'

class Trainer:
	def __init__(self, name, pokemon, num_of_potions, currently_active):
		self.name = name
		self.pokemon = pokemon
		self.num_of_potions = num_of_potions
		self.currently_active = currently_active
	
	def heal(self):
		self.pokemon[self.currently_active].regain_health(20)

	def switch_pokemon(self, num):
		if num >= 0 and num < len(self.pokemon):
			self.currently_active = num
	
	def battle(self, trainer):
		pass
		




bulbasore = Pokemon("Bulbasore", 5, 'grass', 59, 59, False)
charmander = Pokemon("Charmander", 5, 'fire', 66, 66, False)
squirtal = Pokemon("Squirtal", 5, 'water', 50, 50, False)

bulbasore.attack(squirtal)

chris = Trainer('Chris', [bulbasore, charmander, squirtal], 4, 0)
print(chris.pokemon[2].current_health)
chris.heal()

