class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursePrereqs = [[] for _ in range(numCourses)]

        for preReq in prerequisites:
            coursePrereqs[preReq[0]].append(preReq[1])

        visited = set()
        def dfs(course):
            if course in visited:
                return False

            if not coursePrereqs[course]:
                return True

            visited.add(course)
            for edge in coursePrereqs[course]:
                if not dfs(edge):
                    return False

            visited.remove(course)
            
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True



