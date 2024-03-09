def find_direct_friends(n, relationships):
    # Create a dictionary to represent the friendship graph
    graph = {}
    
    # Populate the friendship graph
    for i in range(n):
        id1, id2 = relationships[i]
        if id1 not in graph:
            graph[id1] = set()
        if id2 not in graph:
            graph[id2] = set()
        graph[id1].add(id2)
        graph[id2].add(id1)

    # Identify the undesirable person's friends and friends of friends
    undesirable_friends = set(graph[2])
    for friend in undesirable_friends.copy():
        undesirable_friends.update(graph[friend])

    # Find your direct friends who are not undesirable friends
    direct_friends = sorted(set(graph[1]) - undesirable_friends)

    # Output the result
    if direct_friends:
        print(" ".join(map(str, direct_friends)))
    else:
        print("nobody")


# Sample Input 0
input_0 = (2, [(1, 4), (2, 1)])
find_direct_friends(*input_0)

# Sample Input 1
input_1 = (8, [(1, 3), (9, 1), (3, 2), (8, 9), (5, 6), (7, 1), (2, 8), (1, 4)])
find_direct_friends(*input_1)

# Sample Input 2
input_2 = (4, [(1, 5), (6, 2), (5, 6), (6, 1)])
find_direct_friends(*input_2)
