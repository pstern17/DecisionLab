import cvxpy as cp

# Parameters
num_people = 2
num_slots = 3
availability = [[1,0,1], [0,1,1]]
preference = [[5,0,3], [0,2,1]]
max_meetings = 1
pref_rate = 1
attendance_rate = 1

# Variables
svars = [cp.Variable(boolean=True) for _ in range(num_slots)]
xvars = [[cp.Variable(boolean=True) for _ in range(num_slots)] for _ in range(num_people)]

#Objective

#Preferences
pref = 0
for i in range(num_people):
    for j in range(num_slots):
        pref = pref + availability[i][j] * xvars[i][j] * preference[i][j]

#Availability
attendance = 0 
for j in range(num_slots):
    attendance = attendance + availability[i][j] * xvars[i][j]

objective = cp.Maximize(pref_rate * pref + attendance_rate * attendance)

# Constraints
constraints = []

# There are at most max_meetings meetings
constraints.append(cp.sum(svars) <= max_meetings)

# There is at least one meeting
constraints.append(cp.sum(svars) >= 1)

# If a person is a assigned to a meeting, then the meeting is hosted
for j in range(num_slots):
    num_assigned = 0
    for  i in range(num_people):
        num_assigned += xvars[i][j]
    constraints.append(num_assigned <= svars[j] * 100000)

#A person can only be assigned to a meeting if they are available
for i in range(num_people):
    for j in range(num_slots):
        constraints.append(xvars[i][j] <= availability[i][j])

# Create problem instance
problem = cp.Problem(objective, constraints)

# Solve problem
problem.solve()

# Check solution status
if problem.status == cp.OPTIMAL:
    print("Optimal solution found.")
    # Print solution variables if needed
    # for var in svars:
    #     print(var.value)
else:
    print("Problem status:", problem.status)


