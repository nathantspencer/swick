from ast import Assert
from . import swc

import re


class SWCFormatError(Exception):
    """
    Error thrown during reading or writing of ``.swc`` files in
    cases in which the format is not or cannot be properly
    adhered to.
    """
    pass


def read_swc(path: str):
    """
    Reads an ``.swc`` file to create and return an ``SWC`` object.

    :parameter path: the path to the ``.swc`` file to be read
    :return: an ``SWC`` object containing the loaded data
    """

    swc_file = open(path, 'r')
    line_number = 0
    for line in swc_file:
        line_number = line_number + 1

        # ignore empty, white-space only, and comment lines
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        fields = re.split(r'[\t ]+', line)
        if len(fields) != 7:
            raise SWCFormatError(f"Could not read {path}. Line"
                                 f" {line_number} contains"
                                 f" {len(fields)} fields;"
                                 f" expected 7 fields.")

        try:
            assert fields[0].isdigit()
            id = int(fields[0])
        except AssertionError:
            raise SWCFormatError(f"Could not read {path}. Line"
                                 f" {line_number} has ID with"
                                 f" value {fields[0]};"
                                 f" expected an integer.")

        # TODO: error checking on these fields
        type = int(fields[1])
        x = float(fields[2])
        y = float(fields[3])
        z = float(fields[4])
        radius = float(fields[5])
        parent_id = int(fields[6])
