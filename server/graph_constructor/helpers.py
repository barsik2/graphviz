from bs4 import BeautifulSoup
from pyvis.network import Network

def load_graph_from_html(html_file_path, output_html_path):
    # Откройте файл HTML и загрузите его с помощью BeautifulSoup
    with open(html_file_path, "r") as html_file:
        soup = BeautifulSoup(html_file, "html.parser")

    # Извлеките данные о графе (узлы и рёбра) из HTML
    nodes = []
    edges = []

    for node in soup.find_all("li", class_="network-popover"):
        node_id = int(node["data-node-id"])
        label = node.find("span", class_="node-label").text
        nodes.append((node_id, label))

    for edge in soup.find_all("li", class_="edge"):
        source = int(edge["data-from"])
        target = int(edge["data-to"])
        edges.append((source, target))

    # Создайте экземпляр класса Network и добавьте узлы и рёбра
    graph = Network()
    for node_id, label in nodes:
        graph.add_node(node_id, label=label)
    for source, target in edges:
        graph.add_edge(source, target)

    print(graph)

    # Сохраните загруженный граф в новый HTML-файл
    graph.show(output_html_path)

if __name__ == '__main__':
    load_graph_from_html("server/app/static/nx/Ddfas.html", "loaded_graph.html")
