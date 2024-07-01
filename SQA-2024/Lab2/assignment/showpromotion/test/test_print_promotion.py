import source.print_promotion as promotion
import pytest


def test_TS001_TC01(capsys):
    promotion.print_promotion(total_cost=0)
    captured = capsys.readouterr()
    assert captured.out == 'Thank you and see you next time\nFree ice cream cone = 0\n'

def test_TS002_TC01(capsys):
    promotion.print_promotion(total_cost=150)
    captured = capsys.readouterr()
    assert captured.out == 'Thank you and see you next time\nFree ice cream cone = 0\n'

def test_TS003_TC01(capsys):
    promotion.print_promotion(total_cost=500)
    captured = capsys.readouterr()
    assert captured.out == 'Free ice cream cone = 1.0\n'
    
def test_TS004_TC01(capsys):
    promotion.print_promotion(total_cost=600)
    captured = capsys.readouterr()
    assert captured.out == 'Free ice cream cone = 1.2\n'
    
def test_TS005_TC01(capsys):
    promotion.print_promotion(total_cost=700)
    captured = capsys.readouterr()
    assert captured.out == 'Free chocolate cake = 1.0\n'
    
def test_TS006_TC01(capsys):
    promotion.print_promotion(total_cost=1000)
    captured = capsys.readouterr()
    assert captured.out == 'Free chocolate cake = 1.4285714285714286\n'
    
def test_TS007_TC01(capsys):
    promotion.print_promotion(total_cost=1400)
    captured = capsys.readouterr()
    assert captured.out == 'Free ice cream cone = 1.1666666666666667 and Free chocolate cake = 1.1666666666666667\n'
    
def test_TS008_TC01(capsys):
    promotion.print_promotion(total_cost=-1)
    captured = capsys.readouterr()
    assert captured.out == 'Thank you and see you next time\nFree ice cream cone = 0\n'

def test_TS009_TC01(capsys):
    promotion.print_promotion(total_cost=-1000)
    captured = capsys.readouterr()
    assert captured.out == 'Thank you and see you next time\nFree ice cream cone = 0\n'
    
def test_TS010_TC01(capsys):
    promotion.print_promotion(total_cost = None )
    captured = capsys.readouterr()
    assert captured.out == 'Thank you and see you next time\nFree ice cream cone = 0\n'
    
def test_TS011_TC01(capsys):
    promotion.print_promotion(total_cost = 'hi' )
    captured = capsys.readouterr()
    assert captured.out == 'Thank you and see you next time\nFree ice cream cone = 0\n'
    

