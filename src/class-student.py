class Student:
	def __init__(self, first_name, last_name, gender):
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender

	def __str__(self):
        return str(self.first_name) + " " + str(self.last_name) + " " + str(self.gender)

	@property
	def get_first_name(self):
	    return self.get_first_name	

	@property
	def get_last_name(self):
		return self.get_last_name

	@property
	def get_gender(self):
	    return self.get_gender