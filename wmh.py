import matplotlib.pyplot as plt;
import numpy as np;
from mpl_toolkits.mplot3d import Axes3D;
from matplotlib import cm;

# Probability hit rate WMH
def p_hit(rat, defense):
    tn_lookup = [
    0.0, # 0 - Not real
    0.0, # 1 - Not Real
    0.0,  # 2 - Special case
    35.0, # 3+
    33.0, # 4+
    30.0, # 5+
    26.0, # 6+
    21.0, # 7+
    15.0, # 8+
    10.0, # 9+
    6.0, # 10+
    3.0] # 11+, 12 is special case
    
    tn = defense - rat;
    if tn >= 12:
        return 1.0/36.0;
    if tn <= 2:
        return 35.0/36.0;
    return tn_lookup[tn] / 36.0;

fig = plt.figure();
ax = fig.add_subplot(111, projection='3d');
X = np.arange(12);
Y = np.arange(12);
Z = [[0 for x in range(12)] for y in range(12)] ;
for x in X:
    for y in Y:
        Z[x][y] = p_hit(x,y);
X,Y = np.meshgrid(X,Y);
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)