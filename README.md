## Algorithm
1. 알고리즘 풀이
2. 문제 풀이에 쓰이는 문법 간단 정리

## 기본 입출력

### 입력
1. 표준 입력 방법
 - input()
   한 줄의 문자열을 입력 받는 함수
 - int(input())
   문자열을 입력 받아 int 형으로 변환

2. 여러 데이터 입력 방법
 - input().split()
   - 공백을 기준으로 구분된 데이터를 입력 받음 (위 코드 기준)
 - map(int, input().split())
   - 공백을 기준으로 구분된 데이터를 입력 받아 모두 int 형으로 변환
   - map()은 리스트의 모든 원소에 특정 함수를 적용할 때 사용
   - ex) a, b = map(int, input().split())
     입력된 데이터의 개수가 많지 않을 때 사용
   - ex) data = list(map(int, input().split())
     입력된 데이터를 리스트에 저장할 때 사용

3. 빠르게 입력 받기
 - sys.stdin.readline().rstrip()
  - sys 라이브러리에 있는 sys.stdin.readline() 사용
  - 입력 후 Enter는 개행 문자로 입력되므로 rstrip() 함께 사용

### 출력
1. 출력 시 줄 바꿈 하지 않기
 - print('', end="")
  - print()는 기본적으로 출력 이후 줄 바꿈 수행
  - 'end' 속성을 이용해 줄 바꿈을 하지 않을 수 있음
