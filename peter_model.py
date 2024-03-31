import cvxpy as cp

# Number of people and number of slots
num_slots = 4
num_people = 5
availability = [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

# Create the variables
svars = [cp.Variable(boolean = True) for i in range(num_slots)]
xvars = [cp.Variable(boolean = True) for j in range(num_people * num_slots)]

# Create the objective
objective = cp.Minimize(cp.sum(svars))

# Create the constraints
constr = [cp.sum(svars) >= 1]

# Ensure that each person is assigned to at least one slot
for i in range(num_people):
    constr.append(cp.sum([xvars[j*num_people + i] for j in range(num_slots)]) >= 1)

# Ensure that meetings are hosted such that each person is assigned to a meeting
for i in range(num_people):
    constr.append(cp.sum([availability[j*num_people + i] * xvars[j*num_people + i] for j in range(num_slots)]) >= 1)

# Create the problem
problem = cp.Problem(objective, constr)
problem.solve()

# Retrieve results
print("Optimal values of svars:", [svar.value for svar in svars])