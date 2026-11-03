class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        l = 0
        cnt = 0
        students = deque(students)
        sandwiches = deque(sandwiches)
        while True:
            if len(students) == cnt:
                return len(students)
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                cnt = 0
            else:
                cnt+= 1
                s = students.popleft()
                students.append(s)
