class Employee(object):
	
	def __init__(self, name, ID, salary, manager=None):
		self.name = name
		self.ID = ID
		self.salary = salary
		self.manager = manager

	def get_info(self):
		return "Employee: {}, ID: {}, salary: {}, manager: {}".format(
			self.name, self.ID, self.salary, self.manager)

if __name__ == "__main__":
	july = Employee("july", 1, 999999, None)
	print(july.get_info())