import random
import math
import numpy as np

graph_matrix = input("Matrix: ")
order = 5

graph_matrix = graph_matrix.split("],")
for i in range(0, len(graph_matrix)):
    graph_matrix[i] = "[" + graph_matrix[i].replace("[", "").replace("]", "").replace(" ", "") + "]"
print(graph_matrix)

def get_edge_list_from_row(row_list, index):
    edge_list = []
    for i in range(0, len(row_list[index])):
        if str(row_list[index][i]) == "0" or str(row_list[index][i]) == "1" or str(row_list[index][i]) == "2":
            edge_list.append(int(row_list[index][i]))
    print(edge_list)
    return edge_list

def check_k3(graph_matrix):
    found_k3 = False
    for i in range(0, len(graph_matrix)):
        for j in range(0, len(graph_matrix[i])):
            edge_list = get_edge_list_from_row(graph_matrix, j)
            if i != j:
                for k in range(0, len(edge_list)):  # at edge (i, j)
                    if edge_list[k] == 1:
                        for l in range(0, len(graph_matrix)):
                            for m in range(0, len(graph_matrix[i])):
                                edge_list = get_edge_list_from_row(graph_matrix, j)
                                if l != m:
                                    for n in range(0, len(edge_list)):  # at edge (l, m)
                                        # check if (i, l) and (j, l) exist or (i, m) and (j, m)
                                        il = get_edge_list_from_row(graph_matrix, i)[l]
                                        jl = get_edge_list_from_row(graph_matrix, j)[l]

                                        im = get_edge_list_from_row(graph_matrix, i)[m]
                                        jm = get_edge_list_from_row(graph_matrix, j)[m]

                                        if il == 1 and jl == 1:
                                            print("FOUND K3!!!")
                                        if im == 1 and jm == 1:
                                            print("FOUND K3!!!")
                    if edge_list[k] == 2:
                        for l in range(0, len(graph_matrix)):
                            for m in range(0, len(graph_matrix[i])):
                                edge_list = get_edge_list_from_row(graph_matrix, j)
                                if l != m:
                                    for n in range(0, len(edge_list)):  # at edge (l, m)
                                        # check if (i, l) and (j, l) exist or (i, m) and (j, m)
                                        il = get_edge_list_from_row(graph_matrix, i)[l]
                                        jl = get_edge_list_from_row(graph_matrix, j)[l]

                                        im = get_edge_list_from_row(graph_matrix, i)[m]
                                        jm = get_edge_list_from_row(graph_matrix, j)[m]

                                        if il == 2 and jl == 2:
                                            print("FOUND K3!!!")
                                            found_k3 = True
                                        if im == 2 and jm == 2:
                                            print("FOUND K3!!!")
                                            found_k3 = True
    return found_k3

def generate_matrix():
    edge_list_temp = []
    matrix = []
    for i in range(0, 5):
        for j in range(0, 5):
            print(i)
            edge_list_temp.append(0)
            if j == 4:
                matrix.append(edge_list_temp)
                print("edge list: " + str(edge_list_temp))
                edge_list_temp = []
    for i in range(0, 5):
        for j in range(0, 5):
            if i != j:
                edge = random.randint(1, 2)
                matrix[i][j] = edge
                matrix[j][i] = edge
    return matrix

gigging = True

while gigging == True:
    new_matrix = generate_matrix()
    found_k3 = check_k3(new_matrix)
    array = np.array(new_matrix)
    determinant = np.linalg.det(array)
    if found_k3 == True and determinant != 0:
        print(str(new_matrix) + "\n\n" + str(determinant))
        information_w = open("Information_dump", "w")
        information_w.write(str(new_matrix) + "\n\n" + str(determinant))