
import json
import re

data = open("user.json").read()

def inv1(n):
    return str(255 - int(n))

def change(match):
    return "rgb({}, {}, {})".format(
            inv1(match.group(1)),
            inv1(match.group(2)),
            inv1(match.group(3)))

# print(re.sub("rgb\(([0-9]+), ([0-9]+), ([0-9]+)", change, "rgb(100, 20, 30) rgb(10, 255,100)"))
print(re.sub("rgb\(([0-9]+), ([0-9]+), ([0-9]+)", change, data))






