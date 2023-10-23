import os
from pyvis.network import Network
from jinja2 import Environment, FileSystemLoader

class GVNetwork(Network):
    def __init__(self):
        super().__init__()
        self.template_new_dir = os.path.dirname(__file__) + "/local_templates/"
        self.templateNewEnv = Environment(loader=FileSystemLoader(self.template_new_dir))

    def generate_html(self, name="index.html", local=True, notebook=False, loc_template = "template.html"):
        """
        This method gets the data structures supporting the nodes, edges,
        and options and updates the template to write the HTML holding
        the visualization.
        :type name_html: str
        """
        # here, check if an href is present in the hover data
        print(loc_template)
        use_link_template = False
        for n in self.nodes:
            title = n.get("title", None)
            if title:
                if "href" in title:
                    """
                    this tells the template to override default hover
                    mechanic, as the tooltip would move with the mouse
                    cursor which made interacting with hover data useless.
                    """
                    use_link_template = True
                    break
        if not notebook:
            # with open(loc_template) as html:
            #     content = html.read()
            template = self.templateNewEnv.get_template(loc_template)  # Template(content)
        else:
            template = self.template

        nodes, edges, heading, height, width, options = self.get_network_data()

        # check if physics is enabled
        if isinstance(self.options, dict):
            if 'physics' in self.options and 'enabled' in self.options['physics']:
                physics_enabled = self.options['physics']['enabled']
            else:
                physics_enabled = True
        else:
            physics_enabled = self.options.physics.enabled

        self.html = template.render(height=height,
                                    width=width,
                                    nodes=nodes,
                                    edges=edges,
                                    heading=heading,
                                    options=options,
                                    physics_enabled=physics_enabled,
                                    use_DOT=self.use_DOT,
                                    dot_lang=self.dot_lang,
                                    widget=self.widget,
                                    bgcolor=self.bgcolor,
                                    conf=self.conf,
                                    tooltip_link=use_link_template,
                                    neighborhood_highlight=self.neighborhood_highlight,
                                    select_menu=self.select_menu,
                                    filter_menu=self.filter_menu,
                                    notebook=notebook,
                                    cdn_resources=self.cdn_resources
                                    )
        return self.html


if __name__ == "__main__":
    mynw = GVNetwork()
    mynw.add_node(0, label = "Я котик")
    mynw.save_graph('kotik.html')