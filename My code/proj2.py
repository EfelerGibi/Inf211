

import random

def generate_random(row, column):
    image=[]
    for _ in range(row):
        image.append([])
        for _ in range(column):
            image[-1].append({"red":random.randint(0, 255), "green":random.randint(0, 255), "blue":random.randint(0, 255)})
    return image

def is_valid(img):
    for i in img:
        for j in i:
            if (j["red"] or j["blue"] or j["green"]) not in range(0, 256):
                return False
    return True

def read_from_file(filename):
    img=[]
    file=open(filename, "r")
    for i in file:
        linelist= i.strip("\n").split(", ") if ", " in i else i.strip("\n").split(",")
        img.append([])
        for j in linelist:
            img[-1].append({"red":int(j[0:2], 16), "green":int(j[2:4], 16), "blue":int(j[4:6], 16)})

    file.close()
    return img

def int_to_hex(number):
  h = format(int(number), 'x')
  return ('0' + h if len(h) % 2 else h).upper()

def write_to_file(img, filename):
    file=open(filename, "w")
    hx=""
    for i in img:
        for j in i:
            hx+=int_to_hex(j["red"])+int_to_hex(j["green"])+int_to_hex(j["blue"])
            hx+=","
        hx=hx.strip(",")+"\n"

    file.write(hx)
    file.close()
    
def clear(img):
    for i in img:
        for j in i:
            j["red"], j["green"], j["blue"]=0,0,0
        
def set_value(img, value, channel="rgb"):
    for i in img:
        for j in i:
            j["red"], j["green"], j["blue"]=(value if "r" in channel else j["red"]),(value if "g" in channel else j["green"]),(value if "b" in channel else j["blue"])
    
def fix(img):
    for i in img:
        for j in i:
            j["red"], j["green"], j["blue"]=(255 if j["red"]>255 else round(j["red"])),(255 if j["green"]>255 else round(j["green"])),(255 if j["blue"]>255 else round(j["blue"]))
            j["red"], j["green"], j["blue"]=(0 if j["red"]<0 else j["red"]),(0 if j["green"]<0 else j["green"]),(0 if j["blue"]<0 else j["blue"])
            
def rotate90(img):
    img_copy=img[:]
    empty=[]
    img_rotated=[]
    for _ in range(len(img[0])):
        img_rotated.append(empty[:])
    
    for i in range(len(img[0])):
        for j in range(len(img)):
            img_rotated[i].append(img_copy[j][i])
        img_rotated[i].reverse()
    # print(img_rotated)
    return img_rotated
        
def rotate180(img):
    return rotate90(rotate90(img))

def rotate270(img):
    return rotate90(rotate180(img))


def mirror_x(img):
    for i in img:
        i.reverse()
        

def mirror_y(img):
       img.reverse()

def enhance(img, value, channel="rgb"):
    fix(img)
    for i in img:
        for j in i:
            j["red"], j["green"], j["blue"]=(j["red"]*value if "r" in channel else j["red"]),(value*j["green"] if "g" in channel else j["green"]),(value*j["blue"] if "b" in channel else j["blue"])
    fix(img)
    
def grayscale(img, mode=1):
    for i in img:
        for j in i:
            if mode==1:
                j["red"], j["green"], j["blue"]= (j["red"]+j["green"]+j["blue"])/3, (j["red"]+j["green"]+j["blue"])/3, (j["red"]+j["green"]+j["blue"])/3
            elif mode==2:
                j["red"], j["green"], j["blue"]= (j["red"]* 0.299 + 0.587*j["green"]+0.114* j["blue"]), (j["red"]* 0.299 + 0.587*j["green"]+0.114* j["blue"]), (j["red"]* 0.299 + 0.587*j["green"]+0.114* j["blue"])
            elif mode==3:
                j["red"], j["green"], j["blue"]= (j["red"]*0.2126+ 0.7152* j["green"]+ 0.0722* j["blue"]), (j["red"]*0.2126+ 0.7152* j["green"]+ 0.0722* j["blue"]), (j["red"]*0.2126+ 0.7152* j["green"]+ 0.0722* j["blue"])
            elif mode==4:
                j["red"], j["green"], j["blue"]= (j["red"]*0.2627+ + 0.6780 * j["green"]+0.0593 * j["blue"]), (j["red"]*0.2627+ + 0.6780 * j["green"]+0.0593 * j["blue"]), (j["red"]*0.2627+ + 0.6780 * j["green"]+0.0593 * j["blue"])
    fix(img)
    
def get_freq(img, channel="rgb", bin_size=16):
    bins={"bin_size":bin_size}
    if "r" in channel: bins["red"]=[0 for i in range(int(256/bin_size))]
    if "g" in channel: bins["green"]=[0 for i in range(int(256/bin_size))]
    if "b" in channel: bins["blue"]=[0 for i in range(int(256/bin_size))]
    ranges=[]
    n=0
    for i in range(int(256/bin_size)):
        ranges.append(list(range(256))[n: n+bin_size])
        n+=bin_size
    print(ranges)
    for i in img:
        for j in i:
            for n in ranges:
                if j["red"] in n and "r" in channel:
                    bins["red"][ranges.index(n)]+=1
                if j["green"] in n and "g" in channel:
                    bins["green"][ranges.index(n)]+=1
                if j["blue"] in n and "b" in channel:
                    bins["blue"][ranges.index(n)]+=1
                    
    return bins
                    
                    

def scale_down(img, N):
    avg_sum_r=0
    avg_sum_g=0
    avg_sum_b=0
    img_copy=[]
    x,y=0,0
    for i in img:
        img_copy.append(i[:])
    n2=N**2
    new_img=[]
    while len(img_copy)%N!=0:
        img_copy.append(img_copy[-1])
    while len(img_copy[-1])%N!=0:
        for i in img_copy:
            i.append(i[-1])
            if len(img_copy[-1])%N==0:
                break
    row=len(img_copy)
    column=len(img_copy[0])
    for i in range(0, row, N):
        new_img.append([])
        for m in range(0, column, N):
            for j in range(N-1):
                for t in range(N-1):
                    avg_sum_r+=img_copy[i+j+y][m+t+x]["red"] 
                    avg_sum_g += img_copy[i+j+y][m+t+x]["green"] 
                    avg_sum_b += img_copy[i+j+y][m+t+x]["blue"]
            avg_sum_r=avg_sum_r/n2
            avg_sum_g=avg_sum_g/n2
            avg_sum_b=avg_sum_b/n2
            new_img[-1].append({"red":avg_sum_r, "green":avg_sum_g , "blue":avg_sum_b})
            avg_sum_r, avg_sum_g, avg_sum_b=0,0,0
    fix(new_img)
    return new_img
            
    
def scale_up(img, N):
    large_board=[]
    for i in img:
        large_board.append([])
        for j in i:
            for _ in range(N):
                large_board[-1].append(j)
        for _ in range(N-1):
            large_board.append(large_board[-1])
    return large_board

def apply_window(img, window): #this might be the best code that i have ever written
    img_copy=[]
    out=[]
    x, y= 1, 1
    avg=[0,0,0]
    for i in img:
        img_copy.append(i[:])
    for i in range(len(img_copy)):
        img_copy[i].append(img_copy[i][-1])
        img_copy[i].insert(0, img_copy[i][0])
    img_copy.append(img_copy[-1])
    img_copy.insert(0, img_copy[0])
    for i in img_copy:
        out.append([])
        for j in i:
            for t in range(0, 3):
                for n in range(0, 3):
                    # print(x-(1-n), "se", x)
                    if x>=len(img_copy[0])-1:
                        break
                    avg[0]+=img_copy[y-(1-t)][x-(1-n)]["red"]*window[t][n]
                    avg[1]+=img_copy[y-(1-t)][x-(1-n)]["green"]*window[t][n]
                    avg[2]+=img_copy[y-(1-t)][x-(1-n)]["blue"]*window[t][n]
                    # print(img_copy[y-(1-t)][x-(1-n)]*window[t][n])

                # if x==len(img_copy[0])-2:
                    # break
            x+=1
            # print("\n")
            
            if x<=len(img_copy[0])-1:
                out[-1].append({"red":avg[0], "green":avg[1], "blue":avg[2]})
            avg=[0,0,0]
        if y>=len(img_copy)-2:
            break
        y+=1
        x=1
    fix(out)
    return out
    
            
