class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if(t == "/"):
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            elif (t == "*"):
                stack.append(stack.pop() * stack.pop())
            elif (t == "+"):
                stack.append(stack.pop() + stack.pop())
            elif (t == "-"):
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            else:
                stack.append(int(t))
        return stack[0]

        