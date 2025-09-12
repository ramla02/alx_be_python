def perform_operation(num1, num2, operation):
    
    """
    This program performs a basic  arithmetic operation between num1 and num2.
    """
    
    if type(operation) is not str:
        return "Error: operation must be string"
    op = operation.strip().lower()
    
    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return f"Error: Unknown operation '{operation}'"