#This script converts latex table to pandas dataframe for different manipulations

import numpy as np
import pandas as pd
import re
data = "C:/Users/Omomule Taiwo G/Desktop/CHPC/latex_to_python/table.tex"
df = pd.read_csv(data,
                 sep='&',
                 header=None)

print(df.to_string(), "\n")

test_acc = df.iloc[:,2]
print(test_acc, "\n")

my_list = []
for m in test_acc:
    my_list.append(m)

print(my_list)

#Testing if all values are of the same data type. In case all values are tested to be of integer type
#res = all(isinstance(sub, type(my_list[0])) for sub in my_list[1:])
res = all(isinstance(item, float) for item in my_list)

if res == True:
    avg_test_num = (sum(my_list)) / 5
    print(round(avg_test_num,3))

else:
    l0 = my_list[0]
    numeric_string0 = (re.sub("[^0-9]", "", l0))
    numeric0 = float(numeric_string0)/1000
    print(numeric0)

    l1 = my_list[1]
    numeric_string1 = (re.sub("[^0-9]", "", l1))
    numeric1 = float(numeric_string1)/1000
    print(numeric1)

    l2 = my_list[2]
    numeric_string2 = (re.sub("[^0-9]", "", l2))
    numeric2 = float(numeric_string2)/1000
    print(numeric2)

    l3 = my_list[3]
    numeric_string3 = (re.sub("[^0-9]", "", l3))
    numeric3 = float(numeric_string3)/1000
    print(numeric3)

    l4 = my_list[4]
    numeric_string4 = (re.sub("[^0-9]", "", l4))
    numeric4 = float(numeric_string4)/1000
    print(numeric4)
    print("\n")

    avg_test = (numeric0+numeric1+numeric2+numeric3+numeric4)/5
    print(round(avg_test, 3))

