import heapq
def dijkstras(graph: dict[str, list[tuple[str, int]]], start: str) -> dict:
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    prev = []

    pq = [(0,start)] # priority queue
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distance[curr_node]:
            continue

        for neighbor, weight in graph[curr_node]:
            dist = curr_dist + weight

            if dist < distance[neighbor]:
                distance[neighbor] = dist
                prev.append(curr_node)
                heapq.heappush(pq, (dist, neighbor))
    return distance

def main():

    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start_node = 'A'
    shortest_paths = dijkstras(graph, start_node)
    print(shortest_paths)
    for node, distance in shortest_paths.items():
        print(f"Distance to {node}: {distance}")
    

if __name__ == "__main__":
    main()