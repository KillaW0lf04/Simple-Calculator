from calculate import calculate


def test_calculate():
    assert calculate('5+5') == 10
    assert calculate('5*5') == 25
    assert calculate('10/2') == 5
    assert calculate('10-4') == 6
    assert calculate('10%4') == 2

    assert calculate('7/3') == 2
    assert calculate('5-10') == -5

    assert calculate('2+7*2') == 16
    assert calculate('4-7/3') == 2
    assert calculate('4+5%3') == 6
