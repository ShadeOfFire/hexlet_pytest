from hexlet_pytest.example import reverse
import pytest


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'

def test_reverse_for_empty_string():
    assert reverse('') == ''

def test_stack():
    stack = []
# Добавляем два элемента в стек и затем извлекаем их
# Почему два? Так надежнее, чем один, а три скорее всего избыточно
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'


def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()
