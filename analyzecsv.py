import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
a = pd.read_csv("1_1.csv")
xaxis = a["amount"]
yaxis = a["balance"]
plt.plot(xaxis,yaxis)
plt.scatter

plt.show()
