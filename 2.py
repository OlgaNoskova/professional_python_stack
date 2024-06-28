class Stack:
    def __init__(self):
        self.list = []

    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def push(self, new_element):
        self.list.extend(new_element)

    def pop(self):
        if len(self.list) > 0:
            self.list.pop()
            if len(self.list) > 0:
                return self.list[-1]

    def peek(self):
        if len(self.list) > 0:
            return self.list[-1]

    def size(self):
        return len(self.list)

def brackets_balance(string):

    stack = Stack()
    for i in range(len(string)):
        brackets_open = ['(', '[', '{']
        if string[i] in brackets_open:
            stack.push(string[i])
        brackets_close = [')', ']', '}']
        if string[i] in brackets_close:
            if string[i] == ')' and stack.peek() == '(':
                stack.pop()
            elif string[i] == ']' and  stack.peek() == '[':
                stack.pop()
            elif  string[i] == '}' and stack.peek() == '{':
                stack.pop()
            else:
                return f'несбалансированна'
    if stack.size() == 0:
        return f'сбалансированна'
    else:
        return f'несбалансированна'


if __name__ == '__main__':
    brackets_1 = brackets_balance('[[{())}]')
    brackets_list = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
    for brackets in brackets_list:
        result = (brackets_balance(brackets))
        print(f'Строка {brackets} {result}.')

