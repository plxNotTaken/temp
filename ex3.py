# encoding: utf8
# ----------------------------------
import sys
sys.path.append('bayesian')
sys.path.append('prettytable-0.7.2')
from bayesian.bbn import build_bbn

def f_rain(rain):
	if rain:
		return 0.2
	else:
		return 0.8

def f_sprinkler(sprinkler, rain):
	if sprinkler:
		if rain:
			return 0.01
		else:
			return 0.4
	else:
		if rain:
			return 0.99
		else:
			return 0.6

def f_grass_wet(grass_wet, sprinkler, rain):
	if sprinkler:
		if rain:
			if grass_wet:
				return 0.99
			else:
				return 0.01
		else:
			if grass_wet:
				return 0.9
			else:
				return 0.1
	else:
		if rain:
			if grass_wet:
				return 0.8
			else:
				return 0.2
		else:
			if grass_wet:
				return 0.0
			else:
				 return 1

if __name__ == '__main__':
	g = build_bbn(
	f_rain,
	f_sprinkler,
	f_grass_wet,
	domains=dict(
	rain=[True, False],
	sprinkler=[True, False],
	grass_wet=[True, False]))
