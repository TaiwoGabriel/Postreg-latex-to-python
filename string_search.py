import numpy as np
import pandas as pd
import re


a1 = " 159.930 &  168.526 &  86.926 &  26.722 &  79.339 &  21.302 &  78.514 &  23.831 &  22.108 &  21.542   "
b1 = a1.replace('&', '')

b2 = list(b1.split())
b3=list(map(float,b2))
print(b3, '\n')
b4 = (sum(b3))/10
b5 = b4 *100
print('Average:',round(b5, 1))
