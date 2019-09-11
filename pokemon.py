class Pokemon:
	def __init__(self, name, level, element, max_health, current_health, is_knocked_out):
		self.name = name
		self.level = level
		self.element = element
		self.max_health = max_health
		self.current_health = current_health
		self.is_knocked_out = is_knocked_out
	
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

pikacu = Pokemon('Pikacu', 25, 'electric', 50, 50, False)

pikacu.lose_health(50)
pikacu.regain_health(50)