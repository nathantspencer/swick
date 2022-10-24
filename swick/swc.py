from .tree import Tree


class SWC:
    r"""
    A representation of the ``.swc`` file, which can contain one or more
    tree-like structures (``Tree``\s), each containing some number of connected
    ``Node``\s.

    The ``trees`` field contains a list of these ``Tree``\s.
    """

    def __init__(self, trees: list[Tree]):
        self.trees = trees
