class Animal(object):
	def run(self):
		print("animal is running...")

class Dog(Animal):
	def run(self):
		print("Dog is running...")

class Cat(Animal):
	def run(self):
		print("cat is runnung...")
def run_twice(animal):
	animal.run()
	animal.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()

run_twice(Animal())
run_twice(Dog())
