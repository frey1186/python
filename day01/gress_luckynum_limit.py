__author__ = 'yangfeilong'

Lucky_Num = 6
for i in range(3):
    input_num = int(input("guess my lucky number:"))
    if input_num > Lucky_Num:
        print("too big. Input a smaller number.")
    elif input_num < Lucky_Num:
        print("too small. Input a bigger number.")
    else:
        print("Bingo.")
        break
else:
    print("Too many retries.")

