from pyungo.core import Graph


graph = Graph()


@graph.register(inputs=['a', 'b'], outputs=['c'])
def f_my_function(a, b):
    return a + b


@graph.register(inputs=['d', 'a'], outputs=['e'])
def f_my_function3(d, a):
    return d - a


@graph.register(inputs=['c'], outputs=['d'])
def f_my_function2(c):
    return c / 10.


@graph.register(inputs=['e', 'a', 'f'], outputs=['v'])
def f_my_functiondede(c, a, tor):
    return c / 10.


graph.calculate(data={'a': 2, 'b': 3, 'f': 7})
