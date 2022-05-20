my_name = "Efe Bayrakceken"
my_id = "210102002026"
my_email = "e.bayrakceken2021@gtu.edu.tr"

def problem1(x, y):
    out=[]
    for i in x:
        if x.count(i)==y:
            out.append(i)
    return out

def problem2(x):
    if len(x)<=0:
        return 0
    values=list(x.values())
    values.sort()
    if len(values)%2!=0:
        return values[int(len(values)/2)]
    else:
        return (values[int(len(values)/2)]+values[(int(len(values)/2)-1)])/2
    
def problem3(file):
    try:
        x=open(file, "r")
    except FileNotFoundError:
        return []
    out=[]
    for i in x:
        list1 = i.strip().split(",")
        out.append({"name":list1[0], "credit":int(list1[1]), "term":int(list1[2]), "grade":list1[3].strip()})
        if out[-1]["grade"]=="": 
            out[-1]["grade"]="NA"
    x.close()
    return out

def problem4(x, y):
    gradelist={"AA":4.0, "BA":3.5, "BB":3.0, "CB":2.5, "CC":2.0, "DC":1.5, "DD":1.0, "FF":0.0, "NA":None}
    points=0
    credit=0
    for i in x:
        if i["term"]==y and i["grade"]!="NA":
            credit +=i["credit"] 
            points += i["credit"] * gradelist[i["grade"]]
    return int((points/credit)*100)/100 if credit!=0 else 0

# def testfunc(x):
    # return str(list(range(x+1))).count("1")

def problem5(ffunc, x):
    return ffunc(x)==str(list(range(x+1))).count("1")
    

def problem6(x):
    x = x.lower()        
    def permutations(iterable, r=None):
        pool = tuple(iterable)
        n = len(pool)
        r = n if r is None else r
        if r > n:
            return
        indices = list(range(n))
        cycles = list(range(n, n-r, -1))
        yield list(pool[i] for i in indices[:r])
        while n:
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    yield list(pool[i] for i in indices[:r])
                    break
            else:
                return
    a=[]
    test=[]
    for i in range(1 , len(x)+1):
        test=list(permutations(x, i))
        a.extend(test)
    a= list(map(''.join, a))
    a.sort()
    a = list(dict.fromkeys(a))
    return a
        

def problem7(x, word):
    lst1=problem6(x)
    lst_out=[]
    word=open(word)
    for j in word:
        for i in lst1:
            if i==j.strip("\n"):
                lst_out.append(i)
    word.close()
    return lst_out

def problem8(board, check):
    x, y= 0, 0
    if len(check[0])>len(board[0]) or len(check)>len(board):
        return False

    for i in board:
         for j in i:
             if j==check[0][0]:
                 y=board.index(i)
                 x=i.index(j)
    
    for i in range(len(check)):
        for j in range(len(check[0])):
            if check[i][j]!=board[y+i][j+x]:
                return False
    return True

def problem9(x):
    compressed=""
    prev=""
    count=1
    for i in x:
        if i != prev:
            if count > 1:
                compressed+=str(count)
            compressed+=i
            count=1
        else:
            count+=1
        prev=i
    if count>1:
        compressed+=str(count)        
    return compressed, int(100-(100*len(compressed)/len(x)))
        

def problem10(x):
    x.sort()
    lst1=list(range(x[0], x[-1]+1))
    print(lst1)
    if lst1==x:
        return x[-1]+1
    for i in x:
        lst1.remove(i)
    return lst1[0]
