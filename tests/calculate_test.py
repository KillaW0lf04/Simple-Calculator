from calculate import calculate


def test_basic_operators():
    assert calculate('5+5') == 10
    assert calculate('5*5') == 25
    assert calculate('10/2') == 5
    assert calculate('10-4') == 6
    assert calculate('10%4') == 2

    assert calculate('6/3') == 2
    assert calculate('5-10') == -5

    assert calculate('55+20') == 75


def test_operator_precedence():
    # Test Precedence of operators
    assert calculate('2+7*2') == 16
    assert calculate('4-6/3') == 2
    assert calculate('4+5%3') == 6


def test_parentheses():
    assert calculate('7+(5*2)') == 17
    assert calculate('7*(5+2)') == 49
    assert calculate('(7*3)+(9/3)') == 24
    assert calculate('7+(7*(6+10/(1*2)))') == 84


def test_whitespaces():
    assert calculate('5 + 5') == 10
    assert calculate('5+5 -3') == 7
    assert calculate('5     +  9') == 14

    assert calculate('5\t+6') == 11
    assert calculate('8\n+5+  7') == 20


def test_floating_point():
    assert calculate('10/4') == 2.5
    assert calculate('5.5*2') == 11
    assert calculate('100/3') - 33.33 < 0.1
    assert calculate('5.5+3.5') == 9
    assert calculate('3.4-1.4') == 2
