import pydot


class Graph(object):
    def __init__(self, structure={}, styles={'rankdir': 'LR', 'splines':
                                                 'curves'}, layout='dot'):
        self.structure = structure
        self.graph = pydot.Dot(graph_type='graph', rankdir='LR',
                               splines='polyline')
        self.graph.set_prog(layout)

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
            if self.structure[key] != None:
                for edge in self.structure[key]:

                    # Set node-specific styles
                    # (only if there are style attributes speicified)
                    if type(edge) == dict:
                        for attr in edge.keys():
                            self.graph.get_node(key.replace(' ', '')).set(
                                attr, edge[attr])
                    elif type(edge) == list:

                        node = self.graph.get_node(edge[1])

                        if type(node) == list and len(node) == 0:
                            node = pydot.Node(edge[1].replace(' ', ''),
                                              style='filled',
                                              fillcolor='#C1C1C1',
                                              shape='rectangle',
                                              label=edge[1])
                            self.graph.add_node(node)

                        new_edge = pydot.Edge(
                            self.graph.get_node(key.replace(' ', '')),
                            # self.graph.get_node(edge[1]),
                            node,
                            label=edge[2],
                            arrowhead=self._arrow_head(edge[0]),
                            dir='forward')

                        # Set edge-specific styles
                        # (only if there are style attributes speicified)
                        try:
                            for attr in edge[3].keys():
                                # For some reason `Edge.set' does not work
                                # new_edge.set(attr, edge[3][attr])
                                # So this `hack' is required
                                new_edge.__getattribute__('set_' + attr)(
                                    edge[3][attr])
                        except Exception, e:
                            pass  # Not fatal

                        self.graph.add_edge(new_edge)

                    nodes = self.graph.get_nodes()

        self.graph.write('output.png', format='png')

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
            {
                'fillcolor': '#ABCDEF',
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


    sun = 'Sun'
    moon = 'Moon'
    earth = 'Earth'
    observer = 'External observer'
    threat_edge_style = {
        'color': '#FF0000',
        'fontcolor': '#FF0000',
        'label': 'does threaten',
        }
    test_structure = {
        sun: [
            ['->', earth, 'shines on'],
            ['->', moon, 'shines on'],
            {
                'style': 'filled',
                'fillcolor': '#FFFF00',
                }],
        moon: [
            ['->', earth, 'reflects on'],
            ['->', sun, 'reflects on'],
            {
                'style': 'filled',
                'fillcolor': '#C1C1C1',
                }],
        earth: [
            ['->', sun, 'coexists', {'dir': 'both'}],
            ['->', moon, 'coexists', {'dir': 'both'}],
            ['->', earth, 'threatens', threat_edge_style],
            ['->', sun, 'threatens', threat_edge_style],
            ['->', moon, 'threatens', threat_edge_style],
            ['->', 'satellite', 'observes\\n/analyzes', {'dir': 'back'}],
            {
                'style': 'filled',
                'fillcolor': '#AEFFAE',
                }],
        observer: [
            ['->', sun, 'observers'],
            ['->', moon, 'observers'],
            ['->', earth, 'observers'],
            ['->', 'something', 'does something', {
                    'fontcolor': '#FF00FF',
                    'color': '#FF00FF',
                    }],
            {
                'shape': 'ellipse',
                },
            ],
        }
# '': [
#     ['->', '', ''],
#     ['->', '', ''],
#     {
#         '': '',
#         '': '',
#         }
#     ],

    test_styles = {
        'splines': 'polyline',
        'rankdir': 'TD',
        }

graph = Graph(test_structure, test_styles)

graph.draw()
