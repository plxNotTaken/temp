# encoding: utf8
# ----------------------------------
import sys
sys.path.append('bayesian')
sys.path.append('prettytable-0.7.2')
from bayesian.bbn import build_bbn

def f_prize_door(prize_door):
	return 0.33333333

def f_guest_door(guest_door):
	return 0.33333333

def f_monty_door(prize_door, guest_door, monty_door):
 	if prize_door == guest_door:
		if prize_door == monty_door:
			return 0
		else:
			return 0.5
	elif prize_door == monty_door:
		return 0
	elif guest_door == monty_door:
		return 0
	else:	
		return 1


if __name__ == '__main__':
	g = build_bbn(
	f_prize_door,
	f_guest_door,
	f_monty_door,
	domains=dict(
	prize_door=['A', 'B', 'C'],
	guest_door=['A', 'B', 'C'],
	monty_door=['A', 'B', 'C']))
