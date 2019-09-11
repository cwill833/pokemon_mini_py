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




bulbasore = Pokemon("Bulbasore", 10, 'grass', 100, 100, False)
charmander = Pokemon("Charmander", 10, 'fire', 75, 75, False)

bulbasore.attack(charmander)
charmander.attack(bulbasore)