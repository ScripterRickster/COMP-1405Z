# Made By Ricky L.

qsize = 10


def enqueue(queue, value):
    if queue is None or value is None: return False
    if len(queue) >= qsize: return False
    queue.append(value)
    return True

def dequeue(queue):
    if not len(queue) > 0: return None
    val = queue[0]
    queue.pop(0)
    return val

def peek(queue):
    if not queue: return None
    if not len(queue) > 0: return None
    return queue[0]

def isempty(queue):
    return len(queue) == 0

def multienqueue(queue, items):
    if queue is None or not items: return 0
    added = 0
    for i in items:
        if enqueue(queue, i):
            added += 1
        else:
            break
    return added

def multidequeue(queue, number):
    if queue is None or not number: return []
    dqueue = []
    for _ in range(number):
        val = dequeue(queue)
        if val is None:
            break
        dqueue.append(val)
    return dqueue









