if __name__ == "__main__":

    import algo
    import matplotlib.pyplot as plt
    import networkx as nx

    # Entering social member ID of the data
    algo.node = int(input("Enter the social member id : "))
    algo.p = algo.Graph(algo.node)

    # Creating an adjacency list
    adj_list = algo.p.create()
    print(adj_list)

    # Checking method for fraudulent checking
    algo.p.fraudulent_checker()

    main_node = algo.node  # Main node you want to highlight
    member_id = main_node  # You can set this to whatever ID you want to display in the title

    # Declaring a directed graph using networkx library
    G = nx.DiGraph()

    # Add nodes and edges
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)  # Seed for reproducibility
    pos[main_node] = [0, 0]  # Fix the position of the main node at the center

    plt.figure(figsize=(10, 8))

    # Add border
    ax = plt.gca()
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['bottom'].set_linewidth(10)
    ax.spines['left'].set_linewidth(10)

    # Set margins
    plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.1)

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='red', node_size=1500, font_size=15,
            arrows=True)

    # Highlight connections of the main node
    edges = G.edges(main_node)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='grey', width=2.5, arrows=True)
    nx.draw_networkx_nodes(G, pos, nodelist=[main_node], node_color='green', node_size=2000)

    # Show the graph
    plt.title(f"The connections of the Member id {member_id}", fontsize=18, pad=20)
    plt.show()
