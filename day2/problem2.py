import requests as r
import pandas as pd

cookie_session = "session=53616c7465645f5fe5b43baa3978676e6ee21c3867fa195fabc1574e137162acdb7bb51aa25df722c4e1026c296ae422"

page = r.get("https://adventofcode.com/2021/day/2/input",
             headers={"Cookie": cookie_session})

data = page.content.decode('UTF-8').split('\n')[:-1]

# Idk how to do this without iterating a list...:(
aim = 0
horizontal = 0
depth = 0

for i, num in enumerate(data):
    direction, amount = num.split(' ')
    amount = int(amount)
    if direction == "forward":
        horizontal += amount
        depth += aim*amount
    elif direction == "up":
        aim -= amount
    elif direction == "down":
        aim += amount

print(horizontal*depth)
