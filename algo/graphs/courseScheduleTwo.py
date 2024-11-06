# if there is cycle - no valid course structurer

# topological sort for graph algo

# adjency list:
# 0: [ 1, 2 ]
# 1: [ 3 ]
# 2: [ ]
# 3: [ 2 ]
# 4: [ 0 ]
# 5: [ 0 ]

def prereqsTwo(numCourses, prereqs):
    # build ajc list of prereqs
    prereq = { c: [] for c in range(numCourses )}
    for crs, pre in prereqs:
        prereq[crs].append(pre)

    # a course has 3 possible states:
    # visited -> crs has een added to output
    # visiting -> crs not added to output, but added to cycle
    # unvisited -> crs not added to output or cycle
    output = []
    visit, cycle = set(), set()

    def dfs(crs):
        if crs in cycle:
            # detected a cycle
            return False
        if crs in visit:
            return True

        cycle.add(crs) # if we see crs again, recursively there is cycle

        for pre in prereq[crs]:
            if dfs(pre) == False: # if False, there is cycle
                return False
        
        cycle.remove(crs)
        visit.add(crs)
        # can only add crs after preqes
        output.append(crs)
        return True
    
    for c in range(numCourses):
        if dfs(c) == False:
            return []
        
    return output