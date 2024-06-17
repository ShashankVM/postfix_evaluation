def evaluate_postfix_inverse(expression):
    # implement this
 
    stack = []
    operator_set = ("+", "-", "*", "/")
    for char in expression.split(' '):
        if char in operator_set:
            first_elem = stack.pop()
            second_elem = stack.pop()
            if char == "+":
                stack.append(first_elem + second_elem)
            elif char == "-":
                stack.append(first_elem - second_elem)
            elif char == "*":
                stack.append(first_elem * second_elem)
            elif char == "/":
                stack.append(first_elem / second_elem)
        elif char.isdigit():
            stack.append(int(char))      
        else:
            pass   
    return stack[-1]      

    

print(evaluate_postfix_inverse("2 3 -"))  # Expected output: 1
print(evaluate_postfix_inverse("2 3 +"))  # Expected output: 5
print(evaluate_postfix_inverse("6 3 *"))  # Expected output: 18
