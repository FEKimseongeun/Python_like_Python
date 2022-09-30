## ****2차원 리스트를 1차원 리스트로 만들기 - from_iterable****

> 이차원 리스트를 일차원 리스트로 만들어야 할 때
>

아무것도 모른다면 보통은,

```python
my_list = [[1, 2], [3, 4], [5, 6]]
answer = []
for element in my_list:
    answer += element
```

이렇게 작성하곤 한다.

### 파이썬에서는 for문을 사용하지 않고도 리스트를 이어붙여 1차원 리스트로 만들 수 있다.

```python
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))
```

---

**제한적으로 사용 가능한 방법**

### 각 원소의 길이가 동일한 경우에만 사용 가능

```python
# 방법 7 - numpy 라이브러리의 flatten 이용
import numpy as np
np.array(my_list).flatten().tolist()
```

예를 들어 다음과 같은 리스트는 편평하게 만들 수 있고

- `[[1], [2]]`
- `[[1, 2], [2, 3], [4, 5]]`

다음과 같이 같이 **각 원소의 길이가 다른 리스트는 편평하게 만들 수 없습니다.**

- `[['A', 'B'], ['X', 'Y'], ['1']]`

→ 이걸로 사용하면

```
VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
  answer=np.array(my_list).flatten().tolist()
```

이런 에러가 뜬다!