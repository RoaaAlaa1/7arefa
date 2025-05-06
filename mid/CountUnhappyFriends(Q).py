# You are given a list of preferences for n friends, where n is always even.

# For each person i, preferences[i] contains a list of friends sorted in the order of preference. In other words, a friend earlier in the list is more preferred than a friend later in the list. Friends in each list are denoted by integers from 0 to n-1.

# All the friends are divided into pairs. The pairings are given in a list pairs, where pairs[i] = [xi, yi] denotes xi is paired with yi and yi is paired with xi.

# However, this pairing may cause some of the friends to be unhappy. A friend x is unhappy if x is paired with y and there exists a friend u who is paired with v but:

# x prefers u over y, and
# u prefers x over v.
# Return the number of unhappy friends.

    unhappy = 0
    
    for x in range(n):
        y = pair_map[x]
        x_pref = pref_rank[x][y]
        for u in preferences[x][:x_pref]:
            v = pair_map[u]
            if pref_rank[u][x] < pref_rank[u][v]:
                unhappy += 1
                break

def unhappyFriends(n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
    pair_map = {}
    for x, y in pairs:
        pair_map[x] = y
        pair_map[y] = x

    pref_rank = [[0]*n for _ in range(n)]
    for i in range(n):
        for rank, friend in enumerate(preferences[i]):
            pref_rank[i][friend] = rank
    
    return unhappy