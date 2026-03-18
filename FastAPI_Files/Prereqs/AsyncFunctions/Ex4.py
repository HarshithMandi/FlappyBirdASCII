from typing import List
from typeguard import typechecked

@typechecked
def gettotal(numbers: List[int]) -> int:
    return (numbers[0] )

print(gettotal([1, 2, 3, 4, 5]))
print(gettotal([10, "20", 30]))