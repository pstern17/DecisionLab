# Import packages.
import cvxpy as cp
import numpy as np

# Generate a random non-trivial linear program.
n = 15
k = 10

S = cp.Variable(n)
X = cp.Variable((n, k), boolean = True)

constraints = []

for i in range(n):
    constraints.append(cp.sum(X[i, :]) >= 1)
for j in range(k):
    constraints.append(S[j] <= cp.sum(X[:, j]))
constraints.append(sum(S) >= 1)

objective = cp.Minimize(sum(S))
problem = cp.Problem(objective, constraints)

problem.solve()

