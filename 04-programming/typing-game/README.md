# Python Typing Game

Python과 Tkinter를 활용하여 제작한 GUI 타자 게임입니다.

Python의 기본 문법과 GUI 프로그래밍을 학습하고, 파일 입출력, 예외 처리, 리스트, 딕셔너리, 함수, 이벤트 처리 및 반복 실행 등의 개념을 실제 프로그램에 적용했습니다.

## 1. Project Overview

화면 위에서 아래로 떨어지는 단어를 사용자가 입력하여 맞추는 타자 게임입니다.

단어가 일정한 간격으로 생성되며, 사용자가 단어를 입력하고 엔터 키를 누르면 정답 여부를 확인합니다.

단어가 화면 아래쪽에 도달하면 놓친 단어로 처리하고 점수를 갱신합니다.

## 2. Development Environment

* Language: Python
* GUI Library: Tkinter
* Operating System: macOS
* Project Type: School Assignment
* Difficulty: Beginner

## 3. Main Features

### 3.1 Word File Loading

`words.txt` 파일에서 단어를 읽어 리스트에 저장합니다.

파일을 찾을 수 없거나 읽기 오류가 발생하면 기본 단어 목록을 사용합니다.

### 3.2 Falling Words

랜덤으로 선택한 단어를 캔버스에 생성하고, 일정한 속도로 아래쪽으로 이동시킵니다.

### 3.3 Word Matching

사용자가 입력한 단어와 화면에 표시된 단어를 비교합니다.

일치하는 단어가 있으면 해당 단어를 제거하고 정답 점수를 증가시킵니다.

### 3.4 Score System

* 맞춘 단어 수
* 놓친 단어 수

두 가지 점수를 화면에 표시합니다.

## 4. Python Concepts

### 4.1 Module Import

```python
import os
import random

from tkinter import *
```

파이썬에서 모듈을 불러와 다른 기능을 사용할 수 있습니다.

* `os`: 파일 경로 처리
* `random`: 랜덤한 단어와 숫자 선택
* `tkinter`: GUI 프로그램 제작

`import`는 외부 또는 내장 모듈의 기능을 현재 프로그램에서 사용할 수 있도록 불러오는 역할을 합니다.

### 4.2 Variables and Lists

```python
word_list = []
active_words = []

score_success = 0
score_fail = 0
```

변수는 데이터를 저장하는 공간입니다.

* `word_list`: 전체 단어 목록
* `active_words`: 현재 화면에 표시되는 단어 객체 목록
* `score_success`: 맞춘 단어 수
* `score_fail`: 놓친 단어 수

리스트는 여러 개의 데이터를 하나의 자료구조로 관리할 때 사용합니다.

### 4.3 File Path and File I/O

```python
file_path = os.path.expanduser("~/Downloads/words.txt")
```

`os.path.expanduser()`를 사용하여 사용자의 홈 디렉터리를 기준으로 파일 경로를 구성합니다.

```python
infile = open(file_path, "r", encoding="utf-8")

for line in infile:
    word = line.rstrip()
    word_list.append(word)

infile.close()
```

파일을 읽기 모드(`"r"`)로 열고, 각 줄을 읽어 단어 목록에 저장합니다.

* `open()`: 파일 열기
* `for`: 파일의 각 줄을 반복 처리
* `rstrip()`: 문자열 오른쪽의 공백 및 줄바꿈 제거
* `append()`: 리스트에 데이터 추가
* `close()`: 파일 닫기

### 4.4 Exception Handling

```python
try:
    infile = open(file_path, "r", encoding="utf-8")
    
except IOError:
    print("다운로드 폴더에서 words.txt를 찾지 못해 기본 단어를 불러옵니다.")
    word_list = ["python", "apple", "code", "keyboard", "macbook"]
```

`try-except`는 프로그램에서 특정 오류가 발생했을 때 처리할 수 있도록 합니다.

파일이 존재하지 않거나 읽기 과정에서 오류가 발생하는 경우 기본 단어 목록을 사용하도록 구성했습니다.

예외 처리를 통해 파일 오류가 발생하더라도 기본 단어를 활용하여 프로그램을 실행할 수 있습니다.

### 4.5 Functions

```python
def spawn_word():
    ...
```

함수는 특정 작업을 하나의 코드 블록으로 정의하여 필요할 때 호출할 수 있도록 합니다.

프로그램에서는 다음과 같은 함수를 사용합니다.

| 함수                     | 역할               |
| ---------------------- | ---------------- |
| `spawn_word()`         | 새로운 단어 생성        |
| `update_game()`        | 단어 이동 및 바닥 도달 확인 |
| `check_word()`         | 사용자 입력과 단어 비교    |
| `update_score_label()` | 점수 화면 갱신         |

함수를 사용하면 기능별로 코드를 나누어 관리할 수 있습니다.

### 4.6 Random Module

```python
word = random.choice(word_list)
speed = random.randint(1, 3)
x = random.randint(50, 550)
```

`random` 모듈을 사용하여 단어, 이동 속도, 생성 위치를 랜덤으로 결정합니다.

* `random.choice()`: 리스트에서 임의의 요소 선택
* `random.randint()`: 지정한 범위의 정수 중 하나 선택

이를 통해 단어가 매번 동일한 위치와 속도로 생성되지 않도록 구현했습니다.

### 4.7 Dictionary

```python
fw = {
    "id": text_id,
    "word": word,
    "speed": speed,
    "y": y
}
```

딕셔너리는 키와 값의 쌍으로 데이터를 저장하는 자료구조입니다.

하나의 단어에 필요한 여러 정보를 딕셔너리로 관리합니다.

| Key     | Value     | 설명              |
| ------- | --------- | --------------- |
| `id`    | `text_id` | 캔버스에 생성된 텍스트 ID |
| `word`  | `word`    | 단어 문자열          |
| `speed` | `speed`   | 이동 속도           |
| `y`     | `y`       | 단어의 세로 위치       |

```python
active_words.append(fw)
```

생성된 단어 정보를 `active_words` 리스트에 추가합니다.

### 4.8 Tkinter GUI

```python
root = Tk()

root.title("GUI 타자 프로그램")
root.geometry("600x500")
```

Tkinter를 사용하여 GUI 프로그램의 기본 창을 생성합니다.

* `Tk()`: 메인 윈도우 생성
* `title()`: 창 제목 설정
* `geometry()`: 창 크기 설정

```python
canvas = Canvas(root, width=600, height=400, bg="white")
canvas.pack()
```

`Canvas`는 텍스트, 도형 등의 요소를 화면에 표시할 수 있는 위젯입니다.

게임에서는 떨어지는 단어를 표시하는 영역으로 사용합니다.

### 4.9 Event Handling

```python
entry.bind("<Return>", check_word)
```

사용자가 입력창에서 엔터 키를 누르면 `check_word()` 함수가 실행되도록 연결합니다.

`bind()`는 특정 이벤트가 발생했을 때 함수를 실행하도록 설정하는 데 사용합니다.

### 4.10 Repeated Execution with after()

```python
root.after(3000, spawn_word)
root.after(50, update_game)
```

Tkinter의 `after()` 메서드를 사용하여 일정 시간이 지난 후 함수를 실행하도록 설정합니다.

* `3000`: 3000밀리초(3초) 후 단어 생성 함수 호출
* `50`: 50밀리초 후 게임 업데이트 함수 호출

함수 내부에서 다시 `after()`를 호출하여 반복적으로 실행되도록 구성했습니다.

## 5. Game Logic

### 5.1 Word Generation

1. 단어 목록에서 랜덤으로 단어 선택
2. 이동 속도와 생성 위치 결정
3. 캔버스에 텍스트 생성
4. 단어 정보를 딕셔너리에 저장
5. 활성 단어 리스트에 추가
6. 3초 후 새로운 단어 생성 예약

### 5.2 Word Movement

1. 활성 단어 리스트를 순회
2. `canvas.move()`로 단어 이동
3. 단어의 세로 위치 갱신
4. 단어가 바닥에 도달했는지 확인
5. 바닥에 도달하면 단어 삭제 및 놓친 단어 점수 증가

### 5.3 Word Matching

1. 입력창에서 사용자 입력 가져오기
2. 입력창 초기화
3. 활성 단어 리스트에서 일치하는 단어 검색
4. 일치하는 단어가 있으면 캔버스에서 삭제
5. 활성 단어 리스트에서 해당 객체 제거
6. 정답 점수 증가

## 6. What I Learned

이번 프로젝트를 통해 다음과 같은 개념을 학습했습니다.

* Python의 변수와 리스트 사용
* 파일 입출력 및 예외 처리
* 함수 정의와 호출
* 딕셔너리를 활용한 데이터 관리
* Tkinter GUI 구성
* 이벤트 처리
* `after()`를 활용한 반복 작업 구현

특히 단순한 문법 연습을 넘어 여러 파이썬 개념을 하나의 GUI 프로그램에 적용하는 과정을 경험했습니다.

## 7. Limitations and Future Improvements

현재 프로젝트의 개선 사항입니다.

* 단어가 화면의 경계를 벗어나지 않도록 위치 조정
* 게임 시작 및 종료 기능 추가
* 난이도 조절 기능 추가
* 중복 단어 처리 방식 개선
* 게임 상태를 클래스로 관리하는 구조 학습
* 코드 구조와 예외 처리 개선

## 8. Project Status

* [x] 기본 타자 게임 구현
* [x] 단어 파일 불러오기
* [x] 단어 이동 기능
* [x] 정답 및 놓친 단어 점수 표시
* [x] GUI 구성

현재 프로젝트는 Python 및 Tkinter 기초 학습을 목적으로 제작한 학교 과제입니다.
