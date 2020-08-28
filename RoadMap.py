import networkx as nx
import random


class RoadMap(object):
    def __init__(self, graph):
        self.graph = graph

    def update_congestion(self):
        for node in self.graph.nodes.data():
            node[1]['traffic_cong'] = random.randint(0, 100)

    def find_path_cost(self, path):
        path_cost = 0
        for i in range(len(path) - 1):
            path_cost += (self.graph.edges[path[i], path[i + 1]])[
                'weight']  # graph.edges[path[i], path[i+1]] returns a dictionary

        return path_cost

    def find_path_traffic(self, path):
        path_traffic = 0
        for i in range(len(path) - 1):
            path_traffic += self.graph.nodes[path[i]]['traffic_cong']
        return path_traffic

    def find_cost_of_all_path(self, source, destiny):
        path_costs = {}
        if nx.has_path(self.graph, source, destiny):

            # possible path is a generator object
            possible_path = nx.all_simple_paths(self.graph, source, destiny)
            path_costs = {}
            for path in possible_path:
                path_costs[tuple(path)] = [self.find_path_cost(path),
                                           self.find_path_traffic(path)]

        else:
            # you can throw exception if you want
            print("No path exists")
        return path_costs

    def select_best_path(self, source, destiny):
        path_with_cost_traffic = self.find_cost_of_all_path(source, destiny)

        if len(path_with_cost_traffic):
            max_path_cost = max(path_with_cost_traffic.values(), key=lambda v: v[0])[0]

            for path, cost_traffic in path_with_cost_traffic.items():
                # normalizing path cost
                normalized_path_cost = (cost_traffic[0] / max_path_cost) * 100
                total_cost = 0.5 * normalized_path_cost + cost_traffic[1] * 2
                cost_traffic.append(total_cost)

            # min function only returns a single value even if multiple min exists. So, no handling is done.
            min_tot_cost_path = min(path_with_cost_traffic.items(), key=lambda x: x[1][2])
            return min_tot_cost_path[0]
        else:
            print("No path exists")
            return tuple()
