import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

with open ('data.txt', 'r') as inp:
    txt = [i for i in inp.readlines()]
l1 = [i for i in txt[0][1:-1].split('][')]
l2 = []
for j in l1:
    l2.append(j[1:-1].split('), ('))
l3 = []
for k in l2:
    l3.append([tuple(map(float, l.split(', '))) for l in k])

def change_tuple(tup, val):
    y = list(tup)
    del y[2]
    y.append(val)
    return tuple(y)

fin_l = []

for big_l in range(len(l3)):
    almost_fin_l = []
    for sm_l in range(len(l3[big_l])):
        if l3[big_l][sm_l][2] < 5:
            print(l3[big_l][sm_l])
            almost_fin_l.append(change_tuple(l3[big_l][sm_l], 5.0))
        elif l3[big_l][sm_l][2] > 4000:
            print(l3[big_l][sm_l])
            almost_fin_l.append(change_tuple(l3[big_l][sm_l], 4000.0))
        else:
            almost_fin_l.append(l3[big_l][sm_l])
    fin_l.extend(almost_fin_l)

fin_pd = pd.DataFrame(fin_l, columns=['quality', 'angle', 'distance'])
fin_pd['rad'] = fin_pd['angle'].apply(lambda x: np.deg2rad(x))
fin_pd['x'] = fin_pd['distance'] * fin_pd['rad'].apply(lambda x: math.cos(x))
fin_pd['y'] = fin_pd['distance'] * fin_pd['rad'].apply(lambda x: math.sin(x))
fig, ax = plt.subplots()
ax.plot(fin_pd['x'], fin_pd['y'], marker='o', linestyle='')
# plt.show()
plt.savefig('laser__в2рая_жизнь_туалетной_бумаги.png')
