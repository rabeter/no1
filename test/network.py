
import random
import numpy as np

class network(object):
    def __init__(self,n):
        W = []
        for w in range(n):
            self.W = random.random()
        b = random.random()
    def forword(self,x):
        return np.dot(x,self.W)+self.b

