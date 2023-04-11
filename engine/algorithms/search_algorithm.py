from engine.problems.problem import Problem, StatisticsProblemDecorator
from engine.core.node import Node


class SearchAlgorithm:

    def search(self, problem: Problem | StatisticsProblemDecorator) -> Node:
        raise NotImplementedError
