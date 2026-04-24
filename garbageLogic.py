def GarbageLogic(int_score):
    if int_score > 90:
        print("Grade:A")
    elif int_score > 70:
        print("Grade:B")
    elif int_score > 50:
        print("Grade:C")
    elif int_score > 40:
        print("Grade:D")
    elif int_score < 40:
        print("Grade:F")
    else:
        print("Garbage value")
        print("commit message: swap.py1")


GarbageLogic(99.99)


