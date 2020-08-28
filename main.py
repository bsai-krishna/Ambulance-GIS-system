from Ambulance import Ambulance
from RoadMap import RoadMap
import networkx as nx
import csv
import math
import simpy
import matplotlib.pyplot as plt

fig = plt.figure()


def find_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def main_function(source,destination,ambulance_speed):

    def generate_graph():
        myGraph = nx.Graph()

        # context manager, so that when we are done reading the file, it is closed
        with open("points.csv", "r") as f:
            points = csv.reader(f)

        # to skip the first row containing headers
            next(points)

            for row in points:
                myGraph.add_node((int(row[0]), int(row[1])), traffic_cong=int(row[2]),name=row[6])

        with open("roads.csv", "r") as f:
            roads = csv.reader(f)
            next(roads)
            for row in roads:
                p1 = (int(row[1]), int(row[2]))
                p2 = (int(row[3]), int(row[4]))
                distance = find_distance(p1, p2)
                myGraph.add_edge(p1, p2, weight=distance)
        return myGraph


    myGraph = generate_graph()

# main execution code
    env = simpy.rt.RealtimeEnvironment(factor=0.1, strict=False)
    my_road = RoadMap(myGraph)
    my_ambulance = Ambulance(env, my_road, ambulance_speed, source, destination) # roadmap should have been drawn
    my_ambulance.env.process(my_ambulance.drive_to_destination())
    my_ambulance.env.run()


