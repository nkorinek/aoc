import requests as r
import pandas as pd

cookie_session = "session=53616c7465645f5fe5b43baa3978676e6ee21c3867fa195fabc1574e137162acdb7bb51aa25df722c4e1026c296ae422"

page = r.get("https://adventofcode.com/2021/day/2/input",
             headers={"Cookie": cookie_session})

data = page.content.decode('UTF-8').split('\n')[:-1]

for i, num in enumerate(data):
    data[i] = num.split(' ')
    data[i][1] = int(data[i][1])

df = pd.DataFrame(data, columns=["direction", "amount"])

horizontal = df["amount"].loc[df["direction"] == "forward"].sum()
pos_vert = df["amount"].loc[df["direction"] == "up"].sum()
neg_vert = df["amount"].loc[df["direction"] == "down"].sum()
vertical = neg_vert - pos_vert

print(horizontal*vertical)
