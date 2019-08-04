# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a calculator script file.
"""

# 15 a = b = c = d = e = f = m = x = y = z = 0
# 27   elif equation[-1] in "abcdefmxyz":
# 28   
import time
import signal
TIMEOUT = 5
def interrupted(signum, frame):
    """called when read times out"""
    print("inturrupted!")
signal.signal(signal.SIGALRM, interrupted)
def myinput(string):
    """waits for {TIMEOUT} seconds"""
    try:
        something = input(string)
        return something
    except:
        # timeout
        return
start = time.time()    
ans = 0
while True:
    signal.alarm(TIMEOUT)
    equation = myinput(">>> ").strip()
    signal.alarm(0)
    if equation == "":
        print(ans)
    elif equation.upper() in "QUIT":
        break
    elif equation[0] in "+-*/%":
        try:
            sol = eval(equation[1:])
            ans = eval(str(ans) + equation[0] + str(sol))
            print(ans)
        except:
            input("Syntax Error")
    else:
        try:
            ans = eval(equation)
            print(ans)
        except:
            input("Syntax Error")
end = time.time()
running_time = end - start
print("Program Running Time :", running_time, "seconds")