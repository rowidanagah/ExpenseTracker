import os 
class LogFile:
	def current_balance(self, dir_path):
		# Load your total balance of the given user
		with open(dir_path + "total_balance.txt", 'r') as file:
			balance = file.read()
			return balance.strip("\n").split("\n")

	def new_balance(self, dir_path, balance):
		# add new & change balance into the default file of the given user
		with open(dir_path + "total_balance.txt", 'w') as file:
			file.write(balance +'\n')
		return

	def append_balance(self, dir_path ,salary):
		# append new balance into the default file
		with open(dir_path + "total_balance.txt", 'a') as file:
			file.write(salary + '\n')
		return 

	def write_to_new_file(self,dir_path, expense):
		# add new & change salary into a given&specified file
		with open(dir_path, 'w') as file:
			file.write(expense+ '\n')
	
	def append_expense_to_new_file(self, dir_path, expense):
		# append new salary into a specified file
		with open(dir_path, 'a') as file:
			file.write(expense + '\n')
		return

	def current_balance_in_another_file(self, dir_path, file_name = "daily_balance.txt"):
		"""read logs from a specified file,
		aka-> we could sperate totalBalance from daily balance
		"""
		with open(dir_path + file_name , 'r') as file:
			balance = file.read()
			return balance.strip("\n").split("\n")

	def clear_history(sef, dir_path ):
		os.remove(dir_path)
		
