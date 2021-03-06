class Car():
	"""A simple representation of a car."""

	def __init__(self, make, model, year):
		"""Initialze attributes to describe a car."""

		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Display the car's mileage"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value
		Reject the change if they try to lower the mileage
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount of miles to the odometer reading"""
		self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)

print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#Update attr through instance
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#Update attr through a method
my_new_car.update_odometer(46)
my_new_car.read_odometer()

my_new_car.update_odometer(20)
my_new_car.read_odometer()

my_new_car.update_odometer(15000)
my_new_car.read_odometer()

#Update attr through incrementing it
my_new_car.increment_odometer(100)
my_new_car.read_odometer()