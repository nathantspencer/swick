from .node import Node


class Object:
    """
    A group of connected nodes which form a tree structure. For each root node
    in a given ``.swc`` file, there will be one ``Object``.

    The ``nodes`` field contains a dictionary mapping a unique ID to each
    ``Node`` in the ``Object``.
    """

    def __init__(self, nodes: dict[int, Node]):
        self.nodes = nodes
