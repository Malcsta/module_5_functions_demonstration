"""
Description: Module 05 demonstration: Functions
Author: Malcolm White
Date: 2023-10-23
Usage: To run individual functions, place a function 
call within the main guard.
"""

def greet() -> None:
    """
    Prints a greeting message to the console.
    Args:
        None
    Returns:
        None
    """
    print('Hello World!')


def greet_name_age(name: str, age: int) -> str:
    """
    This function prints a greeting which includes the values of the name 
    and age parameters.
    Args:
        name (str): The name of the person being greeted.
        age (int): The age of the person being greeted.
    Returns:
        None
    """
    print(f"Hello {name} you are {age} years old.")


def math_operation(operand_1: int, operand_2: int, operator: str) -> float:
    """
    This function returns the specified math operation based on the values
    of the two operands.
    Args:
        operand_1: (int) represents the left side of the operation
        operand_2: (int) represents the right side of the operation
        operator: (str) the operation to perform
    Returns:
        float: The result of the operation.
    Raises: 
        ValueError: When operator is not a + or -
            "Invalid operation, must be plus or minus."
    
    """
    if operator == '+':
        result = operand_1 + operand_2
    elif operator == '-':
        result = operand_1 - operand_2
    else:
        raise ValueError('Invalid operation, must be plus or minus.')


    return(float(result))


result = math_operation(1,3,'+') #4
print(result)


try:
    print(math_operation(6,10,'-')) # -4
except ValueError as e:
    print(e)

try:
    print(math_operation(6,10,'*')) # -4
except ValueError as e:
    print(e)



print('end of file')
print(math_operation.__doc__)


