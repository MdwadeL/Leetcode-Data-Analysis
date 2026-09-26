# Python Script Formatting
LeetCode: problem name

Skills:
- skill #1
- skill #2
- skill #3

solution:
import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:

    result = world[
        (world["area"] >= 3000000) |
        (world["population"] >= 25000000)
    ]

    return result[["name", "population", "area"]]
