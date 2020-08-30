import pandas as pd
import snapshottest
from io import StringIO
from snapshottest.file import FileSnapshot

def test1(snapshot):
    path_save = "tests/data/iris_info.csv"
    df: pd.DataFrame = pd.read_csv("data/iris.csv")
    df.describe().reset_index().to_csv(path_save)
    snapshot.assert_match(FileSnapshot(path_save), "iris_info")

def test2(snapshot):
    df: pd.DataFrame = pd.read_csv("data/iris.csv")
    csv_buffer = StringIO()
    df.describe().reset_index().to_csv(csv_buffer, index=False)
    snapshot.assert_match(csv_buffer.getvalue(), "iris_info2")
