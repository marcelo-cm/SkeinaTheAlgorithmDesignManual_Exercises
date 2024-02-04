# Describe how to test whether a given set of tickets establishes sufficient coverage in the Lotto problem of Section 1.6 (page 23).
# Write a program to find good ticket sets

possible_perms = []
covered = []
tickets = [{1, 4, 5}, {1, 2, 3}]
candidates = [1, 2, 3, 4, 5]


def permute(nums, cur, k, start, host):
    if k == 0:
        host.append(cur.copy())
        return
    for i in range(start, len(nums)):
        cur.add(nums[i])
        permute(nums, cur, k - 1, i + 1, host)
        cur.remove(nums[i])


def check_coverage():
    permute(candidates, set(), 2, 0, possible_perms)

    all_nums = set()

    for ticket in tickets:
        all_nums = all_nums.union(ticket)

    permute(list(all_nums), set(), 2, 0, covered)

    success = True
    for perm in possible_perms:
        if perm not in covered:
            print(perm, "not covered")
            success = False

    return success


print(check_coverage())
