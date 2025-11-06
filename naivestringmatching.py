# Naive String Matching Algorithm

def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    
    print("Pattern found at indices:", end=" ")
    for i in range(n - m + 1):   # Slide pattern over text
        match = True
        for j in range(m):       # Check each character
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            print(i, end=" ")

# Example
text = "AABAACAADAABAABA"
pattern = "AABA"

naive_string_match(text, pattern)
