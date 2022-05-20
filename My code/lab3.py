

def problem1(x):
    if "K" in x:
        return True
    else:
        return False
    
def problem2(x, y ,z ,t):
    return min(x, y, z, t)
    
def problem3(x, y):

    if y%1==0.5 and y>0:
        rndy= y+0.5
    
    elif y%1==0.5 and y<0:
        rndy= y-0.5
    else:
        rndy=round(y)
        
    if x<0 and rndy<x: 
        return int(x)-1
    
    elif x<0:
        return int(x)
    
    elif x>rndy:
        return int(x)
    
    elif x==int(x):
        return int(x)
    
    else: 
        return int(x)+1
    
def problem4(radius , height, pi=3.1415):
        return (radius**2)*height*pi , (radius**2)*pi*height
    
def problem5(radius, height, pi=3.1415):
    if type(radius) not in (float, int) or type(pi) not in (float, int) or type(height) not in (float, int):
        return -1
    else:   
        return (radius**2)*height*pi , (radius**2)*height*pi
        

def problem6(x):
    lst= []
    lst2= []
    str1=""
    for i in x:
        if i in lst:
            lst.remove(i)
            lst2.append(i)
        else:
            lst.append(i)
            
            
    for i in lst:
        if i not in lst2:
            str1 += i
        
    return str1

def problem7(x):
    prev1= ""
    for i in x:
        if i < prev1:
            return False
        else:
            prev1 = i
            
    return True

def problem8(x):
    lst =[]
    for i in x:
        if i in lst:
            return False
        else: 
            lst.append(i)
            
    return True

    
def problem9(row ,column) :
    if row==1 and column==1:
        return 1
    elif column==1 and row>1:
        return 3
    elif row==column and row>1:
        return 2
            
    return problem9(row-1 , column-1) + problem9(row-1 , column)

def problem10(x,y):
    count = 0 
    for i in range(0, min(len(y), len(x))):
        if x[i]==y[i]:
            count+=1

    return count
