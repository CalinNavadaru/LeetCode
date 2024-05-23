from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
                counter = 0
            else:
                first_element = students.pop(0)
                students.append(first_element)
                counter += 1
                if counter == len(students):
                    break

        return len(students)

