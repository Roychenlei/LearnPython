from collections import defaultdict

colours = (
	('Yasoob','Yellow'),
	('Ali','Blue'),
	('Arham','Green'),
	('Ali','Black'),
	('Yasob','Red'),
	('Ahmed','Silver'),
	)

favourite_colours = defaultdict(list)

for name, colour in colours:
	favourite_colours[name].append(colour)

print(favourite_colours)