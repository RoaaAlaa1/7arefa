def countStudents(students: List[int], sandwiches: List[int]) -> int:
    from collections import deque
    
    student_queue = deque(students)
    sandwich_stack = sandwiches
    
    while student_queue:
        if student_queue[0] == sandwich_stack[0]:
            student_queue.popleft()
            sandwich_stack.pop(0)
        else:
            if sandwich_stack[0] not in student_queue:
                break
            student_queue.append(student_queue.popleft())
    
    return len(student_queue)