from fastapi import Query
from typing import Annotated

def validate_sort_by(sortBy: Annotated[int, Query()] =-1):
    return 1 if sortBy == 1 else -1