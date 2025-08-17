from flask import Flask, request, render_template, send_file
import matplotlib.pyplot as plt
import networkx as nx
import os
from reportlab.pdfgen import canvas
from algo import Graph
import data2 as data

app = Flask(__name__, static_folder='static')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/input')
def input_page():
    return render_template('input.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(f"Message from {name} ({email}): {message}")
    return render_template('contact.html', success="Thank you for contacting us!")


@app.route('/check', methods=['POST'])
def check_social_id():
    try:
        social_id = int(request.form['social_id'])
        graph_obj = Graph(social_id)
        adj_list = graph_obj.create()
        result, cc, ef, ids = perform_fraudulent_check(graph_obj, social_id)
        graph_image_path = generate_graph_image(adj_list, social_id)
        return render_template('result.html', result=result, cc=cc, ef=ef, ids=ids, graph_image=graph_image_path)
    except KeyError:
        return render_template('input.html', error="Key Error: Social Media ID not found!")


@app.route('/generate-report')
def generate_report():
    pdf_path = "static/report.pdf"
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 800, "Social_Eye - Fraud Analysis Report")
    c.drawString(100, 780, "Result: Fraudulent or Not Fraudulent")  # Placeholder; replace with `result`
    c.drawString(100, 760, f"Clustering Coefficient (CC): 0%")  # Placeholder; replace with actual CC value
    c.drawImage("static/graph.png", 100, 500, width=400, height=200)  # Placeholder graph image
    c.save()
    return send_file(pdf_path, as_attachment=True)


def perform_fraudulent_check(graph_obj, target_node):
    ids = len(graph_obj.adj_list)
    connections = sum(len(v) for v in graph_obj.adj_list.values())
    actual_connections = connections
    length = len(data.data1[target_node]["follower"])
    total_possible = length * (length + 1)
    cc = (actual_connections / total_possible) * 100 if total_possible > 0 else 0

    if cc > 50:
        age = data.data1[target_node]["age"]
        ef = (1 + (5 / age)) ** age
        if ef < length:
            return f"The Social Media ID {target_node} is Fraudulent!", cc, ef, ids
        else:
            return f"The Social Media ID {target_node} is Not Fraudulent!", cc, ef, ids
    else:
        return f"The Social Media ID {target_node} is Not Fraudulent!", cc, None, ids


def generate_graph_image(adj_list, main_node):
    G = nx.DiGraph()
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)
    pos[main_node] = [0, 0]

    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='red', node_size=1500, font_size=15, arrows=True)
    nx.draw_networkx_nodes(G, pos, nodelist=[main_node], node_color='green', node_size=2000)

    graph_image_path = os.path.join('static', 'graph.png')
    plt.savefig(graph_image_path)
    plt.close()

    return graph_image_path


if __name__ == '__main__':
    app.run(debug=True)
