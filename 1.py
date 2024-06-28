stack = [1, 2, 3, 5]
new_element = [4]

class Stack:
    def is_empty(self, stack):
        if len(stack) == 0:
            return True
        else:
            return False

    def push(self, stack, new_element):
        stack.extend(new_element)
        print(stack)

    def pop(self, stack):
        stack.pop()
        print(stack)
        return stack[-1]

    def peek(self, stack):
        return stack[-1]

    def size(self, stack):
        return len(stack)



m = Stack()
print(m.is_empty(stack))
m.push(stack, new_element)
print(m.pop(stack))
print(m.peek(stack))
print(m.size(stack))