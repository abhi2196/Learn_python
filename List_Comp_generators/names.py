NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    return [ name.title() for name in set(names) ]


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    second_name = [ name.split()[1] for name in names ]
    second_name.sort(reverse=True)
    return [ name for second in second_name for name in names if name.split()[1] == second ]


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    first_names = [ name.split()[0] for name in names ]
    min_length = len(first_names[0])
    for name in first_names:
        if len(name) < min_length:
            min_length = len(name)
    return [ name for name in first_names if len(name) == min_length ][0]
