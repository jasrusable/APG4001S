from thing import RinexParser


parser = RinexParser('data/brdc2000.15n')
parser.parse()

print(parser.get_satellite(1))
