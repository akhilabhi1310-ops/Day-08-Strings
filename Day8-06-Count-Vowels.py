text = input("Enter a String: ").lower()
count = 0
for ch in text:
    if ch in "aeiou":
        count += 1
print("Number of Vowels:", count)
print("\n------------------------")
input("Please Click Enter to Exit...")

