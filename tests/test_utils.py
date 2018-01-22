from bitshares.utils import assets_from_string


def test_assets_from_string():
    assert assets_from_string('USD:CYB') == ['USD', 'CYB']
    assert assets_from_string('BTSBOTS.S1:CYB') == ['BTSBOTS.S1', 'CYB']
