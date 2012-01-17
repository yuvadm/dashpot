#!/usr/bin/env python

from kademlia.node import Node

print "Starting dashpot..."

node = Node()
node.joinNetwork()

print "Shutting down..."
