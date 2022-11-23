import os 

os.chdir("../../res/users")

USER_DIR = os.path.dirname(os.path.realpath('__file__'))

class CostFunction:
	def current_salary(self):
		# Load your salary 
		with open("total_balance.txt", 'r') as file:
			balance = file.read()
			return balance
	def new_salary(self, salary):
		# add new salary into the default file
		with open("total_balance.txt", 'w') as file:
			file.write(salary +'\n')
		return

	def append_salary(self, salary):
		# append new salary into the default file
		with open("total_balance.txt", 'a') as file:
			file.write(salary + '\n')
		return 

	def write_to_new_file(self, file_name, salary):
		# add new salary into a specified file
		with open(file_name, 'w') as file:
			file.write(salary+ '\n')
		return 

	def append_salary(self,file_name, salary):
		# append new salary into a specified file
		with open(file_name, 'a') as file:
			file.write(salary + '\n')
		return

	def current_salary_in_another_file(self, file_name):
		## read logs from a specified file
		with open(file_name , 'r') as file:
			balance = file.read()
			return balance

	def clear_history(sef, file_name = ""):
		dir_path = file_name if file_name else "total_balance.txt"
		os.remove(dir_path)
		return