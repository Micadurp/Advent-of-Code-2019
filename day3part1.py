#!/usr/bin/python3

def main():
	filepath = 'day3wirepaths.txt'
	with open(filepath) as f:
		wire_one = f.readline().split(',')
		wire_two = f.readline().split(',')
		wire_one = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(',')
		wire_two = "U62,R66,U55,R34,D71,R55,D58,R83".split(',')
		nav_map_one = []
		nav_map_two = []
		navigate_path(wire_one, nav_map_one)
		navigate_path(wire_two, nav_map_two)
		find_crossings(nav_map_one, nav_map_two)
		print(nav_map_one)
		print(nav_map_two)
		

def navigate_path(wire, nav_map):
	nav_map.append((0,0))
	index = 0
	
	for move in wire:
		dir = move[0]
		steps = int(move[1:])
		#print(steps)
		if(dir == 'U'):
			nav_map.append((nav_map[index][0], nav_map[index][1] + steps))
		elif(dir == 'D'):
			nav_map.append((nav_map[index][0], nav_map[index][1] - steps))
		elif(dir == 'R'):
			nav_map.append((nav_map[index][0] + steps, nav_map[index][1]))
		elif(dir == 'L'):
			nav_map.append((nav_map[index][0] - steps, nav_map[index][1]))
		index += 1
		
def find_crossings(nav_map_one, nav_map_two):
	distance = 9999999
	for i in range(1, len(nav_map_one)):
		for j in range(1, len(nav_map_two)):
			line1 = (nav_map_one[i-1], nav_map_one[i])
			line2 = (nav_map_two[j-1], nav_map_two[j])
			x, y = line_intersection(line1, line2)
			if(x == 0 and y == 0):
				continue
			if(abs(x) + abs(y) < distance):
				print("l1:", line1 ," l2:", line2)
				print("x:", x ," y:", y)
				distance = abs(x) + abs(y)
	print(distance)

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return 999, 999

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y
	
if __name__ == '__main__':
    main()