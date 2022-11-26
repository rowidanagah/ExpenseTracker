import os
import sys

sys.path.append("../../src/apidoc/")

from user import UserFolderSetup

os.chdir("../../res")

DIR_PATH = os.path.dirname(os.path.realpath('__file__'))

DIR_PATH += "/users/"

class User:
	def __init__(self):
		self.setup = UserFolderSetup()
		self.create_initial_setup()

	def create_initial_setup(self):
		if not self.setup.check_init():
			self.setup.initial_setup()
	
	def check_user(self, user_name):
		return self.setup.check_user(DIR_PATH + user_name)

	def check_user_history(self, user_name):
		try:
			res = self.setup.check_user_history(DIR_PATH+user_name)
			return res if res else "No history provided"
		except:
			return "not a valid user name"

	def create_user(self, user_name):
		""" validate first that this user doesn't exist -> create
		"""
		#path = DIR_PATH + "/users/{}".format(user_name)
		path = DIR_PATH + "/{}".format(user_name)
		if not self.setup.check_user(path):
			self.setup.create_user(path)

	def rename(self, old_name, new_name):
		res = DIR_PATH + "/{}".format(old_name)
		dst = DIR_PATH + "/{}".format(new_name)
		try: 
			# make sure if the new username doesn't already exist.
			self.setup.update_user(res,dst)
		except:
			print("UserName already exists")

user = User()
print(user.check_user_history("dana"))
