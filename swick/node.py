class Node:
    """
    A single node in an SWC structure, which is represented by a single line in
    the ``.swc`` file.

    The ``type`` is an integer that corresponds to a enumeration describing
    the structure being represented by the node.

    The ``x``, ``y``, and ``z`` fields describe the 3D position of the node in
    space, in the prescribed units for the file.

    The ``radius`` field describes the radius of the sphere used to represent
    the volume of the node.

    The ``parentID`` field describes the unique ID of another node that is the
    "parent"  of this node: a connected node that is one step closer to the
    root node of the object. A root node has no parent, and will use a value
    ``-1`` for this field.
    """

    def __init__(self, type: int, x: float, y: float, z: float, radius: float,
                 parent_id: int):
        self.type = type
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.parent_id = parent_id
