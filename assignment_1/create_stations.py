from stations import Station 
from coordinates import CartesianCoordiante, GeographicalCoordinate, OtherCoordinate


def create_stations():
	stations = []
	hermanus = Station(
		name='Hermanus', 
		code='HNUS',
		cartesian_coordinate=CartesianCoordiante(
			x=4973168.840,
			y=1734085.512,
			z=-3585434.051,
		),
		geographical_coordinate=GeographicalCoordinate(
			latitude=34.42463,
			longitude=19.22306,
		),
		other_coordinate=OtherCoordinate(
			y=-20504.530,
			x=3810786.584,
		),
		ellipsoidal_height=63.048,
	)
	pretoria = Station(
		name='Pretoria',
		code='PRET',
		cartesian_coordinate=CartesianCoordiante(
			x=5064032.237,
			y=2724721.031,
			z=-2752950.762,
		),
		geographical_coordinate=GeographicalCoordinate(
			latitude=25.73203,
			longitude=28.28264,
		),
		other_coordinate=OtherCoordinate(
			y=71984.249,
			x=2847342.471,
		),
		ellipsoidal_height=1387.339,
	)
	richards_bay = Station(
		name='Richards Bay',
		code='RBAY',
		cartesian_coordinate=CartesianCoordiante(
			x=4739765.776,
			y=2970758.460,
			z=-3054077.535,
		),
		geographical_coordinate=GeographicalCoordinate(
			latitude=28.79554,
			longitude=32.07839,
		),
		other_coordinate=OtherCoordinate(
			y=89979.302,
			x=3186957.331,
		),
		ellipsoidal_height=31.752,
	)
	thohoyandou = Station(
		name='Thohoyandou',
		code='TDOU',
		cartesian_coordinate=CartesianCoordiante(
			x=5064840.815,
			y=2969624.535,
			z=-2485109.939,
		),
		geographical_coordinate=GeographicalCoordinate(
			latitude=23.07991,
			longitude=30.38401,
		),
		other_coordinate=OtherCoordinate(
			y=63116.647,
			x=2553520.044,
		),
		ellipsoidal_height=630.217,
	)
	ulundi = Station(
		name='Ulundi',
		code='ULDI',
		cartesian_coordinate=CartesianCoordiante(
			x=4796680.897,
			y=2930311.589,
			z=-3005435.714,
		),
		geographical_coordinate=GeographicalCoordinate(
			latitude=28.29312,
			longitude=31.42093,
		),
		other_coordinate=OtherCoordinate(
			y=-41290.625,
			x=3130997.349,
		),
		ellipsoidal_height=607.947,
	)
	stations.append(hermanus)
	stations.append(pretoria)
	stations.append(richards_bay)
	stations.append(ulundi)
	return stations