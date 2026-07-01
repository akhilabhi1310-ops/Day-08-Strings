string1 = input("Enter First String: ").lower()
string2 = input("Enter Second String: ").lower()
if sorted(string1) == sorted(string2):
    print("Anagram")
else:
    print("Not Anagram")
print("\n------------------------")
input("Please Click Enter to Exit...")

