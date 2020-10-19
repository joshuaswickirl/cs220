from PA2 import eval_tt_f2, equivalent
from PA1 import *

def test_eval_tt_f2():
    r = eval_tt_f2(iff)
    assert r == [[False, False, True], [False, True, False], [True, False, False], [True, True, True]]

def test_equivalent():
    r = equivalent(implies, nqIMPnp)
    assert r == True