import pydot


class EasyGraph(object):
    def __init__(self, structure={}, styles={'rankdir': 'LR', 'splines':
                                                 'curves'}, layout='dot'):
        # def __init__(self, structure, styles, layout='dot'):
        self.structure = structure
        self.graph = pydot.Dot(graph_type='graph', rankdir='LR',
                               splines='polyline')
        self.graph.set_prog(layout)

        self._BOTH_ARROW_HEAD = '<->';

        for attr in styles.keys():
            self.graph.set(attr, styles[attr])

        self._arrow_symbols_left = {
            '<-': 'normal',
            '-': 'none',
            '[]-': 'box',
            '>-': 'crow',
            '\\-': 'halfopen',
            '<>-': 'diamond',
            'o-': 'dot',
            '>>-': 'inv',
            '|-': 'tee',
            '<<-': 'vee',
            'o<-': 'invdot',
            }

        self._arrow_symbols_right = {
            '->': 'normal',
            '-': 'none',
            '-[]': 'box',
            '-<': 'crow',
            '-\\': 'halfopen',
            '-<>': 'diamond',
            '-o': 'dot',
            '-<<': 'inv',
            '-|': 'tee',
            '->>': 'vee',
            '->o': 'invdot',
            }

        self._arrow_symbols = {
            '->': 'normal',
            '--': 'none',
            '-[]': 'box',
            '-<': 'crow',
            '-\\': 'halfopen',
            '-<>': 'diamond',
            '-o': 'dot',
            '-<<': 'inv',
            '-|': 'tee',
            '->>': 'vee',
            '>>': 'vee',
            '-o<': 'invdot',
            }
        self._double_arrow_symbols = {
            '<->': 'normal',
            '--': 'none',
            '[]-[]': 'box',
            '>-<': 'crow',
            '/-\\': 'halfopen',
            '<>-<>': 'diamond',
            'o-o': 'dot',
            '>>-<<': 'inv',
            '|-|': 'tee',
            '<<->>': 'vee',
            '<<>>': 'vee',
            '>o-o<': 'invdot',
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
                            # arrowhead=self._arrow_head(edge[0]),
                            # arrowhead='->',
                            # dir='forward'

                            # arrowhead='normal',
                            # dir='forward'
                            )
                        self._dispatch_arrow_head(new_edge, edge[0]);

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

    def _dispatch_arrow_head(self, edge, symbol):
        if symbol in self._arrow_symbols:
            # In theory, this should work:
            #
            # edge.set('arrowhead', self._arrow_symbols[symbol])
            # edge.set('dir', 'forward')
            #
            # In reality, it does not. So this `hack' is required:
            edge.__getattribute__('set_arrowhead')(
                self._arrow_symbols[symbol])
            edge.__getattribute__('set_dir')('forward')

        elif symbol in self._double_arrow_symbols:
            # In theory, this should work:
            #
            # edge.set('arrowhead', self._double_arrow_symbols[symbol])
            # edge.set('arrowtail', self._double_arrow_symbols[symbol])
            # edge.set('dir', 'both')
            #
            # In reality, it does not. So this `hack' is required:
            edge.__getattribute__('set_arrowhead')(
                self._double_arrow_symbols[symbol])
            edge.__getattribute__('set_arrowtail')(
                self._double_arrow_symbols[symbol])
            edge.__getattribute__('set_dir')('both')
        else:
            try:
                syms = symbol.split('-')
                left = syms[0] + '-'
                right = '-' + syms[-1]
                if left in self._arrow_symbols_left and right in self._arrow_symbols_right:
                    edge.__getattribute__('set_arrowhead')(
                        self._arrow_symbols_right[right])
                    edge.__getattribute__('set_arrowtail')(
                        self._arrow_symbols_left[left])
                    edge.__getattribute__('set_dir')('both')
            except Exception, e:
                # In theory, this should work:
                #
                # edge.set('arrowhead', 'normal')
                # edge.set('dir', 'forward')
                #
                # In reality, it does not. So this `hack' is required:
                edge.__getattribute__('set_arrowhead')('normal')
                edge.__getattribute__('set_dir')('forward')
