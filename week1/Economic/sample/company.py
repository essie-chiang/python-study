from employee import Employee

class Company(object):
	"""docstring for Company"""
	def __init__(self, name, employees=[]):
		self.name = name
		self.employees = employees

	def hire(self, employee):
		if employee not in self.employees:
			self.employees.append(employee)	
		
	def fire(self, employee):
		if employee in self.employees:
			self.employees.remove(employee)

	def get_info(self):
		ret = "Company: {}".format(self.name)
		for employee in self.employees:
			ret += "{}\n".format(self.employee.get_info())
		return ret
test = Company("testCom")

if __name__ == "__main__":
	julyedu = Company("julyedu")
	julyedu.get_info()

