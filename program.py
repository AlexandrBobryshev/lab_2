import matplotlib.pyplot as plt

f = open('DS3.txt', 'r')
x = []
y = []

while True:
    line = f.readline()
    if not line:
        break
    x.append(int(line.split()[0]))
    y.append(int(line.split()[1]))

plt.rcParams['toolbar'] = 'None'
plt.figure(figsize=(960/plt.rcParams['figure.dpi'], 540/plt.rcParams['figure.dpi']))
plt.scatter(x, y)
plt.axis('off')
plt.savefig('result.jpg')
plt.show()
f.close()
