#! /usr/bin/python3
print("Welcome to my repository")
last = 1
for n in range(56):
    running = (n**2*running)/last
    last = n
print(running, "ooo")