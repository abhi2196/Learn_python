import itertools

def friends_teams(friends_list, team_size=2, order_does_matter=False):
    if order_does_matter:
        return itertools.permutations(friends_list, team_size)
    else:
        return itertools.combinations(friends_list, team_size)
    
