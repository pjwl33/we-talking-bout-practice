# draw out as graph
# prereq = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
# DFS from course to array with a map
def courseSchedule(numCourse, prereqs) -> bool:
    # preMap = {}
    #
    # for pre in prereqs:
    #     c, p = pre[0], pre[1]
    #     if preMap[c]:
    #         preMap[c].append(p)
    #     else:
    #         preMap[c] = [p]
    preMap = { i:[] for i in range(numCourse)}
    for crs, pre in prereqs:
        preMap[crs].append(pre)

    visited = set()
    def dfs(crs):
        if crs in visited:
            return False # since we already visited, cylcical
        if preMap[crs] == []:
            return True # since it doesn't need prereq

        visited.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre): return False # 1 course can't be completed, then all

        visited.remove(crs)
        preMap[crs] = [] # it can be visited
        return True

    for crs in range(numCourse):
        if not dfs(crs): return False

    return True # O(numCourse + len(prereqs))
