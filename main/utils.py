import pandas as pd

from engine.engine import UninformedAlgorithms, InformedAlgorithms


def algorithm_parser(self, name):
    try:
        algorithm = UninformedAlgorithms.__members__[name]
    except KeyError:
        try:
            algorithm = InformedAlgorithms.__members__[name]
        except KeyError:
            raise Exception("Algorithm not supported")
    return algorithm


def export_data(solution, file_name):
    df = pd.DataFrame(solution, index=[0])
    df.to_csv(file_name, mode='a', header=False, index=False)

