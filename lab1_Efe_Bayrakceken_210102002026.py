my_name = "Efe Bayrakceken"
my_id = "210102002026"
my_email = "e.bayrakceken2021@gtu.edu.tr"

def problem1():
    return my_name[0]

def problem2():
    u_input_chno= int(input("Enter a number: "))
    f_charno= u_input_chno%len(my_name)
    return my_name[f_charno]

def problem3():
    u_input_rno1=int(input("Enter first number: "))
    u_input_rno2=int(input("Enter second number: "))
    f_rno1= u_input_rno1%len(my_name)
    f_rno2= u_input_rno2%len(my_name)
    if f_rno1<= f_rno2: 
        return my_name[f_rno1:f_rno2+1]
    else:
        return my_name[f_rno2:f_rno1+1]

def problem4():
    Vowels="aeiouAEIOU"
    u_input_str1=input("Enter input: ")
    f_count = 0
    for i in range(0, len(u_input_str1)):
        if u_input_str1[i] in Vowels:
            f_count += 1
    return f_count

def problem5():
    f_sumno=0
    for i in my_id:
        f_sumno += int(i)
    
    return f_sumno

def problem6():
    u_input_factor=int(input("Enter input: "))
    f_factorialno= 1
    f_factorial = 1
    while f_factorialno <= u_input_factor:
        f_factorial = f_factorialno*f_factorial
        f_factorialno += 1
        
    return f_factorial
    
def problem7():
    u_input_div= int(input("Enter a number: "))
    f_div= ""
    if u_input_div%21==0:
        f_div= True
    else:
        f_div= False
    
    return f_div

def problem8():
    
    u_input_div2= int(input("Enter a number: "))
    f_div2= ""
    if u_input_div2%21==0:
        f_div2=3
        
    elif u_input_div2%3==0:
        f_div2= 1
        
    elif u_input_div2%7==0:
        f_div2=2
        
    else:
        return
    
    return f_div2

def problem9():
    u_input_prime= int(input("Enter a number: "))
    f_prime=2
    f_prime2=0
    f_prime3=0
    f_prime_out= 0
    
    if u_input_prime>1: 
        while f_prime<= u_input_prime:
            f_prime2 = u_input_prime%f_prime
            if f_prime2 !=0 :
                f_prime+=1
            else:
                f_prime3+=1
                f_prime+=1
    else:
        f_prime3= 2

            
    if f_prime3<=1:
        f_prime_out= True
    else:
        f_prime_out= False
    
    return f_prime_out
    
def problem10():
    u_input_root= float(input("Enter a number: "))
    g = (u_input_root/2.0)
    g2 = g+1
    if u_input_root == 0:
        return 0

    while(g != g2):
        n = u_input_root / g
        g2 = g
        g = (g + n)/2

    return g
