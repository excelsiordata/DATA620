graphlab.get_dependencies()

import graphlab as gl
gl.canvas.set_target('ipynb')

vertices = gl.SFrame.read_csv('https://raw.githubusercontent.com/excelsiordata/DATA620/master/krackhardt_vertices.csv')
edges = gl.SFrame.read_csv('https://raw.githubusercontent.com/excelsiordata/DATA620/master/krackhardt_edges.csv')
vertices.show()
edges.show()
g = gl.SGraph()
g = g.add_vertices(vertices=vertices, vid_field='name')

g = g.add_edges(edges=edges, src_field='src', dst_field='dst')

g.get_vertices()
g.get_edges()

pr = gl.pagerank.create(g)

pr.get('pagerank').topk(column_name='pagerank')

print g

g.show(vlabel='id', highlight=['Diane'], arrows=True)