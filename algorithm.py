from mst import mst

def algorithm(n):
    output_list = []
    for i in range(0, n):
        if mst(i) != False:
            output_list.append(mst(i))
    return output_list
