def generate_strings(n):
    if n == 0:
        return ['']
    else:
        strings = generate_strings(n-1)
        return [s+c for s in strings for c in 'UD']
    
# Generate all strings of length 5
strings = generate_strings(40)

# Print the result
print(strings)
