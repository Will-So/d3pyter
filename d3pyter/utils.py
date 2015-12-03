
def docstring_copy(from_, to):
    """
    Copies docstrings
    """
    to.__doc__ = from_.__doc__
    return to