'''
Transportation problem, using NWC method,

check GForG
'''

grid = [[3, 1, 7, 4], [2, 6, 5, 9], [8, 3, 3, 2]] # table
supply = [300, 400, 500] # supply
demand = [250, 350, 400, 200] # demand

startR = 0 # start row
startC = 0 # start col
ans = 0
# loop runs until it reaches the bottom right corner
while startR != len(grid) and startC != len(grid[0]):
	# if demand is greater than supply
	if supply[startR] <= demand[startC]:
		ans += supply[startR] * grid[startR][startC]
		# subtract the value of supply from the demand
		demand[startC] -= supply[startR]
		startR += 1
	# if supply is greater than demand
	else:
		ans += demand[startC] * grid[startR][startC]
		# subtract the value of demand from the supply
		supply[startR] -= demand[startC]
		startC += 1

print("The initial feasible basic solution is ", ans)
