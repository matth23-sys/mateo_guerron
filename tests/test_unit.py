import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import add

def test_add_ok():
    assert add(2, 2) == 4
    assert add(-1, 3) == 2
