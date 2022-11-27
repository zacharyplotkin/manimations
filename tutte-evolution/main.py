import networkx as nx  # to handle calculating the Tutte polynomial
from manim import *  # to draw all our fancy animations
from sympy import factor  # factor our Tutte polynomial so it looks prettier


class TuttePolynomialFull(Scene):
    def construct(self):

        # calculate the Tutte polynomial of a given graph, then parse and return the output
        def calculate_tutte_polynomial(vertices, edges):

            # create the graph

            # create a graph entity via networkx
            graph = nx.Graph()
            # add edges to the graph from the input edge values
            graph.add_edges_from(edges)
            # add vertices to the graph from the input vertex values
            graph.add_nodes_from(vertices)

            # calculate the polynomial and parse the returned values

            # change ** to ^ so Tex recognizes the superscript, and change * to empty character because I don't like how
            # the * looks as a multiplication sign
            raw_tutte = nx.tutte_polynomial(graph).factor()
            parsed_tutte = str(raw_tutte).replace("**", "^").replace("*", "")
            # parse into a format that Tex can read
            polynomial = Tex(r"$" + parsed_tutte + "$")
            # return the parsed value
            return polynomial

        def create_and_draw():
            # connect the graph and text together
            group = VGroup(g, g_tutte)
            # arrange them so that the graph is on top, with the text below it
            group.arrange(DOWN)
            # set the width of the frame
            group.width = config["frame_width"] - 2 * LARGE_BUFF
            group.height = config["frame_height"] - 2 * LARGE_BUFF

            # write the text using Tex
            self.play(Write(g_tutte))
            # draw the graph
            self.play(Create(g))
            # wait 3 seconds
            self.wait(3)
            # clear the screen
            self.play(Unwrite(g_tutte))
            self.play(Uncreate(g))

        # test graph 1

        vertices = [1]
        edges = []
        g = Graph(vertices, edges)
        g_tutte = calculate_tutte_polynomial(vertices, edges)
        create_and_draw()

        # test graph 2

        vertices = [1, 2]
        edges = [(1, 2)]
        g = Graph(vertices, edges)
        g_tutte = calculate_tutte_polynomial(vertices, edges)
        create_and_draw()

        # test graph 3

        vertices = [1, 2, 3]
        edges = [(1, 2), (1, 3)]
        g = Graph(vertices, edges)
        g_tutte = calculate_tutte_polynomial(vertices, edges)
        create_and_draw()

        # test graph 4

        vertices = [1, 2, 3]
        edges = [(1, 2), (1, 3), (2, 3)]
        g = Graph(vertices, edges)
        g_tutte = calculate_tutte_polynomial(vertices, edges)
        create_and_draw()

        # first graph

        # initial list of vertices for the graph
        vertices = [1, 2, 3, 4]
        # initial list of tuples for the edges of the graph
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        # create the graph from the edge list and tuple list
        g = Graph(vertices, edges)
        # call the previous method we defined to calculate and parse the Tutte polynomial of the graph we just made
        g_tutte = calculate_tutte_polynomial(vertices, edges)

        # draw it
        create_and_draw()

        # second graph

        # add a vertex to the graph
        vertices.append(5)
        # add an edge to the graph
        edges.append((4, 5))
        # same as before, create the graph, draw, and calculate it
        g = Graph(vertices, edges)
        g_tutte = calculate_tutte_polynomial(vertices, edges)

        create_and_draw()

        # third graph

        vertices.append(6)
        edges.extend([(4, 6), (5, 6)])
        g = Graph(vertices, edges)
        g_tutte = calculate_tutte_polynomial(vertices, edges)

        create_and_draw()

        # fourth graph

        vertices.append(7)
        edges.extend([(5, 7), (6, 7)])
        g = Graph(vertices, edges)
        g_tutte = calculate_tutte_polynomial(vertices, edges)

        create_and_draw()

        self.wait(1)
