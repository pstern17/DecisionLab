import cvxpy as cp
import numpy as np

# Problem parameters
n = 5  # Number of variables, adjust as needed
C = np.random.randint(0, 2, (n, n))  
K = 3  

# Define decision variables
X = cp.Variable((n, n), integer=True)
S = cp.Variable(n, integer=True)

#Define Objective Function
S = cp.Variable(n, integer = True)
objective = cp.Minimize(cp.sum(S))


#Define Constraints
constraints = []
# Constraint 1: Sum over j s.t. C_ij = 1 (X_ij) >= 1 for all i
for i in range(n):
    constraints += [cp.sum(X[i, j] for j in range(n) if C[i, j] == 1) >= 1]

# Constraint 2: nS_j >= sum from i=1 to n (X_ij) for all j
for j in range(n):
    constraints += [n * S[j] >= cp.sum(X[:, j])]

#Constraint 3: Sum from j=1 to K (S_j) >= 1
constraints.append(cp.sum(S[0:K]) >= 1) 


#Define and Solve Problem
prob = cp.Problem(objective, constraints)
prob.solve()

#Results
print("Status:", prob.status)
print("Values of S_j:", S.value)
print("Values of X_ij:", X.value)
print("Minimum Objective Value:", prob.value)







