from ..buffers import *


def test_fixed_buffer():
    buffer = FixedLengthBuffer(3)

    assert buffer.can_add
    assert not buffer.can_take

    buffer.add(1)
    buffer.add(2)

    assert buffer.can_add
    assert buffer.can_take

    buffer.add(3)

    assert not buffer.can_add
    assert buffer.can_take

    assert buffer.take() == 1

    assert buffer.can_add
    assert buffer.can_take

    assert buffer.take() == 2
    assert buffer.take() == 3

    assert buffer.can_add
    assert not buffer.can_take


def test_dropping_buffer():
    buffer = DroppingBuffer(2)

    assert buffer.can_add
    assert not buffer.can_take

    buffer.add(1)
    buffer.add(2)

    assert buffer.can_add
    assert buffer.can_take

    assert buffer.take() == 1

    buffer.add(3)
    buffer.add(4)

    assert buffer.take() == 2
    assert buffer.take() == 3

    assert buffer.can_add
    assert not buffer.can_take


def test_sliding_buffer():
    buffer = DroppingBuffer(2)

    assert buffer.can_add
    assert not buffer.can_take

    buffer.add(1)
    buffer.add(2)

    assert buffer.can_add
    assert buffer.can_take

    assert buffer.take() == 1

    buffer.add(3)
    buffer.add(4)

    assert buffer.take() == 3
    assert buffer.take() == 4

    assert buffer.can_add
    assert not buffer.can_take


def test_promise_buffer():
    buffer = PromiseBuffer()

    assert buffer.can_add
    assert not buffer.can_take

    buffer.add(1)

    assert not buffer.can_add
    assert buffer.can_take

    assert buffer.take() == 1

    assert not buffer.can_add
    assert buffer.can_take

    assert buffer.take() == 1
    assert buffer.take() == 1


def test_empty_buffer():
    buffer = EmptyBuffer()

    assert not buffer.can_take
    assert not buffer.can_add