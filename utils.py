import cv2
import numpy as np
import sys

def get_canvas(canvas_file):
    img = cv2.imread(canvas_file,1)
    return img

def get_char_coords(word):
    x_coord = 10
    y_coord = 400

    char_ws = []
    char_hs = []

    for i in word:
        char_width, char_height = cv2.getTextSize(i,cv2.FONT_HERSHEY_SIMPLEX,0.7,2)[0]
        char_ws.append(char_width)
        char_hs.append(char_height)

    max_char_h = max(char_hs)
    max_char_w = max(char_ws)

    char_rects = []

    for i in range(len(char_ws)):
        rect_coord = [(x_coord,y_coord-max_char_h),(x_coord+max_char_w,y_coord)]
        char_rects.append(rect_coord)
        x_coord = x_coord + max_char_w

    return char_rects

def draw_blank_rects(word,char_rects,img):

    for i in range(len(char_rects)):
        top_left, bottom_right = char_rects[i]
        if not word[i].isalpha() or ord(word[i]) < 65 or ord(word[i]) > 122 or (ord(word[i]) > 90 and ord(word[i]) < 97):
            cv2.putText(img,word[i],(top_left[0],bottom_right[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            continue
        cv2.rectangle(img,top_left,bottom_right,(0,0,255),thickness=1,lineType = cv2.LINE_8)

    return img

def draw_hint(img,hint,temp):
    x,y = 20,30
    if temp == 1:
      cv2.putText(img,"Location:",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)
    elif temp == 2:
      cv2.putText(img,"Hint:",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)
    elif temp == 3:
      cv2.putText(img,"Scientific Name:",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)
    
    cv2.putText(img,"{}".format(hint),(x,y+30),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)
    return img

def draw_lost(img):
    cv2.putText(img,"YOU LOST",(380,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    return img

def draw_won(img):
    cv2.putText(img,"YOU WON",(380,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    return img

def draw_invalid(img):
    cv2.putText(img,"INVALID INPUT",(300,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    return img

def draw_reuse(img):
    cv2.putText(img,"ALREADY USED",(300,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    return img

def draw_wrong(img,incorrect_attempts):
    cv2.putText(img,"WRONG {}/6".format(incorrect_attempts+1),(380,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    return img

def draw_right(img):
    cv2.putText(img,"RIGHT",(380,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    return img

def displayLetter(img,letter,m,s,word,char_rects):
    l1 = [pos for pos, char in enumerate(word) if char == letter]
    for y in l1:
        if m[y] == 0:
            s = s[:y] + letter + s[y+1:]
            m[y] = 1
            top_left, bottom_right = char_rects[y]
            cv2.putText(img, word[y],(top_left[0],bottom_right[1]),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)
    
    return img, m, s

def draw_used_chars(img,chars_entered):
    cv2.putText(img,"Letters used:",(300,80),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
    y = 120
    x = 350
    count = 0
    for i in chars_entered:
        if count == 10:
           x += 50
           y = 120
        cv2.putText(img,i,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
        y += 20
        count += 1
    return img

def draw_circle(img):
    cv2.circle(img,(190,160),40,(0,0,0),thickness=2,lineType=cv2.LINE_AA)
    return img

def draw_back(img):
    cv2.line(img,(190,200),(190,320),(0,0,0),thickness=2,lineType=cv2.LINE_AA)
    return img

def draw_left_hand(img):
    cv2.line(img,(190,240),(130,200),(0,0,0),thickness=2,lineType=cv2.LINE_AA)
    return img

def draw_right_hand(img):
    cv2.line(img,(190,240),(250,200),(0,0,0),thickness=2,lineType=cv2.LINE_AA)
    return img

def draw_left_leg(img):
    cv2.line(img,(190,320),(130,360),(0,0,0),thickness=2,lineType=cv2.LINE_AA)
    return img

def draw_right_leg(img):
    cv2.line(img,(190,320),(250,360),(0,0,0),thickness=2,lineType=cv2.LINE_AA)
    return img

def draw_hangman(img,num_tries):
    if num_tries==1:
        return draw_circle(img)
    elif num_tries==2:
        return draw_back(img)
    elif num_tries==3:
        return draw_left_hand(img)
    elif num_tries==4:
        return draw_right_hand(img)
    elif num_tries==5:
        return draw_left_leg(img)
    elif num_tries==6:
        return draw_right_leg(img)
    else:
        return img

def revealWord(word,img,char_rects):
    for i in range(len(word)):
        top_left, bottom_right = char_rects[i]
        cv2.putText(img,word[i],(top_left[0],bottom_right[1]),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    return img