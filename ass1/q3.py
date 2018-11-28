from sympy import *

p_0 = Symbol('p_0')
p_1 = Symbol('p_1')
p_2 = Symbol('p_2')
p_3 = Symbol('p_3')
p_4 = Symbol('p_4')
p_5 = Symbol('p_5')
p_6 = Symbol('p_6')
p_7 = Symbol('p_7')
p_8 = Symbol('p_8')
p_9 = Symbol('p_9')
p_10 = Symbol('p_10')
p_11 = Symbol('p_11')
p_12 = Symbol('p_12')
p_13 = Symbol('p_13')
p_14 = Symbol('p_14')


temp = solve([10*p_0-5*p_1-2.5*p_2, 15*p_1-5*p_0-5*p_3-2.5*p_4, 12.5*p_2-5*p_0-5*p_4-2.5*p_5,
              15*p_3-5*p_1-5*p_6-2.5*p_7, 17.5*p_4-5*p_1-5*p_2-5*p_7-2.5*p_8,
              7.5*p_5-5*p_2-5*p_8-2.5*p_9, 15*p_6-5*p_3-5*p_10-2.5*p_11,
              17.5*p_7-5*p_3-5*p_4-5*p_11-2.5*p_12, 12.5*p_8-5*p_4-5*p_5-5*p_12-2.5*p_13,
              7.5*p_9-5*p_13-2.5*p_14, 5*p_10-5*p_6, 7.5*p_11-5*p_6-5*p_7,
              7.5*p_12-5*p_7-5*p_8, 7.5*p_13-5*p_9,
              p_0 + p_1 + p_2 + p_3 + p_4 + p_5 + p_6 + p_7 + p_8 + p_9 + p_10 + p_11 + p_12 + p_13 + p_14- 1],
             [p_0, p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, p_12, p_13, p_14])

for key in temp:
    print(key,temp[key])