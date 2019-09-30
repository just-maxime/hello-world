# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:00:58 2019

@author: maxim
"""

import numpy as np

#a1=np.mat([1,2])  
#a2=np.mat([[1],[2]])
#a3=a1*a2
#print(a3)
#1*2的矩阵乘以2*1的矩阵，得到1*1的矩阵

a1=np.mat([[3,-2,0,-1],[0,2,2,1],[1,-2,-3,-2],[0,1,2,-1]])
a2=a1.I
print(a2)
#求矩阵matrix([[0.5,0],[0,0.5]])的逆矩阵

#a1=np.mat([[1,1],[0,0]])
#a2=a1.T
#print(a2)
#求矩阵的转置

#a1=np.array([[2,6,11,5],[1,2,5,2],[2,2,3,4],[1,2,3,4]])
#a2=np.linalg.det(a1)
#print(a2)
#求行列式的值


