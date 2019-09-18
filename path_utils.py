import numpy as np

def point(p):
    return np.array([p[0], p[1], 1.]).reshape(1, -1)

def collinearity_check(p1, p2, p3, epsilon=1e-6):
    """
    Applies the colinearity test to three points
    """   
    m = np.concatenate((p1, p2, p3), 0)
    det = np.linalg.det(m)
    return abs(det) < epsilon

def prune_path(path):
    """
    Prunes a path by applying the collinearity test
    """
    if path is not None:
        i = 0
        pruned_path = []
        
        while i < len(path):
            if i == 0:
                pruned_path.append(path[i])
            elif i > 1:
                p1 = point(path[i-2])
                p2 = point(path[i-1])
                p3 = point(path[i])
                
                if not collinearity_check(p1, p2, p3) or i == len(path) - 1:
                    pruned_path.append(path[i])   
            i+=1
    else:
        pruned_path = path
        
    return pruned_path