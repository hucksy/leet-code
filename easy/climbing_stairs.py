def climbStairs(n: int) -> int:
    # recursively create a tree with all paths and return the sum of all paths
    def traverse_steps(step: int):
        if step == n -2:
            return 2
        elif step == n-1:
            return 1
        return traverse_steps(step + 1) + traverse_steps(step + 2)
    return traverse_steps(0)


print(climbStairs(9))