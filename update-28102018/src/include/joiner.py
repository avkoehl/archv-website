from collections import OrderedDict

def get_matches(clustergroups, c, d, m):
    if len(m) < 1:
        if clustergroups.get(c):
            m = clustergroups.get(c).split(',')
        m.append(c)
        d.append(c)

    else:
        temp = m
        for match in temp:
            if match not in d:
                if clustergroups.get(match):
                    matches = clustergroups.get(match).split(',')
                    for m2 in matches:
                        m.append(m2)
                    d.append(match)
                else:
                    m.append(match)
                    d.append(match)
            else:
                continue

    while len(d) != len(set(m)):
        get_matches(clustergroups,str(c),d,m)
        m = set(m)

    return sorted(list(m))

def wrapper(clustergroups):
    edges = OrderedDict() 
    index = OrderedDict((k,0) for k in clustergroups)

    for k in index:
        if index[k] == 0:
            test = get_matches(clustergroups, str(k), [], [])
            for t in test:
                index[t] = 1
            test.remove(k)
            edges[k] = ",".join(test)
    return edges
