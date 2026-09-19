# Python Study Notes

Python을 공부하며 실습과 프로젝트를 통해 학습한 내용을 정리한 문서입니다.

---

## 1. List

List는 여러 개의 값을 하나로 묶어서 저장할 수 있는 자료형이다.

```python
active_words = []
```

타이핑 게임에서는 현재 화면에 떨어지고 있는 여러 단어를 저장하기 위해 List를 사용했다.

### `append()`

List의 마지막에 새로운 값을 추가한다.

```python
active_words.append(fw)
```

새로운 단어가 화면에 생성되면 `active_words`에 추가한다.

### `remove()`

List에서 특정 값을 삭제한다.

```python
active_words.remove(fw)
```

단어를 맞혔거나 화면 아래로 떨어진 경우 더 이상 활성화된 단어가 아니므로 List에서 제거한다.

### List를 사용한 이유

게임에서는 동시에 여러 개의 단어가 화면에 존재할 수 있다.

```text
active_words
    ↓
[단어1, 단어2, 단어3, 단어4]
```

따라서 여러 개의 단어를 하나씩 관리하기 위해 List를 사용했다.

---

## 2. Dictionary

Dictionary는 `key : value` 형태로 데이터를 저장한다.

```python
fw = {
    "id": word_id,
    "word": word,
    "speed": speed,
    "y": 0
}
```

타이핑 게임에서는 **하나의 단어와 그 단어에 필요한 정보를 묶어서 관리**하기 위해 Dictionary를 사용했다.

| Key       | 의미                 |
| --------- | ------------------ |
| `"id"`    | Canvas에 생성된 글자의 ID |
| `"word"`  | 실제 단어              |
| `"speed"` | 단어가 아래로 이동하는 속도    |
| `"y"`     | 현재 Y 좌표            |

예를 들어:

```python
fw["word"]
```

→ 현재 단어의 문자열을 가져온다.

```python
fw["speed"]
```

→ 현재 단어의 이동 속도를 가져온다.

---

## 3. List + Dictionary

이 게임에서는 List와 Dictionary를 함께 사용했다.

```python
active_words = []
```

여러 개의 단어를 List에 저장하고,

```python
fw = {
    "id": word_id,
    "word": word,
    "speed": speed,
    "y": 0
}
```

각각의 단어에 대한 상세 정보를 Dictionary로 관리한다.

구조를 그림으로 표현하면:

```text
active_words
│
├── Dictionary (단어 1)
│   ├── id
│   ├── word
│   ├── speed
│   └── y
│
├── Dictionary (단어 2)
│   ├── id
│   ├── word
│   ├── speed
│   └── y
│
└── Dictionary (단어 3)
    ├── id
    ├── word
    ├── speed
    └── y
```

즉,

> **List = 여러 단어를 관리**
> **Dictionary = 하나의 단어에 대한 여러 정보를 관리**

---

## 4. for 반복문

List에 들어 있는 데이터를 하나씩 확인할 때 `for`문을 사용할 수 있다.

```python
for fw in active_words:
    print(fw["word"])
```

`active_words`에 단어가 3개 있다면:

```text
첫 번째 단어 확인
↓
두 번째 단어 확인
↓
세 번째 단어 확인
```

타이핑 게임에서는 현재 화면에 존재하는 모든 단어를 확인하기 위해 사용했다.

---

## 5. `break`

`break`는 반복문을 즉시 종료한다.

```python
for fw in active_words:
    if fw["word"] == input_word:
        matched = fw
        break
```

사용자가 입력한 단어와 일치하는 단어를 찾으면 더 이상 다른 단어를 확인할 필요가 없기 때문에 반복문을 종료한다.

예를 들어:

```text
active_words

python
linux
network
python
```

사용자가 `python`을 입력하면 첫 번째 `python`을 찾은 후 `break`가 실행되어 반복문을 끝낸다.

따라서 한 번 입력했을 때 하나의 단어만 처리된다.

---

## 6. `None`

`None`은 **아직 값이 없거나 존재하지 않음**을 나타낼 때 사용할 수 있다.

```python
matched = None
```

이 코드는 처음에는:

> "아직 일치하는 단어를 찾지 못했다."

라는 의미이다.

이후 일치하는 단어를 찾으면:

```python
matched = fw
```

로 변경된다.

### 동작 과정

```text
matched = None
      ↓
단어 검색
      ↓
일치하는 단어 발견
      ↓
matched = fw
```

만약 끝까지 일치하는 단어가 없다면:

```python
matched == None
```

상태로 남는다.

---

## 7. Local Variable과 Global Variable

### Global Variable

함수 밖에서 선언된 변수는 전역 변수(Global Variable)가 될 수 있다.

```python
score_success = 0
score_fail = 0
```

게임 전체에서 성공 횟수와 실패 횟수를 관리하기 위해 사용했다.

### Local Variable

함수 내부에서 만들어진 변수는 기본적으로 해당 함수 안에서 사용하는 지역 변수(Local Variable)이다.

```python
def test():
    x = 20
    print(x)
```

여기서 `x`는 `test()` 함수의 지역 변수이다.

---

## 8. `global`

함수 안에서 전역 변수를 수정하려면 `global`을 사용할 수 있다.

```python
score_success = 0

def check_word(event):
    global score_success

    score_success += 1
```

`global score_success`는

> "이 함수에서 사용하는 `score_success`는 새로운 지역 변수가 아니라 함수 밖에 있는 전역 변수이다."

라는 의미이다.

### 주의

`global`이 변수를 만들어주는 것은 아니다.

```python
score_success = 0
```

먼저 전역 변수가 존재하고,

```python
global score_success
```

함수 안에서 그 전역 변수를 사용하겠다고 선언하는 것이다.

---

## 9. Local과 Global의 차이

다음 코드를 보면:

```python
x = 10

def test():
    x = 20
    print(x)

test()

print(x)
```

결과:

```text
20
10
```

함수 안의 `x`와 함수 밖의 `x`는 서로 다른 변수이기 때문이다.

```text
Global
x = 10

      ↓

test()
 └── Local
     x = 20
```

따라서 함수 안에서 변수에 값을 대입한다고 해서 항상 전역 변수가 변경되는 것은 아니다.

---

## 10. `canvas.move()`

Tkinter Canvas에서 객체를 이동시킬 때 사용하는 메서드이다.

```python
canvas.move(fw["id"], 0, fw["speed"])
```

구조는 다음과 같다.

```python
canvas.move(이동할_객체, x방향_이동량, y방향_이동량)
```

따라서:

```python
canvas.move(fw["id"], 0, fw["speed"])
```

는

* `fw["id"]` → 어떤 Canvas 객체를 이동할 것인지
* `0` → X 방향으로 이동하지 않음
* `fw["speed"]` → Y 방향으로 speed만큼 이동

이라는 의미이다.

단어가 아래로 떨어지는 이유는 Y 방향으로 이동하기 때문이다.

---

## 11. 위치 값과 화면 이동은 별개

게임 코드에는 다음 두 가지가 함께 사용된다.

```python
canvas.move(fw["id"], 0, fw["speed"])
```

그리고

```python
fw["y"] += fw["speed"]
```

둘은 비슷해 보이지만 역할이 다르다.

### `canvas.move()`

실제 Canvas에 표시된 글자의 위치를 이동시킨다.

### `fw["y"] += fw["speed"]`

Dictionary에 저장해 놓은 Y 위치 값을 업데이트한다.

예를 들어:

```text
현재 y = 399
speed = 2
```

실행 후:

```python
fw["y"] += fw["speed"]
```

결과:

```text
399 + 2 = 401
```

그리고:

```python
if fw["y"] > 400:
```

조건이 참이 되어 해당 단어를 실패 처리한다.

---

## 12. `active_words[:]`

다음과 같은 코드가 있었다.

```python
for fw in active_words[:]:
```

여기서 `[:]`는 List 전체를 복사해서 사용하는 것이다.

즉,

```python
active_words[:]
```

는 원래 List와 같은 내용의 새로운 List를 만든다.

### 왜 복사해서 사용하는가?

게임에서는 반복문을 돌면서 동시에 원래 List에서 데이터를 삭제할 수 있다.

```python
for fw in active_words[:]:
    ...
    active_words.remove(fw)
```

반복문은 복사본을 대상으로 실행되고,

```text
반복문 → 복사본
삭제 → 원본 active_words
```

형태가 된다.

따라서 반복문을 실행하면서 원본 List의 내용을 변경할 때 발생할 수 있는 문제를 줄일 수 있다.

---

## 13. `after()`

Tkinter의 `after()`는 일정 시간이 지난 후 특정 함수를 실행하도록 예약한다.

```python
root.after(50, update_game)
```

의미:

> 50ms 후에 `update_game` 함수를 실행한다.

### 반복 실행

`update_game()` 내부에서 다시:

```python
root.after(50, update_game)
```

를 호출한다.

따라서:

```text
update_game()
    ↓
50ms 대기
    ↓
update_game()
    ↓
50ms 대기
    ↓
update_game()
    ↓
...
```

이렇게 반복된다.

이 구조를 이용해서 단어가 계속 움직이는 애니메이션을 만들 수 있다.

---

## 14. `after()`와 게임 애니메이션

게임에서는 다음과 같은 흐름으로 동작한다.

```text
update_game()
     ↓
단어 위치 이동
     ↓
현재 위치 확인
     ↓
화면 아래로 떨어졌는지 확인
     ↓
점수 업데이트
     ↓
50ms 후 update_game() 다시 실행
     ↓
반복
```

따라서 `after()`는 게임에서 일종의 **주기적인 업데이트를 만드는 역할**을 한다.

---

## 15. 함수(Function)

함수는 특정 작업을 하나로 묶어 필요할 때 실행할 수 있도록 만든 것이다.

타이핑 게임에서는 기능별로 함수를 나누었다.

```python
spawn_word()
```

→ 새로운 단어 생성

```python
update_game()
```

→ 단어 이동 및 실패 처리

```python
check_word(event)
```

→ 사용자가 입력한 단어 확인 및 성공 처리

```python
update_score_label()
```

→ 점수 화면 업데이트

기능을 함수로 나누면 프로그램의 각 부분이 어떤 역할을 하는지 이해하기 쉬워진다.

---

# 16. File I/O

게임에서 사용할 단어를 파일에서 읽어왔다.

```python
with open(word_file, "r") as f:
    word_list = [line.strip() for line in f if line.strip()]
```

파일을 직접 코드에 하나씩 입력하는 대신 `words.txt`에서 단어 목록을 가져오는 방식이다.

### `open()`

파일을 연다.

```python
open(word_file, "r")
```

`"r"`은 읽기 모드(Read)이다.

### `with`

파일을 사용한 후 자동으로 정리할 수 있도록 도와준다.

### `strip()`

문자열의 앞뒤 공백이나 줄바꿈 문자를 제거한다.

---

# 17. Exception Handling

파일을 읽는 과정에서 파일이 없을 수도 있기 때문에 예외 처리를 사용했다.

```python
try:
    ...
except IOError:
    ...
```

의미는:

```text
try
 ↓
파일을 정상적으로 읽어보기
 ↓
성공 → 계속 실행

실패
 ↓
except 실행
 ↓
대체 단어 사용
```

즉, 예상할 수 있는 오류가 발생했을 때 프로그램이 바로 종료되지 않도록 처리하는 방법이다.

---

# 18. `random`

게임에서 단어와 속도, 위치를 무작위로 정하기 위해 `random` 모듈을 사용했다.

예:

```python
random.choice(word_list)
```

→ 단어 목록에서 랜덤으로 하나 선택

```python
random.randint(1, 3)
```

→ 1~3 사이의 랜덤한 숫자 생성

게임에서 매번 같은 위치와 속도로 단어가 등장하지 않도록 하기 위해 사용했다.

---

# 19. Event Handling

Tkinter에서는 사용자의 행동을 이벤트로 받아 처리할 수 있다.

```python
entry.bind("<Return>", check_word)
```

이 코드는 Enter 키가 눌렸을 때 `check_word()` 함수를 실행하도록 연결한다.

```text
사용자가 단어 입력
       ↓
Enter 입력
       ↓
<Return> 이벤트 발생
       ↓
check_word()
       ↓
입력한 단어 확인
```

따라서 사용자의 키보드 입력에 반응하는 프로그램을 만들 수 있다.

---

# 20. 이번 프로젝트에서 배운 Python 핵심 정리

| 개념                 | 이번 프로젝트에서 사용한 목적    |
| ------------------ | ------------------- |
| List               | 여러 개의 활성 단어 관리      |
| Dictionary         | 하나의 단어와 관련된 정보 관리   |
| `append()`         | 새로운 단어 추가           |
| `remove()`         | 단어 삭제               |
| `for`              | 여러 단어를 하나씩 확인       |
| `break`            | 원하는 단어를 찾으면 반복 종료   |
| `None`             | 아직 일치하는 단어가 없음을 표현  |
| Global Variable    | 게임 전체의 점수 관리        |
| `global`           | 함수에서 전역 변수 수정       |
| Function           | 기능별로 코드 분리          |
| `canvas.move()`    | 화면의 단어 이동           |
| `after()`          | 일정 시간 후 함수 실행 및 반복  |
| File I/O           | `words.txt`에서 단어 읽기 |
| Exception Handling | 파일 읽기 오류 처리         |
| `random`           | 단어·속도·위치 랜덤화        |
| Event Handling     | Enter 키 입력 처리       |

---

# 21. 이번 프로젝트에서 이해한 프로그램 흐름

전체적인 흐름은 다음과 같다.

```text
프로그램 시작
      ↓
words.txt에서 단어 읽기
      ↓
Tkinter 화면 생성
      ↓
새로운 단어 생성
      ↓
active_words에 저장
      ↓
update_game() 실행
      ↓
단어 이동
      ↓
화면 아래로 떨어졌는지 확인
      ↓
실패 처리 / 계속 이동
      ↓
사용자가 단어 입력
      ↓
check_word()
      ↓
active_words에서 일치하는 단어 검색
      ↓
일치하면 단어 삭제 + 성공 점수 증가
      ↓
게임 계속 진행
```

---

# 22. 느낀 점 / 배운 점

이번 프로젝트를 통해 단순히 Python 문법만 사용하는 것이 아니라,

* 여러 데이터를 List로 관리하는 방법
* 하나의 데이터를 Dictionary로 구조화하는 방법
* 반복문을 이용해 데이터를 검색하는 방법
* 함수와 전역 변수를 사용하는 방법
* Tkinter를 이용한 GUI 구성
* 이벤트에 따라 함수를 실행하는 방법
* `after()`를 이용해 반복적으로 게임 상태를 업데이트하는 방법

등을 직접 코드에 적용해 볼 수 있었다.

특히 **List 안에 Dictionary를 저장하여 여러 개의 객체를 관리하는 구조**와
**함수 내부에서 전역 변수를 수정하기 위해 `global`을 사용하는 방식**을 이해하는 계기가 되었다.
