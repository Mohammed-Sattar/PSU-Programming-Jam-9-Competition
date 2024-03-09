import sys

def dijkstra(graph, hub):
    n = len(graph)
    if hub < 0 or hub >= n:
        return []

    visited = [False] * n
    distance = [sys.maxsize] * n
    distance[hub] = 0

    for _ in range(n):
        min_distance = sys.maxsize
        min_vertex = -1

        for v in range(n):
            if not visited[v] and distance[v] < min_distance:
                min_distance = distance[v]
                min_vertex = v

        if min_vertex == -1:
            break

        visited[min_vertex] = True

        for v in range(n):
            if graph[min_vertex][v] != -1 and distance[min_vertex] + graph[min_vertex][v] < distance[v]:
                distance[v] = distance[min_vertex] + graph[min_vertex][v]

    return distance

def main():
    try:
        # Read input from console
        n = int(input())
        graph = []
        for _ in range(n):
            row = list(map(int, input().split()))
            graph.append(row)
        hub = int(input())

        # Compute fastest travel times
        distances = dijkstra(graph, hub)

        # Print the results
        for i in range(n):
            if i != hub:
                if distances and distances[i] != sys.maxsize:
                    print(distances[i])
                else:
                    print(-1)

    except ValueError:
        print(-1)
        
    except IndexError:
        print(-1)

if __name__ == "__main__":
    main()
