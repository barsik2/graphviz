from flask import Flask, request, jsonify, render_template, redirect, url_for
from pyvis.network import Network

#######################################################################################
from app import app
from common.pereferences import DEBUG, PORT, HOST, THREADED


@app.route('/index')
@app.route('/')
def hello():
    user = 'Egor'

    return render_template('start_page.html', user= user)


@app.route('/main/<name_project>')
def main_page(name_project):
    nx_file = f'nx/{name_project}.html'
    return render_template('main.html', nx_file= nx_file, name_project=name_project)

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

@app.route('/add_node', methods=['POST', 'GET'])
def add_node():
        print(request.form)
        name = request.form['firstname/']
        surname = request.form['surname']
        patro = request.form['patro']

        g.add_node(len(g.nodes), label=name, title = f"{surname}/{patro}")
        g.save_graph('server/app/templates/nx.html')



        return redirect(url_for('hello'))


@app.route('/add_edge', methods=['POST', 'GET'])
def add_edge():
        print(request.form)
        firstid = request.form['firstid']
        secondid = request.form['secondid']
        type_data = request.form['type']

        print( g.nodes)

        g.add_edge(int(firstid), int(secondid), type_data = type_data)
        g.save_graph('server/app/templates/nx.html')



        return redirect(url_for('hello'))
@app.route('/new_project', methods=['POST', 'GET'])
def new_project():
    return render_template('new_project.html')


@app.route('/creat_new_project', methods=['POST', 'GET'])
def creat_new_project():
    name_progect = request.form['name_progect']
    g = Network()
    g.save_graph(f'server/app/templates/nx/{name_progect}.html')
    
    return redirect(url_for(f'main_page', name_project = name_progect))

def main():
    app.run(HOST, PORT, debug=DEBUG, threaded=THREADED)

if __name__ == '__main__':
    main()
