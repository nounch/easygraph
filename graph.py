import pydot


class Graph(object):
    def __init__(self, structure, styles={'rankdir': 'LR', 'splines':
                                              'curves'}):
        self.structure = structure
        self.graph = pydot.Dot(graph_type='graph', rankdir='LR',
                               splines='polyline')

        for attr in styles.keys():
            self.graph.set(attr, styles[attr])

        self._arrow_symbols = {
            '->': 'normal',
            '--': 'none',
            '-[]': 'box',
            '-<': 'crow',
            '-)': 'curve',
            '-<>': 'diamond',
            '-o': 'dot',
            '-<<': 'inv',
            '-|': 'tee',
            '>>': 'vee',
            }

    def draw(self):
        for key in self.structure.keys():
            # No spaces in names
            self.graph.add_node(pydot.Node(key.replace(' ', ''),
                                           style='filled',
                                           fillcolor='#C1C1C1',
                                           shape='rectangle',
                                           label=key))

        for key in self.structure.keys():
            if structure[key] != None:
                for edge in structure[key]:
                    print(edge)  # DEBUG

                    # Set node-specific styles
                    # (only if there are style attributes speicified)
                    if type(edge) == dict:
                        for attr in edge.keys():
                            self.graph.get_node(key.replace(' ', '')).set(
                                attr, edge[attr])
                    elif type(edge) == list:
                        new_edge = pydot.Edge(
                            self.graph.get_node(key.replace(' ', '')),
                            self.graph.get_node(edge[1]),
                            label=edge[2],
                            arrowhead=self._arrow_head(edge[0]),
                            dir='forward')

                        # Set edge-specific styles
                        # (only if there are style attributes speicified)
                        try:
                            for attr in edge[3].keys():
                                print('ATTR: %s' % new_edge)  # DEBUG
                                # For some reason `Edge.set' does not work
                                # new_edge.set(attr, edge[3][attr])
                                # So this `hack' is required
                                new_edge.__getattribute__('set_' + attr)(
                                    edge[3][attr])
                        except Exception, e:
                            pass  # Not fatal

                        self.graph.add_edge(new_edge)

                    nodes = self.graph.get_nodes()
                    for node in nodes:
                        print(node.get_name())  # DEBUG


        self.graph.write_png('output.png')

    def _arrow_head(self, symbol='->'):
        sym = self._arrow_symbols['->']
        if symbol in self._arrow_symbols:
            sym = self._arrow_symbols[symbol]

        return sym



if __name__ == '__main__':
    duck = 'Dagobert_Duck';
    structure = {
        'tiger': [
            {
                'color': '#00FF00',
                'style': 'filled',
                'fillcolor': '#0000FF',
                },
            ['->', duck, 'eats'],
            ['--', duck, 'live in the same area', {
                    'color': '#FF0000',
                    }],
            ],
        duck: [
            {
                'shape': 'triangle',
                'style': 'filled',
                'fillcolor': '#FFFF00',
                },
            ['->', 'plancton', 'eats', {
                    'style': 'dotted',
                    'labelfontcolor': '#FFFF00',
                    'fontsize': '10.0',
                    }],
            ['->', 'human', 'recognizes'],
            ],
        'snail': [],
        'human': [
            ['->', 'tiger', 'studies'],
            ['--', duck, 'see each other frequently'],
            ['->', 'snail', 'bar', {
                    'color': '#FF0000',
                    'style': 'dashed',
                    'fontsize': '20.0',
                    'fontcolor': '#0000FF',
                    }],
            {
                'shape': 'circle',
                'style': 'filled',
                'fillcolor': '#FF0000',
                },
            ],
        'plancton': None,
        'wind': [
            ['--', 'human' , 'affects'],
            ['--', duck , 'affects'],
            ['--', 'tiger' , 'affects'],
            ],
        'sun': [
            ['--', 'human' , 'affects'],
            ['--', duck , 'affects'],
            ['--', 'tiger' , 'affects'],
            ['--', 'plancton' , 'affects'],
            ],
        'water': [
            ['--', duck , 'affects'],
            ['--', 'plancton' , 'affects'],
            ],
        'foo': [
            ['--', duck , 'affects', {
                    'color': '#00FF00',
                    'arrowhead': 'box',
                    }],
            ['--', 'plancton' , 'affects'],
            ],
        'Mighty One': [
            ['--', duck , 'influences'],
            ['->', duck , 'influences'],
            ['-[]', duck , 'influences'],
            ['-o', duck , 'influences'],
            ['-)', duck , 'influences'],
            ['>>', duck , 'influences'],
            ['-<', duck , 'influences'],
            ['-<<', duck , 'influences'],
            ['-|', duck , 'influences'],
            ['-<>', duck , 'influences'],
            ],
        }

    styles = {
        'splines': 'polyline',
        'rankdir': 'LR',
        }
    graph = Graph(structure, styles)
    graph.draw()
