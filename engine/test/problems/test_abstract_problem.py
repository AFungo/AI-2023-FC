import pytest

from engine.problems.abstract_problem import CountNodes
from engine.problems.practica_1.n_puzzle import NPuzzle, NPuzzleState


def test_count_node_initial_state():
    initial_state = NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0), 3)
    count_node = CountNodes(NPuzzle(initial_state))
    assert count_node.initial_state() == initial_state


def test_count_node_goal_state():
    initial_state = NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0), 3)
    count_node = CountNodes(NPuzzle(initial_state))
    assert count_node.goal_state() is None


def test_count_node_actions():
    initial_state = NPuzzleState((1, 2, 3, 4, 0, 6, 7, 8, 5), 3)
    count_node = CountNodes(NPuzzle(initial_state))
    assert [str(obj) for obj in count_node.actions(initial_state)] == ['Move up', 'Move down', 'Move left', 'Move right']


def test_count_node_result():
    initial_state = NPuzzleState((1, 2, 3, 4, 0, 6, 7, 8, 5), 3)
    count_node = CountNodes(NPuzzle(initial_state))
    move_up = count_node.actions(initial_state)[0]
    move_down = count_node.actions(initial_state)[1]
    move_left = count_node.actions(initial_state)[2]
    move_right = count_node.actions(initial_state)[3]
    assert count_node.result(initial_state, move_up) == NPuzzleState((1, 0, 3, 4, 2, 6, 7, 8, 5), 3)
    assert count_node.result(initial_state, move_down) == NPuzzleState((1, 2, 3, 4, 8, 6, 7, 0, 5), 3)
    assert count_node.result(initial_state, move_left) == NPuzzleState((1, 2, 3, 0, 4, 6, 7, 8, 5), 3)
    assert count_node.result(initial_state, move_right) == NPuzzleState((1, 2, 3, 4, 6, 0, 7, 8, 5), 3)


def test_count_node_goal_test_false():
    initial_state = NPuzzleState((1, 2, 3, 4, 0, 6, 7, 8, 5), 3)
    count_node = CountNodes(NPuzzle(initial_state))
    assert not count_node.goal_test(initial_state)
    assert count_node.explored_node == 1


def test_count_node_goal_test_true():
    initial_state = NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0), 3)
    count_node = CountNodes(NPuzzle(initial_state))
    assert count_node.goal_test(initial_state)
    assert count_node.explored_node == 1


def test_count_node_path_cost():
    initial_state = NPuzzleState((1, 2, 3, 4, 0, 6, 7, 8, 5), 3)
    count_node = CountNodes(NPuzzle(initial_state))
    move_up = count_node.actions(initial_state)[0]
    move_down = count_node.actions(initial_state)[1]
    move_left = count_node.actions(initial_state)[2]
    move_right = count_node.actions(initial_state)[3]
    assert count_node.path_cost(0, initial_state, move_up, count_node.result(initial_state, move_up)) == 1
    assert count_node.path_cost(0, initial_state, move_down, count_node.result(initial_state, move_down)) == 1
    assert count_node.path_cost(0, initial_state, move_left, count_node.result(initial_state, move_left)) == 1
    assert count_node.path_cost(0, initial_state, move_right, count_node.result(initial_state, move_right)) == 1


