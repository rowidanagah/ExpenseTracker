import os


os.chdir("../../res")

DIR_PATH = os.path.dirname(os.path.realpath('__file__'))

class User:
	def check_init(self):
		""" Check is the res folder that hold 
		users' data exist """
		if not os.path.isdir("users"):
			self.initial_setup()
		return True

	def initial_setup(self):
		os.mkdir("users")

	def check_user(self,user_name):
		if not os.path.isdir("/users/{}".format(user_name)):
			self.create_user("/users/{}".format(user_name))
		return True

	def create_user(self,user_name):
		os.mkdir(DIR_PATH + user_name)

	def check_user_history(self, user_name):
		return len(os.listdir(DIR_PATH + "/users/{}".format(user_name)))
		
	def update_user(self, user_name, new_user_name):
		# to rename user's folder 
		file_name = DIR_PATH +"/users/{}".format(user_name)
		dst = DIR_PATH +"/users/{}".format(new_user_name)
		os.rename(file_name, dst)

		
