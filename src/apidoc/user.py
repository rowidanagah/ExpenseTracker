import os
class UserFolderSetup:
	""" It's a more general repo to magage folder
	 folder path & structure per user 
	"""
	def check_init(self):
		""" Check is the res folder that hold 
		users' data exist """
		return os.path.isdir("users")

	def initial_setup(self):
		os.mkdir("users")

	def check_user(self,user_name):
		return os.path.isdir(user_name)

	def create_user(self,user_name):
		os.mkdir(user_name)

	def check_user_history(self, user_name):
		return os.listdir(user_name)

	def update_user(self, user_name, new_user_name):
		os.rename(user_name, new_user_name)


