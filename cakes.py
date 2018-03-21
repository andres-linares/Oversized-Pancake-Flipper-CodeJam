# -*- coding: utf-8 -*-

def main():
	file = open("A-small-practice.in.txt", "r")
	outputFile = open("outpu.txt", "w")
	testCases = int(file.readline())
	for x in range(0, testCases):
		line = file.readline().split()
		s = line[0]
		k = line[1]
		solution = solve(s, int(k))
		output = "Case #{0}: {1}\n".format(x+1, solution)
		outputFile.write(output)
	outputFile.close()

def solve(s, k):
	states = []
	price = obtainPrice(s)
	cakes = len(s)

	entry = [s, 0, price, 0]
	states.append(entry)

	movements = cakes - k + 1
	if movements < 0:
		movements = 0

	if price == 0:
		return 0
	else:
		while True:
			bestExploration = searchStates(states)
			states[bestExploration][3] = 1
			finishState = explore(states[bestExploration][0], movements, k,
				states, states[bestExploration][1])
			if finishState != -1:
				return finishState
			elif bestExploration == -1:
				break


	return "IMPOSSIBLE"


def explore(s, movements, k, states, flips):
	for x in range(0, movements):
		newState = applyMovement(s, k, x)
		if isNewState(newState, states):
			price = obtainPrice(newState)
			entry = [newState, flips + 1, obtainPrice(newState), 0]
			states.append(entry)
			if price == 0:
				return flips + 1 
	return -1

def isNewState(newState, states):
	for x in states:
		if newState == x[0]:
			return False
	return True

def applyMovement(s, k, index):
	newState = ""
	for x in range(0, len(s)):
		cake = s[x]
		if(cake == '-' and (x >= index and x < index + k)):
			cake = '+'
		elif (x >= index and x < index + k):
			cake = '-'
		newState += cake
	return newState

def searchStates(states):
	bestIndex = -1
	bestValue = 999
	for x in range(0, len(states)):
		if states[x][3] == 0:
			g_n = states[x][2]
			h_n = 2 * states[x][1]
			f_n = g_n + h_n
			if f_n < bestValue:
				bestValue = f_n
				bestIndex = x

	return bestIndex

def obtainPrice(s):
	price = 0
	for x in s:
		if x == "-":
			price += 1
	return price


if __name__ == "__main__":
	main()