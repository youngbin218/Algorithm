## Algorithm

##### 알고리즘 풀이에 쓰이는 지식, 문법 간단 정리

---------------------

#### 파이썬 자료형 별 연산자 시간 복잡도

#### List
|Operation|Example|Big-O|Description|
|---|---|---|---|
|Delete|del arr[idx]|O(N)|idx 위치의 요소 삭제|
|Remove|arr.remove(val)|O(N)|val 값을 가지는 요소 삭제|

#### Dictionary
|Operation|Example|Big-O|Description|
|---|---|---|---|
|Delete|del arr[key]|O(1)|해당 key-value 쌍 삭제|

##### [7785번](https://www.acmicpc.net/problem/7785)
> ##### 문제 조건 : 시간 제한 (1초) / 메모리 제한 (256MB) / 입력 되는 n의 범위 (2 ≤ n ≤ 10^6)
> ##### Error : 시간 초과
> ##### -> List 사용 시 Delete, Remove의 시간 복잡도가 O(N)
> ##### -> Delete의 시간 복잡도가 O(1)인 Dictionary 사용

#### 아스키 코드 변환

#### Int -> ASCII
> ##### chr(int) : int에 해당하는 ASCII 문자로 변환

#### ASCII -> Int
> ##### ord(str) : str에 해당하는 숫자로 변환

##### [10809번](https://www.acmicpc.net/problem/10809)
