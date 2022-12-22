The Structure of an SWC
=======================


SWCs, Trees, and Nodes
----------------------

The :doc:`SWC object <../api_documentation/swc>` represents a single SWC file.

Often times SWC files contain just one object (and therefore one root node), but some files contain multiple objects, each a tree-like structure with its own root node.
We'll call those objects :doc:`Trees <../api_documentation/tree>`.

In this example we'll read an SWC and print the number of trees it contains: ::

  import swick

  my_swc = swick.read_swc('path/to/swc_file.swc')
  
  print(len(swick.trees))

Each tree contains a dictionary mapping IDs to :doc:`Node objects <../api_documentation/node>`.
These nodes describe the 3D points that make up the tree, their radii and type specifiers, and the connection to their parent node (except in the case of a root node).