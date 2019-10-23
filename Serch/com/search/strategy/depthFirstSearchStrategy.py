'''
Created on Feb 18, 2019

@author: dr.aarij
'''
from com.search.strategy.searchStrategy import SearchStrategy
from queue import Queue

class DepthFirstSearchStrategy(SearchStrategy):
    '''
    classdocs
    '''
    

    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return (len(self.queue)) == 0

    def addNode(self,node):
        return self.queue.append(node)

    def removeNode(self):
        return self.queue.pop()