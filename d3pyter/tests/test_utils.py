from d3pyter.d3pyter import sigma, Sigma, d3, D3


def test_docstrings_copied():
    assert sigma.__doc__ != ''
    assert sigma.__doc__ == Sigma.__doc__
    assert d3.__doc__ == D3.__doc__
    assert d3.__doc__ != ''
