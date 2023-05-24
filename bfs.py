graph = {
    '1':['2','5'],
    '2':['3','4'],
    '5':['6'],
    '3':[],
    '4':['6'],
    '6':[]
}

visited =[]
queue = []

def bfs(visited , graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m= queue.pop(0)
        print(m,end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("BFS \n")
bfs(visited,graph,'1')

visited= set()

graph = {
    '1':['2','5'],
    '2':['3','4'],
    '5':['6'],
    '3':[],
    '4':['6'],
    '6':[]
}

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("DFS")

dfs(visited, graph, '1')