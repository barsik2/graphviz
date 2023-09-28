from flask import Flask, request, jsonify, render_template, redirect, url_for
from pyvis.network import Network

#######################################################################################
from app import app
from common.pereferences import DEBUG, PORT, HOST, THREADED

g = Network()
# g.add_nodes([1,2,3], value=[10, 100, 400],
#                          title=['I am node 1', 'node 2 here', 'and im node 3'],
#                          x=[21.4, 54.2, 11.2],
#                          y=[100.2, 23.54, 32.1],
#                          label=['NODE 1', 'NODE 2', 'NODE 3'],
#                          color=['#00ff1e', '#162347', '#dd4b39'])
g.save_graph('server/app/templates/nx.html')


@app.route('/index')
@app.route('/')
def hello():
    user = 'Egor'

    return render_template('main.html', user= user)

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

def main():
    app.run(HOST, PORT, debug=DEBUG, threaded=THREADED)

if __name__ == '__main__':
    main()
