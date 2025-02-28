import queue
import matplotlib.pyplot as plt
import networkx as nx
import time

def bfs(graph, start_node):
    visited = set()
    q = queue.Queue()
    q.put(start_node)

    order = []

    while not q.empty():
        vertex = q.get()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            for node in graph[vertex]:
                if node not in visited:
                    q.put(node)
    
    return order

def dfs(graph, start_node):
    s = list()  # stack.
    s.append(start_node)
    visited = set() 

    order = []

    while s:
        vertex = s.pop(0)
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            for node in graph[vertex]:
                if node not in visited: # and node not in s:
                    s.insert(0, node)
        
    return order


def generate_random_graph(n, m):
    while True:
        G = nx.gnm_random_graph(n, m)
        if nx.is_connected(G):
            return G



def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(title)
        nx.draw(G, pos, with_labels=True, node_color=['r' if n == node else 'g' for n in G.nodes])
        plt.draw()
        plt.pause(0.5)
    plt.show()
    time.sleep(0.5)


# G = nx.Graph()
# G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])




if __name__ == '__main__':

    G = generate_random_graph(20, 30)
    pos = nx.spring_layout(G)
    
    

    while True:
        print("1 for dfs \n2 for bfs")
        choice = int(input("choice : "))
        if choice == 1:
            visualize_search(dfs(G, 0), 'DFS Visualization' , G, pos)
            break
        elif choice == 2:
            visualize_search(bfs(G, 0), 'BFS Visulization', G, pos)
            break
        else:
            print("wrong choice. Choose again.")
            continue


