import json
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import urllib.request


def process_points(points):
    x = []
    y = []
    for point in points:
        x.append(point['x'])
        y.append(point['y'])
    return x, y
    
f = urllib.request.urlopen("http://18.222.190.24:8000/regression_graph")
jdat = f.read()

data = json.loads(jdat)
print("keys: {}".format(data.keys()))

dot_a = data['dot_a']  #x/y for first set of dots
dot_b = data['dot_b']  #x/y for second set of dots
line_a = data['line_a']  #first line 2 sets of 2 dots
line_b = data['line_b']  #second set of 2 dots

x,y = process_points(dot_a)
plt.plot(x,y, 'x', Label="dot a")
x1, y1 = process_points(dot_b)
plt.plot(x1,y1, 'x', Label="dot b")

x2, y2 = process_points(line_a)
plt.plot(x2, y2, Label="line a", color="green")

x3, y3 = process_points(line_b)
print(f"x3: {x3}, y3: {y3}")
plt.plot(x3, y3, Label="line b", color="green")
plt.savefig("./graph.png")

plt.show()