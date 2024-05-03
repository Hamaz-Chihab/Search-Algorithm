# import tkinter as tk


# def find_path():
#     # Your path finding code goes here
#     pass
           # total cost for nodes visited
# if __name__ == '__main__':
#     start_node = 'S'
#     goal_node = 'D'
#     visited_nodes, optimal_nodes = AStarSearch(tree, heuristic, start_node, goal_node)
#     print('visited nodes: ' + str(visited_nodes))
#     print('optimal nodes sequence: ' + str(optimal_nodes))

# window = tk.Tk()
# button = tk.Button(window, text="Find Path", command=find_path)
# button.pack()
# window.mainloop()
# -------------------------------------------------------------------------------------------------------------------


# def draw_graph(tree, start, goal):
#     # Create a new Tkinter window
#     window = tk.Tk()

#     # Set the window title
#     window.title("A* Search Visualization")

#     # Create a canvas to draw the graph
#     canvas = tk.Canvas(window, width=600, height=600)
#     canvas.pack()

#     # Calculate the positions of the nodes
#     node_positions = calculate_node_positions(tree)

#     # Draw the nodes
#     for node, position in node_positions.items():
#         x, y = position
#         canvas.create_oval(x-20, y-20, x+20, y+20, fill="blue")
#         canvas.create_text(x, y, text=node, fill="white")

#     # Draw the edges
#     for node, edges in tree.items():
#         x1, y1 = node_positions[node]
#         for edge in edges:
#             x2, y2 = node_positions[edge[0]]
#             canvas.create_line(x1, y1, x2, y2, fill="black")

#     # Run the A* algorithm
#     _, optimal_nodes = AStarSearch(tree, heuristic, start, goal)

#     # Draw the optimal path
#     for i in range(len(optimal_nodes) - 1):
#         x1, y1 = node_positions[optimal_nodes[i]]
#         x2, y2 = node_positions[optimal_nodes[i+1]]
#         canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

#     # Show a message box with the optimal path
#     messagebox.showinfo("Optimal Path", " -> ".join(optimal_nodes))

#     # Start the Tkinter event loop
#     window.mainloop()

# def calculate_node_positions(tree):
#     # Number of nodes
#     N = len(tree)

#     # Center of the circle
#     center_x, center_y = 300, 300

#     # Radius of the circle
#     radius = 200

#     # Positions of the nodes
#     node_positions = {}

#     # Calculate the position of each node
#     for i, node in enumerate(tree):
#         # Angle of the node (in radians)
#         angle = 2 * math.pi * i / N

#         # Position of the node
#         x = center_x + radius * math.cos(angle)
#         y = center_y + radius * math.sin(angle)

#         # Add the position to the dictionary
#         node_positions[node] = (x, y)

#     return node_positions

# # Call the function to draw the graph
# draw_graph(tree, 'E', 'S')
# -------------------------------------------------------------------------------------------------------------------


import tkinter as tk
from tkinter import messagebox
import math
from A_start_Algorithme import AStarSearch
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(tree, start, goal):
    # Create a new Tkinter window
    window = tk.Tk()

    # Set the window title
    window.title("A* Search Visualization")

    # Create a canvas to draw the graph
    canvas = tk.Canvas(window, width=600, height=600)
    canvas.pack()

    # Calculate the positions of the nodes
    node_positions = calculate_node_positions(tree)

    # Draw the nodes
    for node, position in node_positions.items():
        x, y = position
        canvas.create_oval(x-20, y-20, x+20, y+20, fill="blue")
        canvas.create_text(x, y, text=node, fill="white")

    # Draw the edges
    for node, edges in tree.items():
        x1, y1 = node_positions[node]
        for edge in edges:
            x2, y2 = node_positions[edge[0]]
            canvas.create_line(x1, y1, x2, y2, fill="black")

    # Run the A* algorithm
    _, optimal_nodes = AStarSearch(tree, heuristic, start, goal)

    # Draw the optimal path
    for i in range(len(optimal_nodes) - 1):
        x1, y1 = node_positions[optimal_nodes[i]]
        x2, y2 = node_positions[optimal_nodes[i+1]]
        canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

    # Show a message box with the optimal path
    messagebox.showinfo("Optimal Path", " -> ".join(optimal_nodes))

    # Start the Tkinter event loop
    window.mainloop()

def calculate_node_positions(tree):
    # Number of nodes
    N = len(tree)

    # Center of the circle
    center_x, center_y = 300, 300

    # Radius of the circle
    radius = 200

    # Positions of the nodes
    node_positions = {}

    # Calculate the position of each node
    for i, node in enumerate(tree):
        # Angle of the node (in radians)
        angle = 2 * math.pi * i / N

        # Position of the node
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        # Add the position to the dictionary
        node_positions[node] = (x, y)

    return node_positions

# Call the function to draw the graph
tree = {
    'S': [['A', 1], ['B', 5], ['C', 8], ['D', 2], ['E', 3]],
    'A': [['S', 1], ['D', 3], ['E', 7], ['G', 9], ['H', 3], ['I', 4]],
    'B': [['S', 5], ['G', 4], ['I', 7], ['J', 2]],
    'C': [['S', 8], ['G', 5], ['J', 6], ['K', 3]],
    'D': [['A', 3], ['K', 1], ['L', 2]],
    'E': [['A', 7], ['L', 2], ['M', 5]],
    'G': [['A', 9], ['B', 4], ['C', 5], ['M', 3], ['N', 2]],
    'H': [['A', 3], ['N', 4], ['O', 7]],
    'I': [['A', 4], ['B', 7], ['O', 6]],
    'J': [['B', 2], ['C', 6], ['P', 3]],
    'K': [['C', 3], ['D', 1], ['P', 5]],
    'L': [['D', 2], ['E', 2], ['Q', 1]],
    'M': [['E', 5], ['G', 3], ['Q', 2]],
    'N': [['G', 2], ['H', 4], ['R', 6]],
    'O': [['H', 7], ['I', 6], ['R', 3]],
    'P': [['J', 3], ['K', 5], ['S', 4]],
    'Q': [['L', 1], ['M', 2], ['S', 5]],
    'R': [['N', 6], ['O', 3]],
    'S': [['P', 4], ['Q', 5]]
}
G = nx.Graph()

for node, edges in tree.items():
    for edge in edges:
        G.add_edge(node, edge[0], weight=edge[1])
pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
heuristic = {
    'S': 10,
    'A': 9,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 5,
    'G': 4,
    'H': 3,
    'I': 3,
    'J': 3,
    'K': 2,
    'L': 2,
    'M': 2,
    'N': 1,
    'O': 1,
    'P': 1,
    'Q': 1,
    'R': 0  
}
draw_graph(tree, 'E', 'C')