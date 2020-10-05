E = list()
Union = {}
Corr = {}
with open("clustering1.txt", 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:
        n1, n2, cost = line.split()
        cost = int(cost)
        E.append(tuple((n1, n2, cost)))
        if n1 not in Union:
            Union[n1] = [n1]
            Corr[n1] = n1
        if n2 not in Union:
            Union[n2] = [n2]
            Corr[n2] = n2

# ordering edges in increasing order of cost
E = sorted(E, key=lambda x: x[2])

cri = 4
idx = 0
for e in E:
    idx += 1
    # if # of clusters = cri, stop loop
    if len(Union) == cri:
        break
    n1, n2 = e[0], e[1]
    # leader for l1 and l2
    l1, l2 = Corr[n1], Corr[n2]
    # if l1 != l2 means n1 and n2 are in different cluster and need to fuse.
    if l1 != l2:
        if len(Union[l1]) >= len(Union[l2]):
            # fuse smaller cluster into larger one
            fuse = Union[l2]
            Union[l1] += fuse
            del Union[l2]
            # change corresponding leader for nodes in smaller cluster
            for n in fuse:
                Corr[n] = l1
        else:
            # fuse smaller cluster into larger one
            fuse = Union[l1]
            Union[l2] += fuse
            del Union[l1]
            # change corresponding leader for nodes in smaller cluster
            for n in fuse:
                Corr[n] = l2
    else:
        continue

# find next edge makes k = cri -1, that edge is maximum spacing
for e in E[idx:]:
    n1, n2 = e[0], e[1]
    # leader for l1 and l2
    l1, l2 = Corr[n1], Corr[n2] 
    if l1 != l2:
        m_s = e
        break

print(m_s)

