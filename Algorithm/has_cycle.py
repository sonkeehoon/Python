def has_cycle(graph, vertex, visited, parent):
    visited[vertex] = True

    for i in graph[vertex]:
        if not visited[i]:
            if has_cycle(graph, i, visited, vertex):
                return True
        elif parent != i:
            return True

    return False