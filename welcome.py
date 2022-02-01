#! /usr/bin/python3
print("Welcome to my repository")
last = 1
running = 1
for n in range(56):
    running = (n**2*running)/last
    last = n
print(running, "ooo")
print("Damn that's a lot of banana bread")