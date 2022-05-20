
def problem1(): #returns my name
    return "Hi all, This is Efe Bayrakceken"

def problem2(): #returns some input
    u_input1 = input("Enter some input: ")
    return f"Input was {u_input1}"

def problem3(): #takes the sum of two numbers
    u_input_int1 = int(input("Enter first number: "))
    u_input_int2 = int(input("Enter second number: "))
    
    return u_input_int1+u_input_int2

def problem4(): #subtracts 2 numbers from eachother
    u_input_float1 = float(input("Enter first number: " ))
    u_input_float2 = float(input("Enter second number: " ))
    
    return u_input_float1-u_input_float2

def problem5(): #takes a modulo
    u_input_modulo1 = int(input("Enter first number: "))
    u_input_modulo2 = int(input("Enter second number: "))
    
    return u_input_modulo1%u_input_modulo2

def problem6(): #calculates the volume of a cylinder
    pi = 3.141592

    u_input_radius = float(input("Enter radius: "))
    u_input_height =float(input("Enter height: "))
    
    return u_input_radius**2*pi*u_input_height

def problem7(): #calculates the perimeter of a square
    u_input_squareside = float(input("Enter one side: "))
    f_output_squareperimeter = str(u_input_squareside*4)
    
    return f"The perimeter of the square is {f_output_squareperimeter}."
    
