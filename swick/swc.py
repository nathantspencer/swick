from .object import Object


class SWC:
    """
    A representation of the ``.swc`` file, which can contain one or more tree-
    like structures (``Object``\s), each containing some number of connected
    ``Node``\s.

    The ``objects`` field contains a list of these ``Object``\s.
    """

    def __init__(self, objects: list[Object]):
        self.objects = objects
