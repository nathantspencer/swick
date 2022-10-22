from .node import Node


class Tree:
    """
    A group of connected nodes which form a tree structure. For each root node
    in a given ``.swc`` file, there will be one ``Tree``.

    The ``nodes`` field contains a dictionary mapping a unique ID to each
    ``Node`` in the ``Tree``.
    """

    def __init__(self, nodes: dict[int, Node]):
        self.nodes = nodes
