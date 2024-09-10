import networkx as nx
import matplotlib.pyplot as plt

# Example dictionary
example_dict = {
    'root': {
        'child1': {
            'grandchild1': {},
            'grandchild2': {}
        },
        'child2': {
            'grandchild3': {},
            'grandchild4': {
                'great_grandchild1': {}
            }
        }
    }
}

def add_edges(graph, parent_name, child_dict):
    """Recursively add edges to the graph from the dictionary."""
    for child_name, grandchild_dict in child_dict.items():
        graph.add_edge(parent_name, child_name)
        add_edges(graph, child_name, grandchild_dict)

def draw_tree(dictionary):
    """Draw the tree represented by a dictionary."""
    G = nx.DiGraph()  # Create a directed graph

    # Start adding edges from the root
    for root_name, children_dict in dictionary.items():
        add_edges(G, root_name, children_dict)

    # Create a layout for nodes
    pos = nx.spring_layout(G)
    
    # Draw the graph
    nx.draw(G, pos, with_labels=True, arrows=False)
    plt.show()

# Call the function to draw the tree
draw_tree(example_dict)
