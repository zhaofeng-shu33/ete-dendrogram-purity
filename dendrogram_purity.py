# implement dengram purity for ete.Tree structure

def lca(tree, i, j):
    node_i = tree.search_nodes(name = str(i))[0]
    node_j = tree.search_nodes(name = str(j))[0]
    node_i_parent_list = node_i.get_ancestors()
    node_j_parent_list = node_j.get_ancestors()
    pointer_i = len(node_i_parent_list) - 1
    pointer_j = len(node_j_parent_list) - 1
    while(pointer_i >= 0 and pointer_j >= 0):
        if(node_i_parent_list[pointer_i] != node_j_parent_list[pointer_j]):
            break
        pointer_i -= 1
        pointer_j -= 1
    common_parent = node_i_parent_list[pointer_i+1]
    leaves = []
    for i in common_parent.get_leaves():
        leaves.append(int(i.name))
    return leaves

def set_purity(A, B):
    numerator = len(set(A).intersection(B))
    denominator = len(A)
    return numerator*1.0/denominator
    
def dendrogram_purity(tree, leaf_partition):
    purity = 0
    cnt = 0
    for Ck in leaf_partition:
        for i in range(len(Ck)):
            for j in range(i+1, len(Ck)):
                index_i = Ck[i]
                index_j = Ck[j]
                cnt += 1
                lca_set = lca(tree, index_i, index_j)
                purity += set_purity(lca_set, Ck)
    purity /= cnt
    return purity