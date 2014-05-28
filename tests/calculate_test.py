from calculate import calculate


def test_basic_operators():
    assert calculate('5+5') == 10
    assert calculate('5*5') == 25
    assert calculate('10/2') == 5
    assert calculate('10-4') == 6
    assert calculate('10%4') == 2

    assert calculate('7/3') == 2
    assert calculate('5-10') == -5


def test_operator_precedence():
    # Test Precedence of operators
    assert calculate('2+7*2') == 16
    assert calculate('4-7/3') == 2
    assert calculate('4+5%3') == 6


def test_parentheses():
    assert calculate('7+(5*2)') == 17
    assert calculate('7*(5+2)') == 49
    assert calculate('(7*3)+(10/3)') == 24
    assert calculate('7+(7*(6+10/(1*2)))') == 84