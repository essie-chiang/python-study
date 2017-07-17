from employee import Employee
from company import Company

if __name__ == "__main__":
	july = Employee("july", 1, 999999, None)
	print(july.get_info())
	julyedu = Company("julyedu")
	print(julyedu.get_info())
