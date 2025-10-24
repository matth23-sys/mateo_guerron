import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import add

def test_add_should_fail_initially():
    # Falla intencionalmente
    assert add(2, 2) == 5
