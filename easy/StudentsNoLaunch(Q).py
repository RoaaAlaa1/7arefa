# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

# The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

# If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
# Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.



            student_queue.append(student_queue.popleft())
    
    return len(student_queue)

def countStudents(students: List[int], sandwiches: List[int]) -> int:
    from collections import deque
    
        if student_queue[0] == sandwich_stack[0]:
            student_queue.popleft()
            sandwich_stack.pop(0)
        else:
            if sandwich_stack[0] not in student_queue:
                break

    student_queue = deque(students)
    sandwich_stack = sandwiches
    
    while student_queue: