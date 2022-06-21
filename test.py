# import cv2

# cv2.namedWindow("image", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("image",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

# img = cv2.imread("Main_Menu.png")

# cv2.putText(img, "Categories:", (30, 278), cv2.FONT_HERSHEY_SIMPLEX,1,(150,100,255),4)
# cv2.rectangle(img, (230, 250), (445, 285), (255, 255, 0), -1, cv2.LINE_AA)
# cv2.putText(img, "LANDMARKS", (250, 278), cv2.FONT_HERSHEY_SIMPLEX,1,(150,100,160),4)
# cv2.rectangle(img, (230, 310), (375, 345), (255, 255, 0), -1, cv2.LINE_AA)
# cv2.putText(img, "GAMES", (250, 338), cv2.FONT_HERSHEY_SIMPLEX,1,(150,100,160),4)
# cv2.rectangle(img, (230, 370), (500, 405), (255, 255, 0), -1, cv2.LINE_AA)
# cv2.putText(img, "PERSONALITIES", (250, 398), cv2.FONT_HERSHEY_SIMPLEX,1,(150,100,160),4)

# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

words = []

my_file = open("Games.txt", "r")
data = my_file.read()
words = data.split("\n")
words = list(map(lambda x: x.upper(), words))
my_file.close()

print(words)
Words = dict()
for x in words:
    x = x.split(':')
    Words[x[0]] = x[1]

print(Words)