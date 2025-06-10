from Stack import Stack

def isValidExpression(expression):
    
    stack = Stack(100)

    for char in expression:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty():
                return False
            else:
                last_out = stack.pop()
                if (char == "}" and last_out != "{") or \
                   (char == "]" and last_out != "[") or \
                   (char == ")" and last_out != "(") :      
                    return False
    
    return stack.is_empty()

# Example usage
expr = input("Enter an expression: ")
if (isValidExpression(expr)):
    print("Balanced")
else:
    print("Not balanced")