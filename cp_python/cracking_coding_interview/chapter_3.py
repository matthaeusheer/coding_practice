def exc1_three_in_one():
    """Describe how you could use a single array to implement three stacks.
    Idea:
            First we should think about how to implement a single stack with a single array, then expand to three.
            Single: Basically I'd chose an array size and have a index to the last element which is not None. Elements
            are being added to the back of the array by setting the value at position last + 1 and removed by un-setting
            element last. Those are O(1) operations. When the stack is full and an element is being added, double
            the size of the underlying array by creating a new array and copying things over.

            Triple: For having three stacks implemented, we need to subdivide the array into three compartments, each
            of which holds the data for a single stack. The subdivision in terms of index ranges looks as follows.
            s1 = [0, n/3)
            s2 = [n/3, 2n/3)
            s3 = [2n/3, n]
            One issue is the stacks could be very unbalanced, leading to early new space requirements even though
            most of the space is unused. Also the actual increase of space is more complicated since we have to track
            all sub arrays.
    """


def exc2_stack_with_min():
    raise NotImplementedError('This is implemented in data_structures/stack.py')


def exc3_stack_of_plates():
    raise NotImplementedError

