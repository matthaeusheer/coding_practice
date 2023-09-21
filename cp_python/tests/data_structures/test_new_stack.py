import pytest

from data_structures.new_stack import Stack, LinkedListStack, ArrayStack


def _create_empty_linked_list_stack() -> LinkedListStack:
    return LinkedListStack()


def _create_empty_array_stack() -> ArrayStack:
    return ArrayStack()


@pytest.mark.parametrize("stack", [_create_empty_linked_list_stack(), _create_empty_array_stack()])
def test_is_empty_for_new_stack(stack: Stack):
    assert stack.is_empty()


@pytest.mark.parametrize("stack", [_create_empty_linked_list_stack(), _create_empty_array_stack()])
def test_pop_throws_error_for_empty_stack(stack: Stack):
    pytest.raises(RuntimeError, stack.pop)


@pytest.mark.parametrize("stack", [_create_empty_linked_list_stack(), _create_empty_array_stack()])
def test_peek_throws_error_for_empty_stack(stack: Stack):
    pytest.raises(RuntimeError, stack.peek)


@pytest.mark.parametrize("stack", [_create_empty_linked_list_stack(), _create_empty_array_stack()])
def test_push_adds_item_for_empty_stack(stack: Stack):
    value = 5
    stack.push(value)
    assert stack.peek() == value
    assert stack.pop() == value


@pytest.mark.parametrize("stack", [_create_empty_linked_list_stack(), _create_empty_array_stack()])
def test_push_adds_item_for_non_empty_stack(stack: Stack):
    first_value = 3
    second_value = 6
    stack.push(first_value)
    stack.push(second_value)
    assert not stack.is_empty()
    assert stack.peek() == second_value
    assert stack.pop() == second_value
    assert stack.peek() == first_value
    assert stack.pop() == first_value
    assert stack.is_empty()
