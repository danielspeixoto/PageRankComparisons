from typing import List
import plotly.plotly as py
from plotly.graph_objs import *
import networkx as nx
from networkx import DiGraph, get_node_attributes, single_source_shortest_path_length, random_geometric_graph
from methods import helpers


def draw(G: DiGraph, ranks: List[float]):
    print("Plotting...")
    pos = nx.spring_layout(G)

    for i in range(len(G.nodes)):
        G.nodes[i]['pos'] = pos[i]
        G.nodes[i]['rank'] = ranks[i]

    edge_trace = Scatter(
        x=[],
        y=[],
        line=Line(width=0.5, color='#888'),
        hoverinfo='none',
        mode='arrows')




    for edge in G.edges():
        x0, y0 = G.node[edge[0]]['pos']
        x1, y1 = G.node[edge[1]]['pos']
        edge_trace['x'] += [x0, x1, None]
        edge_trace['y'] += [y0, y1, None]

    sizes = helpers.ranks_to_int(ranks)
    percents = helpers.ranks_to_percent(ranks)
    node_trace = Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers',
        hoverinfo='text',
        marker=Marker(
            showscale=False,
            # colorscale options
            # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
            # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
            color=[(float(i[:-1]) * 255) ** 3 for i in percents],
            size=sizes,
            line=dict(width=2))
    )

    for node in G.nodes():
        x, y = G.node[node]['pos']
        node_trace['x'].append(x)
        node_trace['y'].append(y)

    for node, adjacency in enumerate(G.adjacency()):
        node_trace['marker']['color'].append(len(adjacency))
        node_info = 'PageRank: ' + percents[node]
        node_trace['text'].append(node_info)
        # node_trace[node]['size'] = G.nodes[node]['size']

    annot = [(
        dict(
            showarrow=True,
            arrowhead=200,
            arrowsize=100,
            arrowwidth=200,
            arrowcolor='#636363',
            x=edge[0],
            y=edge[1],
            xref='x',
            yref='y'
        )
    ) for edge in G.edges()]

    annot.append(dict(
                     showarrow=False,
                     xref="paper", yref="paper",
                     x=0.005, y=-0.002))

    fig = Figure(data=Data([edge_trace, node_trace]),
                 layout=Layout(
                     title='Regular PageRank',
                     titlefont=dict(size=16),
                     showlegend=False,
                     hovermode='closest',
                     margin=dict(b=20, l=5, r=5, t=40),
                     annotations=annot,
                     xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                     yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))

    py.iplot(fig, filename='networkx')
