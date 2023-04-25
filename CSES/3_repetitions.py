s = input()
counts = {"A": 0, "C": 0, "T": 0, "G": 0}
temp_counts = {"A": 0, "C": 0, "T": 0, "G": 0}
counts[s[0]] = 1
temp_counts[s[0]] = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        temp_counts[s[i]] += 1
    else:
        temp_counts[s[i]] = 1
    if temp_counts[s[i]] >= counts[s[i]]:
        counts[s[i]] = temp_counts[s[i]]
print(max(counts.values()))