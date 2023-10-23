from flask import Flask, request, jsonify, render_template, redirect, url_for
from pyvis import network
from pyvis.network import Network
import networkx as nx
import os

#######################################################################################
from app import app
from common.pereferences import DEBUG, PORT, HOST, THREADED


@app.route('/index')
@app.route('/')
def hello():
    return render_template('start.html')

@app.route('/main/<name_project>')
def main(name_project):
    nx_file = f"nx/{name_project}/{name_project}.html"
    add_node_path = f"/{name_project}/add_node"
    add_edge_path = f"/{name_project}/add_edge"

    G = nx.read_graphml(f"server/app/static/nx/{name_project}/{name_project}.graphml")

    len_nodes = (len(G.nodes))
    len_edges = (len(G.edges))
    
    return render_template('main.html', 
    nx_file = nx_file, name_project = name_project,
    add_node_path = add_node_path, add_edge_path = add_edge_path,
    len_nodes = len_nodes, len_edges = len_edges
    )

@app.route('/new_project', methods=['POST', 'GET'])
def new_project():
     return render_template('newProject.html')

@app.route('/create_new_project', methods=['POST', 'GET'])
def create_new_project():
    name_project = request.form['name_project']
    os.makedirs(f'server/app/static/nx/{name_project}')
    new_g = nx.Graph()
    g = Network()

    nx.write_graphml(new_g, f'server/app/static/nx/{name_project}/{name_project}.graphml')
    g.from_nx(new_g)
    g.save_graph(f'server/app/static/nx/{name_project}/{name_project}.html')
    
    return redirect(url_for(f'main', name_project = name_project))

@app.route('/load_project', methods=['GET', 'POST'])
def load_project():
    projects = os.listdir('server/app/static/nx')
    return render_template('loadProject.html', projects = projects)

@app.route('/upload_project', methods=['GET', 'POST'])
def upload_project():
     name_project = request.form['name_project']
     return redirect(url_for(f'main', name_project = name_project))

@app.route('/api')
def api():
    user = 'Egor'

    return render_template('api.html', user= user)

@app.route('/settings')
def settings():
    user = 'Egor'

    return render_template('settings.html', user= user)

@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        data = request.args

        return ''

@app.route('/<name_project>/add_node', methods=['POST', 'GET'])
def add_node(name_project):
        print(request.form)
        name = request.form['firstname/']
        surname = request.form['surname']
        patro = request.form['patro']
        g = Network()
        G = nx.read_graphml(f"server/app/static/nx/{name_project}/{name_project}.graphml")
        node_attributes = {
            "label": name,
            "title": f"{surname}/{patro}",
        }
        
        G.add_node(len(G.nodes), **node_attributes)
        g.from_nx(G)

        nx.write_graphml(G, f'server/app/static/nx/{name_project}/{name_project}.graphml')
        g.save_graph(f'server/app/static/nx/{name_project}/{name_project}.html')



        return redirect(url_for(f'main', name_project = name_project))


@app.route('/<name_project>/add_edge', methods=['POST', 'GET'])
def add_edge(name_project):
        print(request.form)
        firstid = request.form['firstid']
        secondid = request.form['secondid']
        type_data = request.form['type']

        G = nx.read_graphml(f"server/app/static/nx/{name_project}/{name_project}.graphml")
        g = Network()

        G.add_edge(int(firstid), int(secondid), type_data = type_data)
        g.from_nx(G)

        nx.write_graphml(G, f'server/app/static/nx/{name_project}/{name_project}.graphml')
        g.save_graph(f'server/app/static/nx/{name_project}/{name_project}.html')



        return redirect(url_for(f'main', name_project = name_project))

def main():
    app.run(HOST, PORT, debug=DEBUG, threaded=THREADED)

if __name__ == '__main__':
    main()
