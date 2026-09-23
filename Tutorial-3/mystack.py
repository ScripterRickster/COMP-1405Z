#Made By Ricky L.

def push(stack,value):
    stack.append(value)


def pop(stack):
    if len(stack) == 0: return None

    val = stack[len(stack)-1]

    stack.pop(len(stack)-1)
    return val


def isempty(stack):
    return True if len(stack) == 0 else False

def peek(stack):
    if isempty(stack): return None

    return stack[len(stack)-1]
