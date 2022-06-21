#Words = ["concatenate", "evaporate", "guide", "long", "anemia", "netherlands", "rastafaranism", "vigor", "tangency", "trapezoid", "abdicate", "aberrant", "abject", "abjure", "abscission", "abscond", "bacchanalian", "banal", "banter", "bawdy", "bedizen", "beneficient", "behemoth", "blandishment", "cacophonous", "callous", "calumny", "capricious", "cartography", "debauchery", "decorum", "defame", "default"]

Words = []

my_file = open("Landmarks.txt", "r")
data = my_file.read()
Words = data.split("\n")
my_file.close()

print(Words)

stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]

import random
import time
s = random.choice(Words)
m = len(s)
l = [0, 1]*m
s1 = "_ "*m
word = ""
for c in s:
    word = word + c + " "
# vowel = ['a', 'e', 'i', 'o', 'u']
# for i in range(m):
#   if s[i] in vowel:
#     s1 = s1[:i] + s[i] + s1[i+1:]
#     l[i] = 1
chances = 0
letters = []
print(stages[6-chances])
print(s1)
while chances<6:
  if s1 == word:
    print("You Won!!!")
    print("Word is:" + s)
    break
  else:
    print("Chances left:" + str(6-chances))
    print("Letters used:")
    print(letters)
    print('\n')
    x = input("Enter the letter:")
    if x not in word:
      chances += 1
      print(stages[6-chances])
      print(s1)
    else:
      l1 = [pos for pos, char in enumerate(word) if char == x]
      temp = 0
      for y in l1:
        if l[y] == 0:
          s1 = s1[:y] + x + s1[y+1:]
          l[y] = 1
          temp = 1
      if temp == 0:
        chances += 1
      print(stages[6-chances])
      print(s1)
    if x not in letters:
       letters.append(x)

if (chances == 6) & (s1!=word):
  print("SORRY, You Lose!!!")
  print("Word was:" + s)
  
print("\n\nTHIS WINDOW WILL CLOSE IN 10 SECONDS")
time.sleep(10)