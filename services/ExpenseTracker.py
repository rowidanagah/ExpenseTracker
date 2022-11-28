import sys
import os 

sys.path.append("../src/apidoc/")

from LogesInFolders import LogFile

os.chdir("../res/users")


class ExpenseTracker:
	def __init__(self,user_name):
		# Redirect to user's folder
		self.cost = LogFile()
		self.DIR_PATH = os.path.dirname(os.path.realpath('__file__')) \
		+ "/{}/".format(user_name) 

	def add_balance(self,expense):
		# add new balance into current balance file hostory
		self.cost.new_balance(self.DIR_PATH,expense)

	def add_daily_expense(self,expense,file_name = ''):
		""" add & append new expense into the default
		 `daily_expense` file unless there's a spesified file """
		dst = file_name if file_name else "daily_expense.txt"
		self.cost.append_expense_to_new_file(self.DIR_PATH+dst, expense)

	def sum_up_your_balance(self):
		"""Read all the current balance"""
		balance = self.cost.current_balance_in_another_file(self.DIR_PATH,"total_balance.txt")
		res =  sum(list(map(int, balance)))
		print("your total balance fo far is :- ", res)
		return res 

	def sum_up_your_daily_expense(self):
		expenses = self.cost.current_balance_in_another_file(self.DIR_PATH,"daily_expense.txt")
		res = str(sum(list(map(int, expenses))))
		print("voala your total daily expenses is {} !".format(res))
		# add the total expenses into current_balance file
		self.cost.append_balance(self.DIR_PATH, res)

	def current_balance(self):
		try:
			"""balance = self.cost.current_balance(self.DIR_PATH)
			print(list(map(float, balance)))
			"""
			balance = self.sum_up_your_balance()
			print("Perfect Balance {}".format(balance) if balance > 0 else "Your balance is negative!! Please add")
		except:
			return print("Your current balance file not found")

	def history_expense(self):
		for exp in os.listdir(self.DIR_PATH):
			print("Your saved expenses at {} folder ".format(exp))
			res = self.cost.current_balance_in_another_file(self.DIR_PATH,exp)
			print(*res if res else "No history found at this file!")
			print("--------------")

	def clear(self, file_name = ""):
		"""by default ->> remove currently daily_expense folder
		unless folder_name if spesified..
		"""
		dst = file_name if file_name else "daily_expense.txt"
		print(self.DIR_PATH + dst)
		self.cost.clear_history(self.DIR_PATH + dst)
		print("Your {} Balance folder deleted!".format(dst))

	
expense = ExpenseTracker("dana")
"""expense.add_daily_expense("100089")
expense.add_daily_expense("189")

expense.current_balance()
expense.add_balance("89999")
expense.current_balance()
expense.history_expense()

expense.sum_up_your_daily_expense()
expense.add_daily_expense("900")
expense.sum_up_your_daily_expense()
"""
expense.history_expense()