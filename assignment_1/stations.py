
class Station(object):
	def __init__(self, name, code, cartesian_coordinate, 
			geographical_coordinate, other_coordinate, ellipsoidal_height):
		""" Name should be the full name of the station.
		Code should be a four character string.
		"""
		self.name = name
		self.code = code
		self.cartesian_coordinate = cartesian_coordinate
		self.geographical_coordinate = geographical_coordinate
		self.other_coordinate = other_coordinate
		self.ellipsoidal_height = ellipsoidal_height
