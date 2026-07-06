# Problem 2: Employee Impotance(https://leetcode.com/problems/employee-importance/)
#Time Complexity: O(N), where N is the number of employees, because we visit each employee exactly once during the map building step and exactly once during the DFS step.
#Space Complexity: O(N), because we store every employee in the map and in the worst case the recursion stack can go as deep as N if the hierarchy is a long chain.
#Approach: We first build a map that connects each employee id to their actual employee object, since the subordinates list only gives us ids and not the full object. Then we use DFS starting from the given id, adding up the importance value of every employee we visit, including the starting employee and all their direct and indirect subordinates. The recursion naturally keeps going deeper until there are no more subordinates left to explore.


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # this map will let us jump from an employee id straight to the actual employee object
        # we need this because subordinates are stored as plain ids, not as objects we can use directly
        self.map = {}

        # we loop through every employee once and store them in the map using their id as the key
        # this way later on we can look up any employee in constant time instead of searching the whole list again
        for emp in employees:
            self.map[emp.id] = emp

        # this will hold the running total of importance as we visit employees
        self.result = 0

        # we start the depth first search from the given id
        # this call will handle adding importance for this employee and all their subordinates
        self.dfs(id)
        return self.result

    def dfs(self, id):
        # we look up the actual employee object for this id using our map
        # this is fast because the map gives us direct access instead of searching
        emp = self.map[id]

        # we add this employee's own importance value to the running total
        # this happens for the starting employee and every subordinate we visit along the way
        self.result += emp.importance

        # now we go through each subordinate id that belongs to this employee
        for subid in emp.subordinates:
            # we call dfs again on this subordinate
            # this is what lets us reach not just direct subordinates but also their subordinates and so on
            # the recursion keeps going deeper until it reaches an employee with no subordinates left
            self.dfs(subid)
