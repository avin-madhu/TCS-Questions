def bfs(graph: dict[str,str],start:str, n:int) -> str:
    res = ""
    queue = [start]
    visited = {i:False for i in graph}
    while queue:
        node = queue[0]
        queue = queue[1:]
        visited[node] = True
        res += node
        for neighbour in graph[node]:
            if not visited[neighbour] and not neighbour in queue:
                queue.append(neighbour)
    return res


def main():

    graph = {
        'A': "BC",
        'B': "DC",
        'C': "ABE",
        'D': "BE",
        'E': "DC"
    }

    number_of_nodes = len(graph)
    start = 'A'
    res = bfs(graph,start,number_of_nodes)
    print(res)

if __name__ == "__main__":
    main()
