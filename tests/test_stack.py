import pytest

from hexlet_pytest.stack import create_stack, push, pop, is_empty

def test_stack():
    stack = create_stack()
    push(stack, 'one')
    push(stack, 'two')
    assert pop(stack) == 'two'
    assert pop(stack) == 'one'

def test_emptiness():
    stack = create_stack()
    assert is_empty(stack)
    push(stack, 'one')
    assert not is_empty(stack)
    pop(stack)
    assert is_empty(stack)

def test_pop_with_empty_stack():
    stack = create_stack()
    with pytest.raises(IndexError):
        pop(stack)