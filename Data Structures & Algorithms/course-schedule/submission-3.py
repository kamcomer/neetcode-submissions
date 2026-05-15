class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursePrereqs = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            coursePrereqs[course].append(prereq)

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



