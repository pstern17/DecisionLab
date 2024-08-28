import cvxpy as cp

# Parameters
num_people = 2
num_slots = 3
availability = [[1,0,1], [1,0,1]]
preference = [[5,0,1], [4,0,5]]
max_meetings = 4
pref_rate = 1
possible_prefs = [0.001, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5]
max_per_meeting = 2
min_per_meeting = 1

def solve_model(max_meetings):
    # Variables
    svars = [cp.Variable(boolean=True) for _ in range(num_slots)]
    xvars = [[cp.Variable(boolean=True) for _ in range(num_slots)] for _ in range(num_people)]

    # Objective

    # Preferences
    pref = 0
    for i in range(num_people):
        for j in range(num_slots):
            pref = possible_prefs[pref_rate] + availability[i][j] * xvars[i][j] * preference[i][j]

    # Availability
    attendance = 0 
    for j in range(num_slots):
        attendance = attendance + availability[i][j] * xvars[i][j]

    objective = cp.Maximize(pref_rate * pref + attendance)

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

    # A person can only be assigned to a meeting if they are available
    for i in range(num_people):
        for j in range(num_slots):
            constraints.append(xvars[i][j] <= availability[i][j])


    # Assign each person to at most one meeting
    for i in range(num_people):
        meetings = 0 
        for j in range(num_slots):
            meetings += xvars[i][j]
        constraints.append(meetings <= 1)

    # Each meeting has at least min_per_meeting people
    for j in range(num_slots):
        people = 0
        for i in range(num_people):
            people += xvars[i][j]
        constraints.append(people >= min_per_meeting * svars[j])
        constraints.append(people <= max_per_meeting * svars[j])


    # Each meeting has at most max_per_meeting people

    # Create problem instance
    problem = cp.Problem(objective, constraints)

    # Solve problem
    problem.solve()

    # Check solution status
    if problem.status == cp.OPTIMAL:
        print("Number of meetings: ", max_meetings)
        # Print solution variables if needed
        print(svars)
        for var in svars:
            print(var.value)
        #print(xvars)
        #for var in xvars:
        #    for term in var:
        #        print(term.value)
    else:
        print("No possible meetings of this structure", problem.status)


while max_meetings > 0:
    solve_model(max_meetings)
    max_meetings -= 1