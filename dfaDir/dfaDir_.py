'''
 Maria Isabel Ortiz Naranjo
 Carne: 18176
'''

from dfaDir.Automata import Automata, State, Handler
from dfaDir.tree import Tree
from dfaDir.cal import lastpos, firstpos, followpos, states_tree
from collections import Counter

OPERATORS = ['|', '*', '+', '?', '.', ')', '(']
EPSILON = "ε"

def sintetic_tree(data_tree, expresion):
    # class Tree
    value_tree = Tree()
    value_tree.data = '.'
    leaves = Tree()
    # mark symbol
    leaves.data = '#'
    # add to the new tree
    value_tree.right = leaves
    value_tree.left = data_tree

    # to create
    tree = states_tree(value_tree)
    first = firstpos(value_tree)
    last = lastpos(value_tree)
    # dictionary with the id state of node
    data = {}
    for position in tree:
        data[position] = []
    followpos(value_tree, data)
    
    #print(data.copy)

    tree_sintetic = direct(first, last, data, expresion)

    return tree_sintetic

def direct(first, last, data, expresion):
    automata = Automata(expresion)
    inicial = State(first, len(automata.state))
    automata.state.append(inicial)
    # print(automata.state.append(inicial))

    # take the last position
    if last[-1] in inicial.name:
        inicial.accept = True

    # symbols = get_symbol(expresion)
    symbols = []
    for symbol in expresion:
        if (symbol not in OPERATORS) and (symbol not in symbols) and (symbol != EPSILON):
            symbols.append(symbol)
    
    # go through the states of the automata
    for state in automata.state:
        for i in symbols:
            value = []
            for position in state.name:
                if position.data == i:
                    temp = data[position]
                    for j in temp:
                        if j not in value:
                            value.append(j)
            # if movements, ando no empty
            if movements(automata, value) and value != []:
                new_node = State(value, len(automata.state))
                if last[-1] in value:
                    new_node.accept = True
                automata.state.append(new_node)
                state.transition.append(Handler(i, automata.state[-1].id))
            # if value is emtpy
            elif value != []:
                # go to tree, and search the id
                add = add_tree(automata, value)
                if add:
                    state.transition.append(Handler(i, add.id))
                else:
                    print('There ir no node with %s ' % value)

    return automata

# if exist the node into the tree
def movements(tree, state):
    for node in tree.state:
        if Counter(node.name) == Counter(state):
            return False
    return True

def add_tree(automata, id):
    for node in automata.state:
        if Counter(node.name) == Counter(id):
            return node
    return False
    