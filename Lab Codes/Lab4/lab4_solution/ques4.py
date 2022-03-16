PI = 3.14159

def area(radius):
    """Area of circle
    """
    return PI*(radius**2)

def sphereSurface(radius):
    """Surface of sphere
    """
    return 4.0*area(radius)

def sphereVolume(radius):
    """Volume of sphere
    """
    return (4.0/3.0)*PI*(radius**3)

#radius = 5
#print(sphereSurface(radius))
#print(sphereVolume(radius))
