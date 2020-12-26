from .Graph import Graph, Vertex
import heapq

# Unfinished


def dijkstra(aGraph, start):
    priorityQueue = []
    start.setDistance(0)
    for v in aGraph:
        heapq.heappush(priorityQueue, (v.getDistance(), v))
    while len(priorityQueue) != 0:
        currentVert = heapq.heappop(priorityQueue)[0]
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                priorityQueue.decreaseKey(nextVert, newDist)
