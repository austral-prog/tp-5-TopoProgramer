# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    numero = x

    if numero > y : 
        numero = x
    elif numero < y :
        numero = y
    elif numero == y:
        numero = 0
    return numero # Remove this line and implement


def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    numero = x
    if numero>y and numero>z: 
        numero = x
    if y>numero and y>z: 
        numero = y
    if z>y and z>numero: 
        numero = z
    elif numero==y and numero==z and y==z:
        numero = 0
    return numero  # Remove this line and implement

max_of_two(5,4) # Retorna: 5

max_of_two(-2,-3) # Retorna: -2

max_of_two(0,0) # Retorna: 0

max_of_three(5,4,7) # Retorna: 7

max_of_three(-2,-3,-1) # Retorna: -1

max_of_three(0,0,0) # Retorna: 0
