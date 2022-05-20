my_name = "Efe Bayrakceken"
my_id = "210102002026"
my_email = "e.bayrakceken2021@gtu.edu.tr"

def problem1(x,y):
    if y<0 or len(x)<y+1:
        return None
    return x[y]

def problem2(x,y):
    if len(x)==0 or y<0 or len(x)<y+1:
        return x
    else:
        del x[y]
        return x

def problem3(x, y):
    x.sort(reverse=not y)
    return x

def problem4(x, y):
    count=0
    err=[]
    for i in x:
        if i in y and i not in err:
            count+=1
            err.append(i)
    
    return count

def problem5(x, y):
    f_sum=0
    for i in range(len(x)):
        f_sum += x[i]*y[i]
    f_avg=f_sum/sum(y)

    return f_avg

def problem6(x):
    if len(x)==2:
        if len(x[0])!=len(x[1]):
            return None
        determinant= float(x[0][0]*x[1][1]-x[0][1]*x[1][0])
        return determinant
    elif len(x)==1:
        return float(x[0][0])
    elif len(x)==3:
        if len(x[0])!=len(x[1]) or len(x[1])!=len(x[2]) or len(x[0])!=len(x[2]):
            return None
        determinant=float((x[0][0] * (x[1][1] * x[2][2] - x[2][1] * x[1][2])-x[1][0] * (x[0][1] * x[2][2] - x[2][1] * x[0][2])+x[2][0] * (x[0][1] * x[1][2] - x[1][1] * x[0][2])))
        return determinant
    if len(x)==4:
        if len(x[0])!=len(x[2]) or len(x[1])!=len(x[3]) or len(x[1])!=len(x[0]):
            return None
        determinant=float(x[0][0]*problem6([x[1][1:4], x[2][1:4], x[3][1:4]]) - (x[0][1] * problem6([[x[1][0], x[1][2], x[1][3]], [x[2][0], x[2][2], x[2][3]], [x[3][0], x[3][2], x[3][3]]])) + (x[0][2]*problem6([[x[1][0], x[1][1], x[1][3]],[x[2][0], x[2][1], x[2][3]],[x[3][0], x[3][1], x[3][3]]]))-x[0][3]*problem6([x[1][0:3], x[2][0:3], x[3][0:3]]))
        return determinant
    else:
        return None
    
def problem7(accounts, source, lira, kurus):
    if source<0 or source+1>len(accounts):
        return accounts
    if round(float(accounts[source])-lira-(kurus/100),2)>=0:
        count = -1
        accounts[source]=str(round(float(accounts[source])-lira-(kurus/100),2))
        for i in accounts:
            count+=1
            if float(i)%1!=0:
                accounts[count] = str('%.2f' % float(accounts[count]))
    return accounts

def problem8(accounts, source, destination, lira, kurus, fee=False):
    if source<0 or source+1>len(accounts):
        return accounts
    count = -1
    if fee==True and lira+(kurus/100)<=10:
        fee=0.1
    elif fee==True:
        fee= (lira+(kurus/100))/100
    else:
        fee=0
    if round(float(accounts[source])-lira-(kurus/100),2)-fee>=0:
        accounts[source]=str(round(float(accounts[source])-lira-(kurus/100),2)-fee)
        accounts[destination]=str(round(float(accounts[destination])+lira+(kurus/100),2))
        for i in accounts:
            count+=1
            if float(i)%1!=0:
                accounts[count] = str('%.2f' % float(accounts[count]))
    return accounts
    
    
# def problem9(x):
#     x=list(range(x))
#     x= [i+1 for i in x]
#     newx=[]
#     a=0
#     i=0
#     while len(x)!=1:
#         while i<7:
#             newx.append(x[a])
#             print(newx, i+1)
#             i+=1
#             if a==len(x)-1:
#                 a=-1
            
#             a+=1

#         x.remove(newx[-1])
#         newx.clear()
#         i=0
#         if x[-1]%7==6:
#             a+=1
#         a=a-1
#         if len(x)==2:
#             a=0
#     return x[0]
            
def problem9(x):
    x=list(range(x))
    x= [i+1 for i in x]
    newx=[]
    for _ in range(0, len(x)*7):
        newx.extend(x)
    # print(newx)
    while len(x)!=1:
        # print("x=", x,",", "removed: ",newx[6])
        x.remove(newx[6])
        b=newx[6]
        # print(newx[0:7])
        for _ in range(0,7):
            newx.pop(0)
        while b in newx:
            newx.remove(b)
        # print(newx[0:7])
       
    return x[0]


def problem10(x):
    lst= []
    lst2=[]
    for i in x:
        if i in lst:
            lst2.append(i)
        else:
            lst.append(i)
            
            
    if len(lst2)>0:
        
        return str(lst2[0])
    
    else:
        
        return None