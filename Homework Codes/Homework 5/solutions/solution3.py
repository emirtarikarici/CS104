graph = {"A": (4, 5, 6), "B": (4, 3, 2, 1), "C": (3,), "D": (1, 5, 7), "E": (7, 2, 6)}


def give_edges(vertex):
    return graph[vertex]


def give_vertices(edge):
    vertices = []
    for key, value in graph.items():
        if edge in value:
            vertices.append(key)
    return tuple(vertices)


# Expect (4, 5, 6)
print(give_edges("A"))
# Expect ("B", "E")
print(give_vertices(2))
