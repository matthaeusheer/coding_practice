import pytest

from algorithms.linkedlists.reverse import LinkedList


# --- Helper functions -------------------------------------------------------

def to_list(ll: LinkedList) -> list[int]:
    """Collect the linked list's values into a Python list, head first."""
    values = []
    node = ll.head
    while node is not None:
        values.append(node.data)
        node = node.next
    return values


def make_list(values: list[int]) -> LinkedList:
    """Build a LinkedList whose values appear in the given order, head first."""
    ll = LinkedList()


    # Reverse since values = [2, 4, 5] and head needs to be last to visit being prepended
    for value in reversed(values):
        ll.prepend(value)
    return ll


# --- prepend -----------------------------------------------------------------

def test_prepend_builds_in_reverse_insertion_order():
    ll = LinkedList()
    ll.prepend(5)
    ll.prepend(1)
    ll.prepend(2)
    assert to_list(ll) == [2, 1, 5]


def test_prepend_onto_empty_sets_head():
    ll = LinkedList()
    ll.prepend(42)
    assert ll.head is not None
    assert ll.head.data == 42
    assert ll.head.next is None


def test_make_list_helper_preserves_order():
    assert to_list(make_list([1, 2, 3])) == [1, 2, 3]


# --- reverse -----------------------------------------------------------------

def test_reverse_multiple_elements():
    ll = make_list([1, 2, 3, 4])
    ll.reverse()
    assert to_list(ll) == [4, 3, 2, 1]


def test_reverse_single_element_is_unchanged():
    ll = make_list([7])
    ll.reverse()
    assert to_list(ll) == [7]


def test_reverse_empty_list_stays_empty():
    ll = LinkedList()
    ll.reverse()
    assert ll.head is None
    assert to_list(ll) == []


def test_reverse_is_involutive():
    """Reversing twice returns the original order."""
    ll = make_list([1, 2, 3, 4, 5])
    ll.reverse()
    ll.reverse()
    assert to_list(ll) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ],
)
def test_reverse_parametrized(values, expected):
    ll = make_list(values)
    ll.reverse()
    assert to_list(ll) == expected


def test_reverse_reconneicts_tail_to_none():
    """After reversal the new tail (old head) must terminate the list."""
    ll = make_list([1, 2, 3])
    ll.reverse()
    node = ll.head
    assert node is not None  # list is non-empty; also narrows Node | None -> Node
    while node.next is not None:
        node = node.next
    assert node.data == 1  # old head is now the tail
    assert node.next is None

