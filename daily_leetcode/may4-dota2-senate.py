senate = list(input())
factions = {"R": "Radiant", "D": "Dire"}

i = 0

# Stop when either all elements are the same or only one element remaining
while len(senate) > 1 and len(set(senate)) > 1:
    
    next_i = (i+1)%len(senate)

    # Remove first instance that is not senate[i]
    j = next_i
    while j != i:
        next_j = (j+1)%len(senate)
        print(f"i={i} j={j} {senate}")
        if senate[j] != senate[i]:
            senate.pop(j)
            break
        j = next_j

    i = next_i%len(senate)
print(senate)
print(factions[senate[0]])
