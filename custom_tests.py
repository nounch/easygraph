from graph import Graph


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
            ['->', sun, 'coexists', {
                    'arrowhead': 'dot',
                    'arrowtail': 'dot',
                    'dir': 'both',
                    }],
            ['->', moon, 'coexists', {'dir': 'both'}],
            ['->', earth, 'threatens', threat_edge_style],
            ['->', sun, 'threatens', threat_edge_style],
            ['->', moon, 'threatens', threat_edge_style],
            ['->', 'satellite', 'observes\\n/analyzes', {'dir': 'back'}],
            ['o-o', 'one', 'foo'],
            ['/-\\', 'one', 'foo'],
            ['>>-<<', 'one', 'foo'],
            ['|-|', 'one', 'foo'],
            ['<<>>', 'one', 'foo'],
            ['>o-o<', 'one', 'foo'],
            ['<>-<>', 'nonsense', 'does nothing', {
                    'style': 'filled',
                    'color': '#FFAEFF',
                    'fontcolor': '#FFAEFF',
                    }],
            {
                'style': 'filled',
                'fillcolor': '#AEFFAE',
                }],
        observer: [
            ['o-[]', 'barfoo', 'barfoos'],
            ['<<-<<', 'barfoo2', 'barfoos'],
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
        'rankdir': 'LR',
        }

graph = Graph(test_structure, test_styles)

graph.draw()
