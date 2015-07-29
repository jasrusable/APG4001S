class CartesianCoordiante(object):
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

class GeographicalCoordinate(object):
	def __init__(self, latitude, longitude):
		""" latitude and longitude should be in 
		decimal degrees.
		"""
		self.latitude = latitude
		self.longitude = longitude

class OtherCoordinate(object):
	def __init__(self, y, x):
		self.y = y
		self.x = x
		