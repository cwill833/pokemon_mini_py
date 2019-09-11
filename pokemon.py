class Pokemon:
	def __init__(self, name, level, element, max_health, current_health, is_knocked_out, power):
		self.name = name
		self.level = level
		self.element = element
		self.max_health = max_health
		self.current_health = current_health
		self.is_knocked_out = is_knocked_out
		self.power = power
	
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
		poke.lose_health(self.power)

pikachu = Pokemon("Pickachu", 10, 'electric', 100, 100, False, 12)
ratattat = Pokemon("Ratattat", 10, 'normall', 75, 75, False, 5)

pikachu.attack(ratattat)