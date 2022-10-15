from . import swc


def read_swc(path: str):
    """
    Reads an ``.swc`` file to create and return an ``SWC`` object.

    :parameter path: the path to the ``.swc`` file to be read
    :return: an ``SWC`` object containing the loaded data
    """

    swc = SWC()
    swc_file = open(path, 'r')
    for line in swc_file:

        # ignore empty, white-space only, and comment lines
        line = line.trim()
        if not line or line.startswith('#'):
            continue
