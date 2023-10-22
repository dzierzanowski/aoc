#!python3

with open('input.txt') as file:
    input_lines = file.read().splitlines()

class Model:

    inf = 1000000000000000000000000000000000000000000

    def __init__(self, input_lines):
        edges = {}
        vertices = {}
        
        for line in input_lines:
            vertex_def, edge_def = [ half.split(maxsplit=4) for half in line.split('; ') ]
            vertex_id = vertex_def[1]
            vertex_rate = int(vertex_def[-1].split('=')[-1])
            vertex_neighbors = edge_def[-1].split(', ')
            vertices[vertex_id] = {
                'rate': vertex_rate,
                'neighbors': vertex_neighbors
            }
            edges[(vertex_id, vertex_id)] = 0
            for neighbor_id in vertex_neighbors:
                edges[(vertex_id, neighbor_id)] = 1
        
        for vertex_start in vertices:
            for vertex_end in vertices:
                edge = (vertex_start, vertex_end)
                if not edge in edges:
                    edges[edge] = self.inf
        
        for middle in vertices:
            for start in vertices:
                for end in vertices:
                    edges[(start, end)] = min(
                        edges[(start, end)],
                        edges[(start, middle)] + edges[(middle, end)]
                    )


        self.edges = edges
        self.vertices = vertices
    
    def inspect_vertex(self, vertex, time_remaining, vertices_remaining: set):
        vertex_data = self.vertices[vertex]
        rate = vertex_data['rate'] * time_remaining
        best_result = 0
        for vertex_next in vertices_remaining:
            vertices_remaining_next = vertices_remaining - { vertex_next }
            dist = self.edges[(vertex, vertex_next)] + 1
            if time_remaining - dist < 1:
                continue
            result = self.inspect_vertex(vertex_next, time_remaining - dist, vertices_remaining_next)
            best_result = max(best_result, result)
        return rate + best_result
    
    def run(self):
        first_vertex = 'AA'
        remaining = { vertex for vertex, data in self.vertices.items() if data['rate'] }
        return self.inspect_vertex(
            vertex=first_vertex,
            time_remaining=30,
            vertices_remaining=remaining
        )

model = Model(input_lines)

result = model.run()
print(f'Result: {result}')
