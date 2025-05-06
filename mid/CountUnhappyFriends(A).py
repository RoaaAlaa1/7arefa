def unhappyFriends(n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
    # Create a dictionary to map each person to their preference order
    pref_rank = [[0]*n for _ in range(n)]
    for i in range(n):
        for rank, friend in enumerate(preferences[i]):
            pref_rank[i][friend] = rank
    
    # Create a dictionary to store current pairings
    pair_map = {}
    for x, y in pairs:
        pair_map[x] = y
        pair_map[y] = x
    
    unhappy = 0
    
    for x in range(n):
        y = pair_map[x]
        x_pref = pref_rank[x][y]
        # Check all friends that x prefers over y
        for u in preferences[x][:x_pref]:
            v = pair_map[u]
            # Check if u prefers x over v
            if pref_rank[u][x] < pref_rank[u][v]:
                unhappy += 1
                break
    
    return unhappy