__author__ = 'yangfeilong'

Lucky_Num = 6
input_num = -1
while Lucky_Num != input_num:
    input_num = int(input("guess my lucky number:"))
    if input_num > Lucky_Num:
        print("too big. Input a smaller number.")
    elif input_num < Lucky_Num:
        print("too small. Input a bigger number.")

print("Bongo.")
