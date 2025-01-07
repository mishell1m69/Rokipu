"""Here reside all the custom made math functions of the game"""

from math import *

def calcvect(p1,p2):
    """Calculate the vector from p1 to p2

    Args:
        v1 (list [int,int]): first vector
        v2 (list [int,int]): second vector

    Returns:
        list [int,int]: vector v1 to v2
    """
    return [p2[0]-p1[0],p2[1]-p1[1]]


def getnorm(vect):
    """Returns the norm of vect

    Args:
        vect (list [int,int]): the vector you want to get thez norm of

    Returns:
        int: norm of your vector
    """
    return sqrt(vect[0]**2+vect[1]**2)

def normalize(vect,norm=1):
    """Returns a normalized version of vect with its lenght being norm

    ex:
    vect=[5,2] norm=1 -> [1,0.4]
    vect=[-1,2] norm=3 -> [-1.5,3]

    Args:
        vect (list [int,int]): the vector you want to normalize
        norm (list [int,int]): its norm
    
    Returns:
        list [int,int]: a normalized version of your list
    """
    current_norm=getnorm(vect)
    if current_norm==0: return vect
    return [vect[0]*norm/current_norm,vect[1]*norm/current_norm]

def getanglevector(v1,v2):
    """calculates the angle between two vectors, in degrees

    Args:
        v1 (list [int,int]): _description_
        v2 (list [int,int]): _description_

    Returns:
        int: angle between the two vecotrs, in degrees
    """
    return acos( (v1[0]*v2[0]+v1[1]*v2[1]) / (getnorm(v1)*getnorm(v2)) )

def clostestfromlist(val,list,inlistindex=None):
    """finds the closest value to val in list

    Args:
        val (int): the value you want to compare from
        list (list): list of value to compare to

    Returns:
        int: the closest value to val in list
    """

    if inlistindex:
        return min(list[inlistindex],key=lambda x:abs(x-val))
    return min(list,key=lambda x:abs(x-val))