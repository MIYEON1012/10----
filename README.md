# Python 프로그래밍 실습

## 핵심코드

* **딕셔너리 정의 및 생성**: 중괄호 `{}`를 사용하거나 `dict()`, `zip()` 함수 등을 활용한 다양한 딕셔너리 생성 방법 학습.
* **키-값 접근/할당**: 대괄호 `[]`를 사용하여 특정 키의 값에 접근하거나 값을 수정 및 추가하는 방법.
* **딕셔너리 메서드**: `update()`, `setdefault()`, `pop()`, `clear()`, `get()` 등 주요 메서드의 기능 및 사용법 실습.
* **반복문 활용**: `items()`, `keys()`, `values()` 메서드를 활용하여 딕셔너리 요소를 순회하는 방법.
* **딕셔너리 표현식 (Comprehension)**: 조건문(`if`)을 포함하여 딕셔너리를 간결하게 생성/필터링하는 기법 적용.

## 과제 문제 풀이 (#25 ~ #31)

### 1. **생성 및 변환**
**\#25**
- `zip()`과 `dict()`을 활용한 딕셔너리 생성 및 `del`로 요소 삭제
- `my = dict(zip(keys, values))`

### 2. **접근 및 수정**
**\#26**
- 딕셔너리 키로 값 접근
- `park['english']`

**\#27**
- 반복문을 이용한 모든 값 일괄 수정
- `kim[subject] = 100`

### 3. **확인 및 삭제**

**\#28**
- `in` 연산자로 키 존재 여부 확인 및 `del`로 삭제
- `if 'english' in lee: del lee['english']`

### 4. **반복 및 계산**

**\#29** `items()`를 이용한 키-값 동시 출력
- `for key, value in lim.items():`

**\#30**
- Dictionary Comprehension으로 조건부 필터링
- `{key: value for... if value >= 90}`

**\#31**
- `values()`, `sum()`, `len()`을 이용한 평균 계산
- `sum(yoo.values()) / len(yoo)`

## 과제를 통해 배운 점

- Key는 값이 변하지 않는 자료형(문자열, 숫자, 튜플)만 사용 가능하며, 리스트/딕셔너리는 Key로 쓸 수 없다.
- update()는 수정/추가 모두 되지만, setdefault()는 추가만 되고 이미 있는 값은 수정하지 못한다.
- pop(키)는 특정 키를 삭제하고 값을 반환하며, popitem()은 마지막 쌍을 삭제하고 (키, 값) 튜플을 반환한다.
- copy()는 중첩 딕셔너리에서 얕은 복사이며, 완전히 독립적인 복사본은 copy.deepcopy()를 사용해야 한다.
- .items()로 키-값 쌍을, .keys()로 키만, .values()로 값만 추출하여 반복할 수 있다.

## GitHub Repository URL
- https://github.com/MIYEON1012/10----.git