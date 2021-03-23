import numpy as np
import pandas as pd

#code 1
A = np.zeros((4, ))
print('A: ', A)

#code 2
B = np.zeros((4, ))
B[1] = 1
print('B: ', B)

#code 3
C = np.zeros((4, ))
C[1:] = 1.
print('C: ', C)

#code 4
D =  np.ones((4,))
D[-1] = 0
print('D: ', D)
#D: [1. 1. 1. 0.]
'''
A
D = np.zeros((4, ))
D[:3] = 1
print('D: ', D)

B
D = np.ones((4,))
D[4] = 0
print('D: ', D)

C 
D = np.zeros((4, ))
D[:-1] = 1
print('D: ', D)
'''

#code 5
E =  np.ones((2, 2)) + np.ones((2, 2))
print('E: \n', E)
# E: [[2. 2.]
#    [2. 2.]]
'''
A
E = 2 * np.ones((2, 2))
print('E: \n', E)

B
E = np.array([2.] * 4).reshape(2, 2)
print('E: \n', E)

D
E = np.twos((2, 2))
print('E: \n', E)
'''

#code 6
F = np.array([[1, 2], [3, 4]])
G = F[0, :]
G[1] = 10
print('F: \n', F)

#code 7
H = np.array([[1, 3], [11, 10]])
print(np.mean(H[H > np.pi]))

#code 8
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
         'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
         'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#code 9
df = pd.DataFrame(data=data, index=labels)
print(df)
#print(df.rows_cols)
#print(df.len)
#print(df.lenght)
print(df.shape)
print('')
print( df['animal'].value_counts())
print('')
print(df.describe())
print('')
print(df.sort_values(by='visits', ascending=False))
print('')
print(df.iloc[:, 3])
print('')

#code 10
y_true = np.array([1., 2., 1.])
y_pred = np.array([1.1, 1.98, 1.05])
print(np.sqrt(((y_true-y_pred)**2).mean()))
print('')

x_true = np.array([1., 2., 1.])
x_pred = np.array([1., 2., 1.])
print(np.sqrt(((x_true-x_pred)**2).mean()))