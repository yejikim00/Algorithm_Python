# def push(self, X, stack):
#     self.X = X
#     self.stack = stack
#     stack.append(X)
#     return stack
#
# def pop(self, stack):
#     self.stack = stack
#     pop = stack.pop()
#     if pop == None:
#         print(-1)
#     else:
#         print(pop)
#     return stack
#
# def size(self, stack):
#     self.stack = stack
#     size = len(stack)
#     return size
#
# def empty(self, size):
#     self.size = size
#     if size == 0:
#         return 1
#     else:
#         return 0
#
# def top(self, stack):
#     self.stack = stack
#     top = stack.pop()
#     if top == None:
#         print(-1)
#     else:
#         print(top)

N = int(input())
stack = []

for _ in range(N):
    order = input()

    if order == "push":
        X = int(input())
        stack.append(X)
        # continue

    elif order == "pop":
        try:
            pop = stack.pop()
            print(pop)
        except IndexError:
            print(-1)

    elif order == "size":
        size = len(stack)
        print(size)
        # continue

    elif order == "empty":
        size = len(stack)
        if size == 0:
            print(1)
        else:
            print(0)
        # continue

    elif order == "top":
        try:
            top = stack[-1]
            print(top)
        except IndexError:
            print(-1)

