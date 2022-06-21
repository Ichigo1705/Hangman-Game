import numpy as np
from utils import *
import cv2

cv2.namedWindow("Hangman", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Hangman",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
tmp = -99

def game(temp):
 words = []
 
 if temp == 1:
  my_file = open("Landmarks.txt", "r")
 elif temp == 2:
  my_file = open("Games.txt", "r")
 elif temp == 3:
  my_file = open("Animals.txt", "r")
 
 data = my_file.read()
 words = data.split("\n")
 words = list(map(lambda x: x.upper(), words))
 my_file.close()

 Words = dict()
 for x in words:
     x = x.split(':')
     Words[x[0]] = x[1]

 word = np.random.choice(list(Words.keys()),1)[0]
 hint = Words[word]

 word1 = ""
 for letter in word:
     if letter == " ":
         word1 += "_"
     else:
         word1 += letter

 m = []
 m_copy = []
 for s in word:
     if s == " ":
         m.append(1)
         m_copy.append(1)
     else:
         m.append(0)
         m_copy.append(0)

 s1 = "_"*len(m)
 s1_copy = ""
 for x in s1:
     s1_copy += x

 canvas = "blank-canvas.png"
 img = get_canvas(canvas)

 char_rects = get_char_coords(word)
 img = draw_blank_rects(word,char_rects,img)
 img = draw_hint(img, hint, temp)

 cv2.imshow("Hangman",img)

 chances = 0
 letters = []

 img_copy = img.copy()

 while True:
     img = img_copy.copy()
     if chances >= 6:
         img = draw_lost(img)
         break
     elif s1 == word1:
         img = draw_won(img)
         break
     else:
         letter = cv2.waitKey(0) & 0xFF
         if letter < 65 or letter > 122 or (letter > 90 and letter < 97):
             img = draw_invalid(img)
             cv2.imshow("Hangman",img)
             continue
         else:
             letter = chr(letter).upper()
         if letter in letters:
             img = draw_reuse(img)
             cv2.imshow("Hangman",img)
             continue
         else:
             letters.append(letter)
             if letter not in word:
                 img = draw_wrong(img,chances)
                 chances += 1
             else:
                 img = draw_right(img)
                 img, m, s1 = displayLetter(img,letter,m,s1,word,char_rects)
                 img_copy, m_copy, s1_copy = displayLetter(img_copy,letter,m_copy, s1_copy,word, char_rects)
    
     img = draw_used_chars(img,letters)
     img = draw_hangman(img,chances)
     img_copy = draw_used_chars(img_copy,letters)
     img_copy = draw_hangman(img_copy,chances)
     cv2.imshow("Hangman",img)

 img = revealWord(word,img,char_rects)
 cv2.imshow("Hangman",img)
#  while cv2.getWindowProperty("Hangman", cv2.WND_PROP_VISIBLE) >= 1:
#      keyCode = cv2.waitKey(wait_time)
#      if (keyCode & 0xFF) == ord("q"):
#          cv2.destroyAllWindows()
#          break
 Last_Page()

def mouse_click(event, x, y, lags, param):
    global tmp
    if event == cv2.EVENT_LBUTTONDOWN:
            if x>230 and x<415 and y>220 and y<260:
                cv2.destroyAllWindows()
            elif x>230 and x<415 and y>100 and y<145:
                game(tmp)
            elif x>160 and x<515 and y>160 and y<200:
                Main_Menu()

def Last_Page():
    cv2.waitKey(5000)
    img = cv2.imread('blank.png')
    cv2.rectangle(img, (230, 100), (415, 145), (0, 255, 0), -1, cv2.LINE_AA)
    cv2.putText(img, "Play Again", (240, 130), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),4)
    cv2.rectangle(img, (160, 160), (515, 200), (0, 255, 0), -1, cv2.LINE_AA)
    cv2.putText(img, "Return To Main Menu", (170, 190), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),4)
    cv2.rectangle(img, (230, 220), (415, 260), (0, 255, 0), -1, cv2.LINE_AA)
    cv2.putText(img, "Quit Game", (240, 250), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),4)

    cv2.imshow("Hangman", img)
    while cv2.getWindowProperty("Hangman", cv2.WND_PROP_VISIBLE) >= 1:
        cv2.setMouseCallback("Hangman", mouse_click)
        cv2.waitKey(0)

def Mouse_Click_2(event, x, y, lags, param):
    global tmp
    if event == cv2.EVENT_LBUTTONDOWN:
        if x>230 and x<445 and y>250 and y<285:
            tmp = 1
            game(1)
        elif x>230 and x<375 and y>310 and y<345:
            tmp = 2
            game(2)
        elif x>230 and x<500 and y>370 and y<405:
            tmp = 3
            game(3)
        elif x>15 and x<108 and y>20 and y<50:
            cv2.destroyAllWindows()


def Main_Menu():
    global tmp
    img = cv2.imread("Main_Menu.png")

    cv2.putText(img, "Categories:", (30, 278), cv2.FONT_HERSHEY_SIMPLEX,1,(150,100,255),4)
    cv2.rectangle(img, (230, 250), (445, 285), (255, 255, 0), -1, cv2.LINE_AA)
    cv2.putText(img, "LANDMARKS", (250, 278), cv2.FONT_HERSHEY_SIMPLEX,1,(150,100,160),4)
    cv2.rectangle(img, (230, 310), (375, 345), (255, 255, 0), -1, cv2.LINE_AA)
    cv2.putText(img, "GAMES", (250, 338), cv2.FONT_HERSHEY_SIMPLEX,1,(150,100,160),4)
    cv2.rectangle(img, (230, 370), (400, 405), (255, 255, 0), -1, cv2.LINE_AA)
    cv2.putText(img, "ANIMALS", (250, 398), cv2.FONT_HERSHEY_SIMPLEX,1,(150,100,160),4)
    cv2.rectangle(img, (15, 20), (108, 50), (0, 100, 200), -1, cv2.LINE_AA)
    cv2.putText(img, "Quit Game", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100,0,0), 2)

    cv2.imshow("Hangman", img)
    while cv2.getWindowProperty("Hangman", cv2.WND_PROP_VISIBLE) >= 1:
        tmp = cv2.setMouseCallback("Hangman", Mouse_Click_2)
        cv2.waitKey(0)

Main_Menu()