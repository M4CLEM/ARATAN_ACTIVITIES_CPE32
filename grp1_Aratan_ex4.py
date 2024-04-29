Score = float(input("Enter your Score: "))
print(f"Your Score is: {Score}")

if Score >= 90 and Score <= 100:
    print("Your Grade is A")
elif Score >= 75 and Score <= 89:
    print("Your Grade is B")
elif Score >= 65 and Score <= 74:
    print("Your Grade is C")
else:
    print("Your Grade is F")