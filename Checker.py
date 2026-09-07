Password Strength Checker - My first Cyber tool
By Griffin-cys | Chuka University | Applied CS

password = input("Enter password to check: ")

length = len(password)
has_number = any(c.isdigit() for c in password)
has_upper = any(c.isupper() for c in password)

score = 0
if length >= 8:
    score += 1
if has_number:
    score += 1
if has_upper:
    score += 1

print(f"\nPassword length: {length}")
if score == 3:
    print("Strength: STRONG - Good job!")
elif score == 2:
    print("Strength: MEDIUM - Add numbers & capital letters")
else:
    print("Strength: WEAK - Too easy to hack")
