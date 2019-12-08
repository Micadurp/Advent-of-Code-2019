#!/usr/bin/python3
import math

def main():
	filepath = 'day2intcode.txt'
	with open(filepath) as f:
		int_list = f.readline().split(',')
		int_list = list(map(int, int_list))
		opcode = 99
		index = 0
		running = True
		int_list[1] = 12
		int_list[2] = 2
		while(running):
			opcode = int_list[index]
			if(opcode == 1):
				opcodeone(int_list, index)
			elif(opcode == 2):
				opcodetwo(int_list, index)
			elif(opcode == 99):
				opcodeninenine()
				running = False
			index += 4
		print(int_list[0])
def opcodeone(int_list, index):
	pos1 = int_list[index+1]
	pos2 = int_list[index+2]
	pos3 = int_list[index+3]
	
	int_list[pos3] = int_list[pos1] + int_list[pos2]
	
	
def opcodetwo(int_list, index):
	pos1 = int_list[index+1]
	pos2 = int_list[index+2]
	pos3 = int_list[index+3]
	
	int_list[pos3] = int_list[pos1] * int_list[pos2]
	
def opcodeninenine():
	print("stopping")
	
if __name__ == '__main__':
    main()