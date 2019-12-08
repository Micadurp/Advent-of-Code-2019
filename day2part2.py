#!/usr/bin/python3
import math

def main():
	answer = 19690720
	
	for noun in range(100):
		for verb in range(100):
			if(run_int_list(noun, verb) == answer):
				print(100 * noun + verb)
	
def run_int_list(noun, verb):
	opcode = 99
	inst_point = 0
	running = True
	inst_nr = 0
	
	filepath = 'day2intcode.txt'
	with open(filepath) as f:
		int_list = f.readline().split(',')
		int_list = list(map(int, int_list))
		int_list[1] = noun
		int_list[2] = verb
		while(running):
			opcode = int_list[inst_point]
			if(opcode == 1):
				opcodeone(int_list, inst_point)
				inst_nr = 4
			elif(opcode == 2):
				opcodetwo(int_list, inst_point)
				inst_nr = 4
			elif(opcode == 99):
				opcodeninenine()
				running = False
				inst_nr = 1
			inst_point += inst_nr
		return int_list[0]

def opcodeone(int_list, inst_point):
	pos1 = int_list[inst_point+1]
	pos2 = int_list[inst_point+2]
	pos3 = int_list[inst_point+3]
	
	int_list[pos3] = int_list[pos1] + int_list[pos2]

def opcodetwo(int_list, inst_point):
	pos1 = int_list[inst_point+1]
	pos2 = int_list[inst_point+2]
	pos3 = int_list[inst_point+3]
	
	int_list[pos3] = int_list[pos1] * int_list[pos2]
	
def opcodeninenine():
	return
	
if __name__ == '__main__':
    main()