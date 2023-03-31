import numpy as np
import matplotlib.pyplot as mp
np.random.seed(12)
iksy, igreki = [],[]
linia = [(299, 707), (318, 699), (342, 690), (355, 681), (375, 672), (392, 663), (410, 654), (425, 645), (443, 636), (459, 627), (476, 618), (490, 610), (506, 601), (524, 592), (541, 583), (559, 574), (576, 565), (593, 556), (608, 547), (623, 538)]
for point in linia:
    iksy.append(point[0])
    igreki.append(point[1])
igreki.reverse()
x = np.linspace( 0, 1, 25 )
y = np.cos(x) + 0.5*np.random.rand(25)

p = np.poly1d( np.polyfit(x, y, 3) )
t = np.linspace(0, 1, 250)

polynomial = np.poly1d(np.polyfit(iksy, igreki, 1))
ttt = np.linspace(0, 1280, 12800)
mp.plot(iksy, igreki, 'o', ttt, polynomial(ttt), '-')
mp.show()