class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = 0
        while n != len(students):
            if students[0] == sandwiches[0]:
                n = 0
                del students[0]
                del sandwiches[0]
            else:
                n += 1
                k = students.pop(0)
                students.append(k)
        return n