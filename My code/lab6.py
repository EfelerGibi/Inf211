

from random import randint

def problem1():
    class p1:
        
        def __init__(self, x):
            if type(x)!= int:
                self.var=0
            else:
                self.var=x
        def get_value(self):
            return self.var
        def set_value(self, x):
            if type(x)!= int:
                pass
            else:
                self.var=x
        def __str__(self):
            return str(self.var)
        
    return p1

def problem2():
    class p1:
        
        def __init__(self, x, y):
            if type(x or y)!=int:
                print("Not an integer")
            else:
                self.w=x
                self.h=y
        
        def get_area(self):
            return self.h*self.w
        
        def get_perimeter(self):
            return 2*(self.h+self.w)
        
    return p1


def problem3():
    class Grades:
        
        def __init__(self):
            self.lst=[]
            self.min=min
            self.max=max
            
        def add_grade(self, x):
            self.lst.append(x)
        
        def remove_grade(self, x):
            try:
                self.lst.remove(x)
            except ValueError:
                pass
        def get_min(self):
            return min(self.lst) if len(self.lst)>0 else 0.0
        
        def get_max(self):
            return max(self.lst) if len(self.lst)>0 else 0.0
        
        def get_mean(self):
            if len(self.lst)<1:
                return 0.0
            avg=0
            for i in self.lst:
                avg+=int(i)
            avg= avg/len(self.lst)
            return avg
        
        def get_median(self):
            if len(self.lst)<1:
                return 0.0
            if len(self.lst)%2==0:
                return (self.lst[int(len(self.lst)/2)]+self.lst[int(len(self.lst)/2)-1])/2
            else:
                return self.lst[int(len(self.lst)/2)]
    return Grades


def problem4():
    class Movie:
        
        def __init__(self, movie_name, director, year, rating=0.0, length=0):
            self.dict1={"movie_name":movie_name , "director":director ,  "year":year}
            if 0.0<=rating<=10:
                self.dict1["rating"]=rating
            else:
                self.dict1["rating"]=0.0
            if 0<=length<=500:
                self.dict1["length"]=length
            else:
                self.dict1["length"]=0
        
        def get_movie_name(self):
            return self.dict1["movie_name"]
        
        def get_director(self):
            return self.dict1["director"]
        
        def get_year(self):
            return self.dict1["year"]
        
        def get_rating(self):
            return self.dict1["rating"]
        
        def get_length(self):
            return self.dict1["length"]
        
        def set_rating(self, x):
            if 0.0<=x<=10:
                self.dict1["rating"]=x
            else:
                pass
            
        def set_length(self, x):
            if 0<=x<=500:
                self.dict1["length"]=x
            else:
                pass
        def __str__(self):
            return str(self.dict1)
    return Movie

def problem5():
    class MovieCatalog:
        
        def __init__(self, filename):
            file=open(filename)
            self.lst=[]
            for i in file:
                clean=i.strip("\n").split(",")
                self.lst.append(problem4()(clean[0], clean[1], int(clean[2]), float(clean[3]), int(clean[4])))
            file.close()
            
        def add_movie(self, movie_name, director, year, rating=0.0, length=0):
            if problem4()(movie_name, director, year, rating, length) not in self.lst:
                self.lst.append(problem4()(movie_name, director, year, rating, length))
        
        def remove_movie(self, movie_name):
            for i in self.lst:
                if i["movie_name"]==movie_name:
                    self.lst.remove(i)
        
        def get_oldest(self):
            prev=self.lst[0]
            for i in self.lst:
                if i.dict1["year"] < prev.dict1["year"]:
                    prev=i
                    
            return i.dict1["movie_name"]
        
        def get_lowest_ranking(self):
            prev=self.lst[0]
            for i in self.lst:
                if i.dict1["rating"] < prev.dict1["rating"]:
                    prev=i
            return prev.dict1["movie_name"]
        
        def get_highest_ranking(self):
            prev=self.lst[0]
            for i in self.lst:
                if i.dict1["rating"] > prev.dict1["rating"]:
                    prev=i
            return prev.dict1["movie_name"]
        
        def get_by_director(self, director):
            out=[]
            for i in self.lst:
                if i.dict1["director"]==director:
                    out.append(i.dict1["movie_name"])
            return out
    return MovieCatalog

def problem6():
    class Node:
        
        def __init__(self, x, y, z):
            if type(x and y and z)==int:
                self.x=x
                self.y=y
                self.z=z
        
        def get_node(self):
            return self.x, self.y, self.z
        
        def get_distance(self):
            return (self.x**2+self.y**2+self.z**2)**0.5
        
        def __add__(self, other):
            return self.x+ other.x, self.y+ other.y, self.z+ other.z
        
        def __str__(self):
            return "<"+ str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ">"
        
        def __gt__(self, other):
            if self.get_distance()>other.get_distance():
                return True
            else:
                return False
            
        def __ge__(self, other):
            if self.get_distance()>=other.get_distance():
                return True
            else:
                return False
        
        def __lt__(self, other):
            if self.get_distance()<other.get_distance():
                return True
            else:
                return False
        
        def __le__(self, other):
            if self.get_distance()<=other.get_distance():
                return True
            else:
                return False

        def __eq__(self, other):
            if (self.x, self.y, self.z)==(other.x, other.y, other.z):
                return True
            else:
                return False
    return Node

def problem7():
    class NodeCloud:
        
        def __init__(self, n):
            if n>0:
                self.size=n
                self.cords=[]
                for i in range(n):
                    self.cords.append(problem6()(randint(-20, 20), randint(-20,20), randint(-20,20)))
        
        def get_nodes(self):
            ls1=[]
            for i in self.cords:
                ls1.append((i.x, i.y, i.z))
            return ls1
        
        def get_outermost(self):
            prev=self.cords[0]
            for i in self.cords:
                if float((i.x**2+i.y**2+i.z**2)**0.5)>(prev.x**2+prev.y**2+prev.z**2)**0.5:
                    prev=i
                    
            return prev.x, prev.y, prev.z
        
        def add_node(self, x, y, z):
            self.cords.append(problem6()(x, y, z))
        
        def get_sum(self):
            su=problem6()(0,0,0)
            for i in self.cords:
                su.x += i.x
                su.y += i.y
                su.z += i.z 
            return su
    return NodeCloud
        
def problem8():
    class Encoder:
        
        def __init__(self, x):
            self.string=""
            valids=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    "0", "1", "2","3","4", "5","6","7","8","9"]
            for i in x:
                if i in valids:
                    self.string+=i
        
        def __str__(self):
            return self.string
        
        def morse(self):
            mor_dic={ 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
        
            mor=[]
            for i in self.string:
                mor.append(mor_dic[i.upper()])
                
            return mor
        
        def binary(self):
            return ''.join(format(ord(x), 'b') for x in self.string)
        
        def hex(self):
            out=""
            for i in self.string:
                out+="{:x}".format(ord(i))
            return out
    return Encoder


