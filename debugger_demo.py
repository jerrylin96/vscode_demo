# write code that calculates pi using the Monte Carlo method with one small bug in it
# then use the debugger to find the bug
import random
import math

def calc_pi(n):
    num_in_circle = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if math.sqrt(x**2 + y**2) < 1:
            num_in_circle += 1
    return 4 * num_in_circle / n

if __name__ == "__main__":
    print(calc_pi(1000000))

# Path: vscode_demo/debugger_demo.py