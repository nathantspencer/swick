from .node import Node
from .swc import SWC


def split_swc(swc: SWC):
    """
    Splits an ``SWC`` object into one or more ``SWC`` objects, each containing
    a single root node. Node IDs are not modified by this process.

    :parameter swc:
        the ``SWC`` object to be split

    :return:
        a list of ``SWC`` objects each containing one root node
    """

    # first pass to create map from parent ID to child IDs
    root_nodes = []
    parent_id_to_child_ids = {}
    for id in swc.nodes:
        parent_id = swc.nodes[id].parent_id
        if parent_id == -1:
            root_nodes.append(id)
        elif parent_id in parent_id_to_child_ids:
            parent_id_to_child_ids[parent_id].append(id)
        else:
            parent_id_to_child_ids[parent_id] = [id]

    # second pass using DFS to separate connected components
    swcs = []
    for root_id in root_nodes:
        parent_id_stack = [root_id]
        nodes = {root_id : root_nodes[root_id]}

        while parent_id_stack:
            parent_id = parent_id_stack.pop()
            if parent_id not in parent_id_to_child_ids:
                continue
            for child_id in parent_id_to_child_ids[parent_id]:
                nodes[child_id] = swc.nodes[child_id]
                parent_id_stack.append(child_id)
            nodes.pop(parent_id)

        swcs.append(SWC(nodes))

    # TODO: if anything is left in nodes, throw exception for unreachable nodes
    # add exception to documentation

    return swcs


def combine_swcs(swcs: list[SWC]):
    r"""
    Combines each of the ``SWC`` objects in the list into a single ``SWC``.
    Node IDs for all but the first ``SWC`` in the list may be modified by
    this process in order to avoid collisions between node IDs: for each
    ``SWC`` in the list, the node IDs it contains will be offset by the
    greatest node ID in the previous ``SWC``.

    :parameter swcs:
        a list of ``SWC`` objects to be combined

    :return:
        a single ``SWC`` object containing all ``Tree``\s from the input
    """

    # TODO: reimplement
