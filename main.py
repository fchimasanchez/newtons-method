# This script demonstrates the use of Newton's Method applied to the function $f(x) = \cos x - x$, and returns
# a zero of the function in the neighborhood of the initial guess. Tolerance for the iteration results is set to
# $10^{-6} = 0.000006$. Algorithm is iterated until the difference in iterations is less than the tolerance

import math

# Whole algorithm fits pretty neatly in one small block
p = 0 # Initial guess for the zero
err = 1 # Set error to artificially high starting point
N = 0 # Number of iterations
while err > 1e-6 or N > 500:
  q = p - (math.cos(p)-p)/(-math.sin(p)-1) # Assuming $f(x) = \cos x - x$ and $f'(x) = -\sin x - 1$
  err = abs(q-p)
  p = q
  N = N + 1
  print("{:.6f}".format(p),"{:.2e}".format(err))
