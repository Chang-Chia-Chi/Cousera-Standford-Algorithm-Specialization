import time
from collections import defaultdict

# create masks
def d_Mask(n_bits):
    # zero mask
    masks = [0]
    # d = 1 mask
    masks += (1 << i for i in range(n_bits))
    # d = 2 mask
    for i in range(n_bits):
        for j in range(i+1, n_bits):
            masks.append(masks[i+1]^masks[j+1])
    return masks

# produce permutation for 2 node list
def edge_Iter(nodes1, nodes2):
    for n1 in nodes1:
        for n2 in nodes2:
            if n1 != n2:
                yield (n1, n2)

# Using distance as key so no need to compute pairwise distance
D_map = defaultdict(list)
# Union
Union = defaultdict(list)
Corr = {}
bits = ''
with open("clustering_big.txt", 'r') as file:
    lines = file.readlines()
    idx = 0
    for line in lines[1:]:
        b_list = line.split()
        bits = ''.join(b_list)
        # convert binary code into INT
        bin2Int = int(bits, 2)
        # add node to corresponding binary set
        D_map[bin2Int].append(idx)
        Union[idx].append(idx)
        Corr[idx] = idx
        idx += 1

masks = d_Mask(len(bits))

t1 = time.time()
# iter through all masks with keys in D_map.
# if XOR(mask, key) is in D_map, means you find 
# 2 clusters with distance in interest
for mask in masks:
    # mask all distance and find whether close pair exists
    for d1, nodes_1 in D_map.items():
        # check wether XOR(d1, mask) in D_map
        d2 = d1^mask
        if d2 in D_map:
            # if d2 in D_map, iterate all pairs
            nodes_2 = D_map[d2]
            # pay attention to zip is not suitable for permutation
            for n1, n2 in edge_Iter(nodes_1, nodes_2):
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


t2 = time.time() - t1
print(len(Union), t2)




