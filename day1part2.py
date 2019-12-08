#!/usr/bin/python3
import math

def main():
	filepath = 'day1module_mass_list.txt'
	with open(filepath) as f:
		module_mass = int(f.readline())
		total_fuel_needed = 0
		while module_mass:
			module_mass = int(module_mass)
			fuel_needed = calcFuelNeeded(module_mass)
			total_fuel_needed += fuel_needed
			fule_mass = fuel_needed
			while fule_mass > 0:
				fuel_needed = calcFuelNeeded(fule_mass)
				total_fuel_needed += max(0, fuel_needed)
				fule_mass = fuel_needed
			module_mass = f.readline()
		print(total_fuel_needed)

def calcFuelNeeded(mass):
	return math.floor(mass/3) - 2

if __name__ == '__main__':
    main()