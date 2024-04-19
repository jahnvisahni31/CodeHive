def longestPrefixSuffix(str: str) -> str:
    # Write your code here.
    n = len(str)
    for i in range(n-1, 0, -1):
        prefix = str[:i]
        suffix = str[n-i:]
        if prefix == suffix:
            return prefix
    return ""
    pass
