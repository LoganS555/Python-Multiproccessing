import time
A_grid = [
        [3,7,3,6],
        [9,2,0,3],
        [0,2,1,7],
        [2,2,7,9],
]

B_grid = [
        [6,5,5,2],
        [1,7,9,6],
        [6,6,8,9],
        [0,3,5,2]
]

C_grid = [
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]
]

W_arr = [0,0,0,0]

X_arr = [0,0,0,0]

V = 0

count = 0

def CompC (row,column):
        global count
        for x in range(4):
                if A_grid[row][x] > B_grid[x][column]:
                        count = count + 1
                elif A_grid[row][x] < B_grid[x][column]:
                        count = count - 1
        time.sleep(0.05)
        return count

def CompW(row):
        global count
        for x in range(4):
                if C_grid[row][x] > 0:
                        count = count + 1
                elif C_grid[row][x] < 0:
                        count = count - 1
        time.sleep(0.05)
        return count

def CompX(column):
        global count
        for x in range(4):
                if C_grid[x][column] > 0:
                        count = count + 1
                elif C_grid[x][column] < 0:
                        count = count - 1
        time.sleep(0.05)
        return count

def CompV():
        global count
        for x in range(4):
                if x % 2 == 0:
                        count = count + W_arr[x]-X_arr[x]
                else:
                        count = count + W_arr[x]+X_arr[x]
        time.sleep(0.05)
        return count

start = time.time()

print("A:")
for x in A_grid:
        for y in x:
                print(y, end=" ")
        print()

print("B:")
for x in B_grid:
        for y in x:
                print(y, end=" ")
        print()

for x in range(4):
        for y in range(4):
                C_grid[x][y] = CompC(x,y)
                count = 0

print("C:")
for x in C_grid:
        for y in x:
                print(y, end=" ")
        print()

for x in range(4):
        W_arr[x] = CompW(x)
        count = 0

print("W:")
for x in W_arr:
        print(x, end=" ")
print()

for x in range(4):
        X_arr[x] = CompX(x)
        count = 0

print("X:")
for x in X_arr:
        print(x, end=" ")
print()

V = CompV()

print("V:")
print(V)

end = time.time()
print(f'Time to complete: {end - start:.3f}s')