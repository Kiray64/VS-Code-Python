bigdna = input()
littledna = input()

def find_matches(dna1, dna2):
    max_matches = 0
    coords = []
    diff = len(dna1) - len(dna2) + 1
    for i in range(diff):
        diffdna = dna1[i:i + len(dna2)]
        matches = 0
        for id, value in enumerate(dna2):
            if diffdna[id] == value:
                matches += 1
        if max_matches < matches:
            max_matches = matches
            coords = [[i, i + len(dna2)]] #двойной вложенный список
        elif max_matches == matches:
            coords.append ([i, i + len(dna2)])
    return max_matches, coords
            
print(find_matches(bigdna, littledna))