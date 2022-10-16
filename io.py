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


def parse_int(value: str,  name: str, min_value: int, file_name: str,
              line_number: int,):
    """
    Attempts to interpet a given string ``value`` as an integer,
    returning the integer on success and raising an ``SWCFormatError``
    on failure.

    :parameter value: the string value to be parsed
    :parameter name: the name of the field being parsed
    :parameter min_value: minimum valid integer value
    :parameter file_name: the name of the file being read
    :parameter line_number: the line where the value occurs
    :return: an integer interpretation of the value
    """

    try:
        assert value.isdigit()
        int_value = int(value)
        assert int_value >= min_value
        return int_value
    except AssertionError:
        raise SWCFormatError(f"Could not read {file_name}. Line"
                             f" {line_number} has {name} with value"
                             f" \"{value}\"; expected an integer"
                             f" greater than {min_value - 1}.")


def parse_float(value: str,  name: str, file_name: str, line_number: int,):
    """
    Attempts to interpet a given string ``value`` as a float, returning the
    float on success and raising an ``SWCFormatError`` on failure.

    :parameter value: the string value to be parsed
    :parameter name: the name of the field being parsed
    :parameter file_name: the name of the file being read
    :parameter line_number: the line where the value occurs
    :return: a float interpretation of the value
    """

    try:
        return float(value)
    except ValueError:
        raise SWCFormatError(f"Could not read {file_name}. Line"
                             f" {line_number} has {name} with value"
                             f" \"{value}\"; expected a float.")


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

        id = parse_int(fields[0], "ID", 1, path, line_number)
        type = parse_int(fields[1], "type", 0, path, line_number)
        x = parse_float(fields[2], "x position", path, line_number)
        y = parse_float(fields[3], "y position", path, line_number)
        z = parse_float(fields[4], "z position", path, line_number)
        radius = parse_float(fields[5], "radius", path, line_number)
        parent_id = parse_int(fields[6], "parent ID", -1, path, line_number)

        # TODO: parse remaining fields
