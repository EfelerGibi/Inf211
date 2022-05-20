my_name = "Beyzanur Cam"
my_id = "210102002037"
my_email = "b.cam2021@gtu.edu.tr"

import random


def int_hex(number):
  h = format(int(number), 'x')
  return ('0' + h if len(h) % 2 else h).upper()

def generate_random(row,column):
    ımg=[]
    for i in range(row):
        ımg.append([])
        for j in range(column):
            ımg[-1].append({"red":random.randint(0, 255), "green":random.randint(0, 255),"blue":random.randint(0, 255)})
    return ımg

def is_valid(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            if type(img[i][j]["red"])!= int or type(img[i][j]["green"])!= int or type(img[i][j]["blue"])!= int  :
                return False
            if img[i][j]["red"] not in range(0,256) or img[i][j]["green"] not in range(0,256) or img[i][j]["blue"] not in range(0,256):
                return False
    return True

def read_from_file(filename):
    cam = open(filename)
    ımg1=[]
    for i in cam:
        ımg1.append([])
        cam1= i.strip("\n").split(",")
        for j in cam1:
            ımg1[-1].append({"red":int(j[0:2], 16), "green":int(j[2:4], 16),"blue":int(j[4:-1], 16)})
    return ımg1        
    
def write_to_file(img, filename):
    cam = open(filename,"w")
    ab=""
    for i in range(len(img)):
        for j in range(len(img[i])):
            ab+=int_hex(img[i][j]["red"])+int_hex(img[i][j]["green"])+int_hex(img[i][j]["blue"])
            if j+1!=len(img[i]):
                ab+=","
            
        ab+="\n"
    
    cam.write(ab)
    cam.close()

def clear(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i][j]["red"]=0
            img[i][j]["green"]=0
            img[i][j]["blue"]=0

def set_value(img, value, channel="rgb"):
    for i in range(len(img)):
        for j in range(len(img[i])):
            if "r" in channel:
                img[i][j]["red"]=value
            if "g" in channel:
                img[i][j]["green"]=value
            if "b" in channel:
                img[i][j]["blue"]=value
    
def fix(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i][j]["red"]=round(img[i][j]["red"])
            img[i][j]["green"]=round(img[i][j]["green"])
            img[i][j]["blue"]=round(img[i][j]["blue"])
            
            if img[i][j]["red"]<0:
                img[i][j]["red"]=0
            
            if img[i][j]["green"]<0:
                img[i][j]["green"]=0
            
            if img[i][j]["blue"]<0:
                img[i][j]["blue"]=0
                
            
            if img[i][j]["red"]>255:
                img[i][j]["red"]=255
            
            if img[i][j]["green"]>255:
                img[i][j]["green"]=255
            
            if img[i][j]["blue"]>255:
                img[i][j]["blue"]=255
                
def rotate90(img):
    img2=[]
    for k in range(len(img[0])):
        img2.append([])
    for i in range(len(img[0])):
        for j in range(len(img)):
            img2[i].append(img[j][i])
        img2[i].reverse()
    return img2

def rotate180(img):
    return rotate90(rotate90(img))

def rotate270(img):
    return rotate90(rotate90(rotate90(img)))

def mirror_y(img):
    img.reverse()

def mirror_x(img):
    for i in range(len(img)):
        img[i].reverse()
        

def enhance(img, value, channel="rgb"):
    for i in range(len(img)):
        for j in range(len(img[i])):
            if "r" in channel:
                img[i][j]["red"]*=value
            if "g" in channel:
                img[i][j]["green"]*=value
            if "b" in channel:
                img[i][j]["blue"]*=value
    fix(img)
    
def grayscale(img, mode=1):
    av=0
    for i in range(len(img)):
        for j in range(len(img[i])):
            if mode==1:
                av=(img[i][j]["red"]+img[i][j]["green"]+img[i][j]["blue"])/3
                img[i][j]["red"]=av
                img[i][j]["green"]=av
                img[i][j]["blue"]=av
            elif mode==2:
                av=j["red"]* 0.299 + 0.587*j["green"]+0.114* j["blue"]
                img[i][j]["red"]=av
                img[i][j]["green"]=av
                img[i][j]["blue"]=av
            elif mode==3:
                av=j["red"]*0.2126+ 0.7152* j["green"]+ 0.0722* j["blue"]
                img[i][j]["red"]=av
                img[i][j]["green"]=av
                img[i][j]["blue"]=av
            elif mode==4:
                av=j["red"]*0.2627+ + 0.6780 * j["green"]+0.0593 * j["blue"]
                img[i][j]["red"]=av
                img[i][j]["green"]=av
                img[i][j]["blue"]=av


            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    