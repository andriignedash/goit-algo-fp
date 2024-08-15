import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

def build_tree(values):
    root = None
    for value in values:
        root = insert(root, value)
    return root

def dfs_visualization(root, ax, pos, G):
    stack = [(root, 0)]
    color_step = 1.0 / (len(pos) - 1)
    colors = {}
    
    i = 0
    while stack:
        node, depth = stack.pop()
        if node:
            color = plt.cm.Blues(i * color_step)
            colors[node.value] = color
            stack.append((node.right, depth + 1))
            stack.append((node.left, depth + 1))
            i += 1

    nx.draw(G, pos, ax=ax, with_labels=True, node_color=[colors[node] for node in G.nodes], node_size=3000, font_size=15)

def bfs_visualization(root, ax, pos, G):
    queue = [(root, 0)]
    color_step = 1.0 / (len(pos) - 1)
    colors = {}
    
    i = 0
    while queue:
        node, depth = queue.pop(0)
        if node:
            color = plt.cm.Greens(i * color_step)
            colors[node.value] = color
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
            i += 1

    nx.draw(G, pos, ax=ax, with_labels=True, node_color=[colors[node] for node in G.nodes], node_size=3000, font_size=15)

def build_graph_from_tree(root):
    G = nx.DiGraph()
    pos = {}
    
    def add_edges(node, x=0, y=0, dx=1.0):
        if node:
            G.add_node(node.value)
            pos[node.value] = (x, y)
            if node.left:
                G.add_edge(node.value, node.left.value)
                add_edges(node.left, x - dx, y - 1, dx / 2)
            if node.right:
                G.add_edge(node.value, node.right.value)
                add_edges(node.right, x + dx, y - 1, dx / 2)
    
    add_edges(root)
    return G, pos

def visualize_tree_traversal(values):
    root = build_tree(values)
    G, pos = build_graph_from_tree(root)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    ax1.set_title("DFS Traversal")
    dfs_visualization(root, ax1, pos, G)

    ax2.set_title("BFS Traversal")
    bfs_visualization(root, ax2, pos, G)
    
    plt.show()

values = [10, 5, 15, 3, 7, 12, 18]
visualize_tree_traversal(values)
