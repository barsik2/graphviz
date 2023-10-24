from flask import Flask, request, jsonify, render_template, redirect, url_for, g, session
import networkx as nx
import os

#######################################################################################
from app import app
from common.pereferences import DEBUG, PORT, HOST, THREADED
from graph_constructor.visualization import GVNetwork
from graph_constructor.helpers import get_gen_data

class MySession:
    def __init__(self):
        self.select_id = None

    def set_select_id(self, select_id):
        self.select_id = select_id

    def get_select_id(self):
        return self.select_id

my_session = MySession()

@app.route('/index')
@app.route('/')
def hello():
    return render_template('start.html')

@app.route('/main/<name_project>')
def main(name_project):
    nx_file = f"nx/{name_project}/{name_project}.html"
    generate_path = f"/{name_project}/generate_graph"
    add_node_path = f"/{name_project}/add_node"
    add_edge_path = f"/{name_project}/add_edge"

    G = nx.read_graphml(f"server/app/static/nx/{name_project}/{name_project}.graphml")

    len_nodes = (len(G.nodes))
    len_edges = (len(G.edges))
    
    degrees = dict(G.degree())
    if degrees:
        max_degree = max(degrees.values())
    else:
        max_degree = 0

    center_nodes = "Не определен"
    
    return render_template('main.html', 
        nx_file = nx_file, name_project = name_project,
        add_node_path = add_node_path, add_edge_path = add_edge_path,
        generate_path = generate_path,
        len_nodes = len_nodes, len_edges = len_edges,
        center_nodes = center_nodes, max_degree = max_degree
    )

@app.route('/new_project', methods=['POST', 'GET'])
def new_project():
     return render_template('newProject.html')

@app.route('/create_new_project', methods=['POST', 'GET'])
def create_new_project():
    name_project = request.form['name_project']
    os.makedirs(f'server/app/static/nx/{name_project}')
    new_g = nx.Graph()
    g = GVNetwork()

    nx.write_graphml(new_g, f'server/app/static/nx/{name_project}/{name_project}.graphml')
    g.from_nx(new_g)
    g.loc_generate_html(name_project, name=f'server/app/static/nx/{name_project}/{name_project}.html')
    
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
    return render_template('api.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

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
        g = GVNetwork()
        G = nx.read_graphml(f"server/app/static/nx/{name_project}/{name_project}.graphml")
        node_attributes = {
            "label": name,
            "title": f"{surname}/{patro}",
        }
        
        G.add_node(len(G.nodes), **node_attributes)
        g.from_nx(G)

        nx.write_graphml(G, f'server/app/static/nx/{name_project}/{name_project}.graphml')
        g.loc_generate_html(name_project, name=f'server/app/static/nx/{name_project}/{name_project}.html')


        return redirect(url_for(f'main', name_project = name_project))


@app.route('/<name_project>/add_edge', methods=['POST', 'GET'])
def add_edge(name_project):
        print(request.form)
        firstid = request.form['firstid']
        secondid = request.form['secondid']
        type_data = request.form['type']

        G = nx.read_graphml(f"server/app/static/nx/{name_project}/{name_project}.graphml")
        g = GVNetwork()

        G.add_edge(int(firstid), int(secondid), type_data = type_data)
        g.from_nx(G)

        nx.write_graphml(G, f'server/app/static/nx/{name_project}/{name_project}.graphml')
        g.loc_generate_html(name_project, name=f'server/app/static/nx/{name_project}/{name_project}.html')



        return redirect(url_for(f'main', name_project = name_project))

@app.route('/<name_project>/generate_graph', methods=['POST', 'GET'])
def generate_graph(name_project):
        print(request.form)
        count = int(request.form['count'])
        p = 0.3

        data = get_gen_data(count)
        G = nx.gnp_random_graph(count, p)

        for i, node in enumerate(G.nodes()):
            G.nodes[node]['label'] = data['first_name'][i]
            G.nodes[node]['title'] = f"ФИО: {data['last_name'][i]} {data['first_name'][i]} {data['patronymic'][i]}/ ID: {i}"
            G.nodes[node]['fio'] = f"{data['last_name'][i]} {data['first_name'][i]} {data['patronymic'][i]}"
            G.nodes[node]['phone_number'] = data['phone_number'][i]
            G.nodes[node]['username'] = data['username'][i]
        
        g = GVNetwork()
        g.from_nx(G)

        nx.write_graphml(G, f'server/app/static/nx/{name_project}/{name_project}.graphml')
        g.loc_generate_html(name_project, name=f'server/app/static/nx/{name_project}/{name_project}.html')


        return redirect(url_for(f'main', name_project = name_project))
    
@app.route('/<project_name>/select_node', methods=['POST', 'GET'])
def select_node(project_name):
    print(request.get_json())
    node_id = request.get_json()['nodeId']
    
    G = nx.read_graphml(f"server/app/static/nx/{project_name}/{project_name}.graphml")

    if node_id != None:
        node_id = int(node_id)


    my_session.set_select_id(node_id)

    fio = nx.get_node_attributes(G, 'fio')[f'{node_id}'] if node_id != None else None
    username = nx.get_node_attributes(G, 'username')[f'{node_id}'] if node_id != None else None
    phone_number = nx.get_node_attributes(G, 'phone_number')[f'{node_id}'] if node_id != None else None

    return jsonify({'res_checker': my_session.get_select_id(),'type': "Вершина", "id": my_session.get_select_id(), 
    "fio": fio, "username": username, "phone_number": phone_number, 'degree': "0"})

def main():
    app.run(HOST, PORT, debug=DEBUG, threaded=THREADED)

if __name__ == '__main__':
    main()
