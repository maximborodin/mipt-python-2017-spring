import sys


class Stack:
    def __init__(self, container):
        self.container = container

    def __str__(self):
        result = ''
        for i in self.container:
            result += str(i) + ' '
        result = result[:-1]
        return result

    def __len__(self):
        return len(self.container)

    def push(self, objectToPush):
        self.container.append(objectToPush)

    def pop(self):
        del self.container[-1]

    def top(self):
        return self.container[-1]

exec(sys.stdin.read())
