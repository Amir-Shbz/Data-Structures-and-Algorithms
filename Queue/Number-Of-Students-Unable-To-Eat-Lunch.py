# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 
# respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

# The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a 
# stack. At each step:

# If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it 
# and leave the queue.
# Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich 
# in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the 
# initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        circle_lovers = students.count(0)
        square_lovers = students.count(1)  
        
        for sandwich in sandwiches:
            if sandwich == 0:
                if circle_lovers == 0:  
                    return square_lovers
                circle_lovers -= 1
            else:
                if square_lovers == 0:  
                    return circle_lovers
                square_lovers -= 1

        return 0                