from random import choice

class fighter:
	def __init__(self, name, health, str):
		self.name = name
		self.health = health
		self.str = str

fighter1 = fighter("Zollan", 100, choice([*range(20, 40)]))
fighter2 = fighter("Kallin", 100, choice([*range(20, 40)]))

while(fighter1.health > 0 or fighter2.health > 0):
	print("\n=====================================")
	print(fighter1.name + " health: " + str(int(fighter1.health)))
	print(fighter2.name + " health: " + str(int(fighter2.health)))
	print("=====================================\n")

	f_c = choice([*range(1,3)])
	if(f_c == 1):
		f1_a = choice([*range(1,4)])
		if(f1_a == 1):
			hit = int(fighter1.str * 5 / 3)
			print(fighter1.name + " hit " + fighter2.name + " for " + str(hit) + " damage\n")

			fighter2.health -= hit
			if(fighter2.health <= 0):
				print(fighter1.name + " won the battle")
				break

		elif(f1_a == 2):
			potion = choice([*range(10,40)])
			print(fighter1.name + " used health potion to regenerate " + str(potion) + " health\n")
			fighter1.health += potion
		
		elif(f1_a == 3):
			print(fighter1.name + " just stood there\n")

	elif(f_c == 2):
		f2_a = choice([*range(1, 4)])
		if(f2_a == 1):
			hit = int(fighter2.str * 5 / 3)
			print(fighter2.name + " hit " + fighter1.name +
			      " for " + str(hit) + " damage\n")

			fighter1.health -= hit
			if(fighter1.health <= 0):
				print(fighter2.name + " won the battle")
				break

		elif(f2_a == 2):
			potion = choice([*range(10, 40)])
			print(fighter2.name + " used health potion to regenerate " +
			      str(potion) + " health\n")
			fighter2.health += potion

		elif(f2_a == 3):
			print(fighter2.name + " just stood there\n")
