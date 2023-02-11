The Structure of an SWC
=======================


SWCs and Nodes
--------------

The :doc:`SWC object <../api_documentation/swc>` represents a single SWC file.

In this example we'll read an SWC and print the number of nodes it contains: ::

  import swick

  my_swc = swick.read_swc('path/to/swc_file.swc')
  
  print(len(my_swc.nodes))

These nodes describe the 3D points that make up the tree, their radii and type specifiers, and the connection to their parent node (except in the case of a root node, which has no parent).

Often times SWC files contain just one object (and therefore one root node), but some files contain multiple disconnected objects, each a tree-like structure with its own root node.

The ``SWC`` attribute ``nodes`` is a dictionary that maps IDs to :doc:`Node objects <../api_documentation/node>`. Each ``Node`` object has its own attributes to retrieve position, type, size, and connection information.