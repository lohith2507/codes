def maxavgsub(l,k):
    if len(l) < k:
        return None
    window_sum = sum(l[:k])
    maxi = window_sum / k
    for i in range(k, len(l)):
        window_sum += l[i] - l[i - k]
        maxi = max(maxi, window_sum / k)
    return maxi
# Example usage:
print(maxavgsub([1, 2, 3, 4, 5], 3))  # Output: 4.0
print(maxavgsub([1, 2, 3, 4, 5, 6], 4))  # Output: 5.0