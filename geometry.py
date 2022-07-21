# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 12:56:26 2021

@author: Julien
"""

import numpy as np
import matplotlib.pyplot as plt

class Point :
    
    def __init__(self, *coords):
        self.coords = coords
        self.dim = len(coords)
    
    def length(self):
        return np.sqrt(np.sum(np.array([a**2 for a in self.coords])))
    
    def dist(self, P2):
        return (P2-self).length()
    
    def __mul__(self, P2):
        return np.sum(np.array([a*b for a,b in zip(self.coords, P2.coords)]))
    
    def __sub__(self, P2):
        return Point(*tuple([a-b for a,b in zip(self.coords, P2.coords)]))
    
    def __add__(self, P2):
        return Point(*tuple([a+b for a,b in zip(self.coords, P2.coords)]))
    
    def __neg__(self):
        return Point(*tuple([-a for a in self.coords]))
    
    def scalar_mul(self, l):
        return Point(*tuple([a*l for a in self.coords]))
    
    def __str__(self):
        S = "Point("
        for c in self.coords :
            S+= f"{c},"
        return S[:-1]+")"
    

class Angle :
    
    def __init__(self, A, B, C):
        self.points = A,B,C
        BA = B-A
        BA = BA.scalar_mul(1/BA.length())
        BC = B-C
        BC = BC.scalar_mul(1/BC.length())
        self.unit_vect = BA, BC
        self.value = np.arccos((BA*BC))
    
    def __str__(self):
        Pstr = ""
        for p in self.points :
            Pstr += f"{str(p)[5:]},"
        return f"Angle(Points=({Pstr[:-1]}), value={self.value})"
        

class Polygon :
    
    def __init__(self, *Vertices):
        try :
            n = Vertices[0].dim
            for v in Vertices :
                if not 1 < v.dim < 4 :
                    raise(ValueError("Polygon can only be 2D or 3D object"))
                elif v.dim!=n :
                    raise(ValueError("All vertices must be of same dimention"))
        except ValueError as ve :
            raise ve
        
        self.points = Vertices
        n = len(self.points)
        self.dim = Vertices[0].dim
        
        self.edges = []
        for i in range(n):
            for v in self.points[:i] :
                self.edges.append((self.points[i], v))
        
        self.angles = []
        for i in range(n):
            self.angles.append(Angle(self.points[(i-1) % n],self.points[i%n],self.points[(i+1)%n]))
    
    def __str__(self):
        Pstr = ""
        for p in self.points :
            Pstr += f"{str(p)[5:]},"
        return f"Polygon(Points=({Pstr[:-1]}))"
    
    def __angles__(self):
        Astr = ""
        for a in self.angles :
            Astr += f"{str(a)[5:]},"
        return f"Polygon(Angles=({Astr[:-1]}))"
    
    def plot(self, ax=None):
        if ax==None :
            fig,ax = plt.subplots()
        
        X = [p.coords[0] for p in self.points]+[self.points[0].coords[0]]
        Y = [p.coords[1] for p in self.points]+[self.points[0].coords[1]]
        
        if self.dim == 2 :
            ax.plot(X,Y)
        elif self.dim == 3 :
            Z = [p.coords[2] for p in self.points]+[self.points[0].coords[2]]
            ax.plot(X,Y,Z)
        ax.axis('equal')

def from_value(D, value):
    for k,v in D.items():
        if v==value :
            return k
    return None

class Triangle(Polygon):
    
    def __init__(self, A, B, C):
        super().__init__(A,B,C)
        self.properties = {}
        self.properties['isoceles'] = False
        self.properties['rectangle'] = False
        self.properties['equilateral'] = False
        
        L = np.array([e[0].dist(e[1]) for e in self.edges])
        V, C = np.unique(L, return_counts=True)
        if max(C) >= 2 :
            self.properties['isoceles'] = True
        
        for a in self.angles :
            if a.value == np.pi/2 :
                self.properties['rectangle'] = True
                break
            elif a.value == np.pi/3 :
                self.properties['equilateral'] = self.properties['isoceles']

if __name__ == '__main__' :
    fig, ax = plt.subplots(2,2, figsize=(10,7))
    
    T1 = Triangle(Point(0, 0),Point(1, 2), Point(1, 0))
    T2 = Triangle(Point(0, 0),Point(0.5, 2), Point(1, 0))
    T3 = Triangle(Point(0, 0),Point(np.cos(np.pi/3), np.sin(np.pi/3)), Point(1, 0))
    T4 = Triangle(Point(0, 0),Point(1, 1), Point(1, 0))
    
    T1.plot(ax[0,0])
    ax[0,0].set_title(", ".join([k for k,v in T1.properties.items() if v]))
    T2.plot(ax[0,1])
    ax[0,1].set_title(", ".join([k for k,v in T2.properties.items() if v]))
    T3.plot(ax[1,0])
    ax[1,0].set_title(", ".join([k for k,v in T3.properties.items() if v]))
    T4.plot(ax[1,1])
    ax[1,1].set_title(", ".join([k for k,v in T4.properties.items() if v]))
    
                




















