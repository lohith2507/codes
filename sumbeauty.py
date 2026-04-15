def beautySub(s):
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i + 2, n):
            freq = {}
            for ch in s[i:j+1]:
                freq[ch] = freq.get(ch, 0) + 1
            values = list(freq.values())
            if len(values) > 1:
                ans += max(values) - min(values)
    return ans

print(beautySub("aabcb"))  # Example usage
print(beautySub("aabcbaa"))  # Example usage
print(beautySub("abc"))  # Example usage
            
        