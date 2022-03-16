import time

def squareRootExhaustive(x, epsilon):
   """Assumes x and epsilon are positive floats & epsilon < 1
      Returns a y such that y*y is within epsilon of x"""
   step = epsilon**2
   ans = 0.0
   while abs(ans**2 - x) >= epsilon and ans*ans <= x:
       ans += step
   if ans*ans > x:
      raise ValueError
   return ans

def squareRootBi(x, epsilon):
   """Assumes x and epsilon are positive floats & epsilon < 1
      Returns a y such that y*y is within epsilon of x"""
   low = 0.0
   high = max(1.0, x)
   ans = (high + low)/2.0
   while abs(ans**2 - x) >= epsilon:
      if ans**2 < x:
         low = ans
      else:
         high = ans
      ans = (high + low)/2.0
   return ans

x = 9
epsilon = 0.001

t1 = time.time()
print(squareRootExhaustive(x, epsilon))
t2 = time.time()
print("Exhaustive method runs in {0} seconds".format(t2-t1))

t1 = time.time()
print(squareRootBi(x, epsilon))
t2 = time.time()
print("Bisection method runs in {0} seconds".format(t2-t1))
