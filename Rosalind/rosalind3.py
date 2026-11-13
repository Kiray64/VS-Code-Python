a = input()

pairs = {"A": "T", "T": "A", "G": "C", "C": "G"}

table = str.maketrans(pairs)

print(a.translate(table)[::-1])