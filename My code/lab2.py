
def problem1():
    return (((float(input("Enter Fahrenheit degree: "))) - 32)*5)/9 

def problem2():
    return ((float(input("Enter Celsius degree: "))* 9)/5) + 32

def problem3():
    u_hex= int(input("Enter a number: "))
    return 2*(u_hex**2)-u_hex
    
def problem4():
    u_lucas= int(input("Enter a number: "))
    f_l_prev1=2
    f_l_curr1=1
    for _ in range(u_lucas):
         f_l_prev1, f_l_curr1 =f_l_curr1, f_l_prev1+f_l_curr1
         
    return f_l_prev1

def problem5():
    return input("Enter a string: ")[::-1]

def problem6():
    remove='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    u_input_str1=input("Enter input: ")
    f_str = ""
    for i in range(0, len(u_input_str1)):
        if u_input_str1[i] not in remove:
            f_str += u_input_str1[i]
    return f_str

def problem7():
    u_base=int(input("Enter input: "))
    if u_base>=0:
        s=""
        while True:
            if u_base==0:
                break
            s+=str(u_base%4)
            u_base=u_base//4
        return s[::-1]
    else:
        u_base= -1*u_base
        s=""
        while True:
            if u_base==0:
                break
            s+=str(u_base%4)
            u_base=u_base//4
        return "-"+s[::-1]


def problem8():
    u_bracket=input("Enter input: ")
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []
    if len(u_bracket)%2!=0:
        return False
    for c in u_bracket:
        if c in "{[(":
            stack.append(c)
        elif stack and c == pairs[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0


def problem9():
    u_last=input("Enter input: ")
    f_lastreverse = u_last[::-1]
    f_rev_o= 0
    for i in range(0, len(u_last)):
        if f_lastreverse[i] != " ":
            f_rev_o += 1
            
        else: 
            break
        
    return f_rev_o

def problem10():
    u_direction=input("Enter the exit route:")
    x= 0
    y= 0
    for i in range(0,len(u_direction)):
        
        if u_direction[i] == "s":
            y += -1
        elif u_direction[i] == "w":
            x+= -1
        elif u_direction[i] == "n":
            y += 1
        else:
            x+=1
            
    f_out_ps= x**2+y**2
    
    g = (f_out_ps/2.0)
    g2 = g+1
    if f_out_ps == 0:
        return 0

    while(g != g2):
        n = f_out_ps / g
        g2 = g
        g = (g + n)/2
    
    return g

