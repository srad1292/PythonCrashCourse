"""
Class that can be used to represent a car.
"""

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

	def fill_gas_tank(self):
		"""Fill gas tank to full in a car"""
		print("Gas tank is now full")