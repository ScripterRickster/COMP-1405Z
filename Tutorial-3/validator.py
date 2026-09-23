# Made By Ricky L.


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

def isvalid(str):
    if str == None: return

    chars = list(str.strip())

    stack = []

    open = ["(", "{", "["]
    close = [")", "}", "]"]

    for char in chars:
        if char in open:
            push(stack, char)
        elif char in close:
            if isempty(stack): return False

            last = peek(stack)

            if open.index(last) != close.index(char):
                return False

            pop(stack)

    return isempty(stack)
