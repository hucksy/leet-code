# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version >= 12:
        return True
    else:
        return False

def firstBadVersion(n: int) -> int:
    is_bad = False
    start = 0
    while n != start:
        mid = start + (n-start) // 2
        is_bad = isBadVersion(mid)
        if is_bad:
            n = mid
        else:
            start = mid + 1
    return n


print(firstBadVersion(50))
        