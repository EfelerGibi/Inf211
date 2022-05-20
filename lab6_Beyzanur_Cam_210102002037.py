my_name = "Beyzanur Cam"
my_id = "210102002037"
my_email = "b.cam2021@gtu.edu.tr"

from random import randint

def problem1():
    class p1:
        
        def __init__(self, x):
            if type(x) is int:
                self.a=x
            else:
                self.a=0
            
        def get_value(self):
            if type(self.a) is int:
                return self.a
            else:
                return 0
            
        def set_value(self, x):
            if type(x) is int:
                self.a=x
                return self.a
            else:
                pass
    return p1


def problem2():
    class p2:
        
        def __init__(self,x,y):
            self.a=x
            self.b=y
        
        def get_area(self):
            return self.a*self.b
        
        def get_perimeter(self):
            return 2*(self.a+self.b)
    return p2

def problem3():
    class Grades:
        
        def __init__(self, l=[]):
            self.l=l
            
            
        def add_grade(self,x):
            self.l.append(x)
            return self.l
        
        def remove_grade(self, x):
            try:
                return self.l.remove(x)
            except:
                pass
        
        def get_min(self):
            return min(self.l) if len(self.l)>0 else 0.0
        
        def get_max(self):
            return max(self.l) if len(self.l)>0 else 0.0
        
        def get_mean(self):
            try:
                return sum(self.l)/len(self.l)
            except ZeroDivisionError:
                return 0.0
            
        def get_median(self):
            if len(self.l)==0:
                return 0.0
            elif len(self.l)%2==0:
                return (self.l[(int(len(self.l)/2))] + self.l[int(len(self.l)/2)-1])/2
            else:
                return self.l[int(len((self.l))/2)]
    
    return Grades

def problem4():
    class Movie:
        
        def __init__(self, movie_name, director, year, rating=0, length=0):
            self.m= movie_name
            self.d= director 
            self.y= year
            if rating <= 10.0 and rating >= 0.0:
                self.r= rating
            else:
                self.r=0
            
            if length <= 500 and length >= 0:
                self.l= length
            else:
                self.l=0    
            
            
        def get_movie_name(self):
            return self.m
            
            
        def get_director(self):
            return self.d
            
        def get_year(self):
            return self.y

        def get_rating(self):
            return self.r
            
        def get_lenght(self, l):
            self.l= l
            
        def set_rating(self, x):
            if x <= 10.0 and x >= 0.0:
                self.r= x
            else:
                pass
            
        def set_length(self, y):
            if y <= 500 and y >= 0:
                self.l= y
            else:
                pass
    return Movie

def problem5():
    
    class MovieCatalog:
        def __init__(self, filename):
            self.ml=[]
            x=open(filename)
            for i in x:
                y=i.strip("\n").split(",")
                self.ml.append(problem4()(y[0],y[1],int(y[2]),float(y[3]),int(y[4])))
                               
        def add_movie(self, movie_name, director, year, rating=0.0, length=0):
            new=problem4()(movie_name, director, year, rating, length)
            if new not in self.ml:
                self.ml.append(new)
            else:
                pass
            
        def remove_movie(self, movie_name):
            for i in self.ml:
                if i.m== movie_name:
                    self.ml.remove(i)
        
        def get_oldest(self):
            oldest=self.ml[0]
            for i in self.ml:
                if i.y < oldest.y:
                    oldest=i
            return oldest.m
        
        def get_lowest_ranking(self):
            lrating=self.ml[0]
            for i in self.ml:
                if i.r < lrating.r:
                    lrating=i
            return lrating.m
        
        def get_highest_ranking(self):
            hrating=self.ml[0]
            for i in self.ml:
                if i.r > hrating.r:
                    hrating=i
            return hrating.m
            
        def get_by_director(self,director):
            l1=[]
            for i in self.ml:
                if i.d == director:
                    l1.append(i.m)
            return l1
    
    return MovieCatalog
        
def problem6():
    
    class Node:
        
        def __init__(self ,x,y,z):
            self.x=x
            self.y=y
            self.z=z
            
        def get_node(self):
            return (self.x, self.y, self.z)
        
        def get_distance(self):
            return (self.x**2+self.y**2+ self.z**2)**0.5
        
        def __add__(self, other):
            return Node((self.x+other.x),(self.y+other.y),(self.z+other.z))
        
        def __str__(self):
            return "<"+str(self.x)+", "+str(self.y)+", "+str(self.z)+">"
        
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
            if self.get_node()==other.get_node():
                return True
            else:
                return False
                
    return Node

def problem7():
    
    class NodeCloud:
        def __init__(self, n):
            self.nc=[]
            for i in range(n):
                self.nc.append(problem6()(randint(-20, 20),randint(-20, 20),randint(-20, 20)))
             
        def get_nodes(self):
            l2=[]
            for i in self.nc:
                l2.append(i.get_node())
            return l2
        
        def get_outermost(self):
            enb= self.nc[0]
            for i in self.nc:
                if i>enb:
                    i==enb
            return enb.get_node()
        
        def add_node(self, x,y,z):
            nn=problem6()(x,y,z)
            if nn not in self.nc:
                self.nc.append(nn)
        
        def get_sum(self):
            top=problem6()(0,0,0)
            for i in self.nc:
                top+=i
            return top
        
    return NodeCloud

def problem8():
    
    class Encoder:
        
        def __init__(self, x):
            aa=""
            az=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',"0", "1", "2","3","4", "5","6","7","8","9"]
            for i in x:
                if i in az:
                    aa+=i
            self.st= aa
            
        def __str__(self):
            return self.st
                    
        def morse(self):
            l3=[]
            
            mm={ 'A':'.-', 'B':'-...',
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
            for i in self.st:
                l3.append(mm[i.upper()])
            return l3
        
        def binary(self):
            l4=""
            for i in self.st:
                l4+='{:b}'.format(ord(i))
            return l4
        
        def hex(self):
            l5=""
            for i in self.st:
                l5+='{:x}'.format(ord(i))
            return l5
        
    return Encoder
                


                
                
            
        
        
        
        
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        