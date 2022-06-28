from stack import Stack

def reverse_string(stack, input):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str

stack = Stack()
input_str = "123"
print(reverse_string(stack, input_str))