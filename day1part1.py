#!/usr/bin/python3
import math

def main():
	filepath = 'day1module_mass_list.txt'
	with open(filepath) as f:
		module_mass = int(f.readline())
		needed_fuel = 0
		while module_mass:
			needed_fuel = needed_fuel + math.floor(int(module_mass)/3) - 2
			module_mass = f.readline()
		print(needed_fuel)
	
	
if __name__ == '__main__':
    main()