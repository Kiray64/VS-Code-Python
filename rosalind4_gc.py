a = input()
dna_dict = {}
current_id = None


for line in a.splitlines():
    line = line.strip()

    if line.startswith(">"):
        current_id = line[1:]
        dna_dict[current_id] = ""
    else:
        dna_dict[current_id] += line

max = -1
max_id = None

for id, value in dna_dict.items():
    g = value.count("G")
    c = value.count("C")

    gc_percentage = 100 * (g + c) / len(value)

    if gc_percentage > max:
        max = gc_percentage 
        max_id = id

print(max_id)
print(max)