from random import choice, randint

from easygraph import EasyGraph


if __name__ == '__main__':
###########################################################################
# Settings
###########################################################################

#==========================================================================
# Test 1
#==========================================================================

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


#==========================================================================
# Test 2
#==========================================================================

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


#==========================================================================
# Test 3
#==========================================================================
# Constructs a relatively random graph.

    zero = 'Zero'
    one = 'One'
    two = 'Two'
    three = 'Three'
    four = 'Four'
    five = 'Five'
    six = 'Six'
    seven = 'Seven'
    eight = 'Eight'
    nine = 'Nine'

    bases = [
        zero,
        one,
        two,
        three,
        four,
        five,
        six,
        seven,
        eight,
        nine,

        'foo',
        'bar',
        'baz',
        'foobar',
        'barfoo',
        'foobaz',
        ]


    large_structure = {}

    def random_edge_type():
        return choice([
                'o->',
                '<-o',
                'o-o',
                'o-[]',
                '[]-o',
                '[]-<>',
                ])

    def random_base():
        return choice(bases)

    def random_label():
        return choice([
                'does something',
                'does something else',
                'does something completely different',
                'does nothing',
                ])

    def random_edge_style():
        return choice([
                {
                    'fontcolor': '#FF0000',
                    'color': '#FF0000',
                    'label': 'is red',
                    },
                {
                    'fontcolor': '#00FF00',
                    'color': '#00FF00',
                    'label': 'is green',
                    },
                {
                    'fontcolor': '#0000FF',
                    'color': '#0000FF',
                    'label': 'is blue',
                    },
                ])

    def random_node_style():
        return choice([
                {
                    'style': 'filled',
                    'fillcolor': '#FF7777',
                    },
                {
                    'style': 'filled',
                    'fillcolor': '#77FF77',
                    },
                {
                    'style': 'filled',
                    'fillcolor': '#7777FF',
                    },
                ])

    def random_edge():
        return [random_edge_type(), random_base(), random_label(),
                random_edge_style()]

    def random_structure(structure, bases):
        struct = structure

        for base in bases:
            struct[base] = []

        for key in struct:
            for i in range(1, randint(1, 20)):
                struct[key].append(random_edge())
            struct[key].append(random_node_style())
        return struct


    # Build a random structure
    large_structure = random_structure(large_structure, bases)


    large_styles = {
        'splines': 'polyline',
        'rankdir': 'TD',
        }


###########################################################################
# Run
###########################################################################

# graph = Graph(structure, styles)
# graph = Graph(test_structure, test_styles)

# graph = EasyGraph(large_structure, large_styles)
graph = EasyGraph(test_structure, test_styles)
graph.draw()
