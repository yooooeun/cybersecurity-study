import os
import random

from tkinter import *


# ==========================================

# 1. 전역 변수 선언 (게임 상태 관리)

# ==========================================

word_list = []

# Mac 다운로드 폴더 안 words.txt 경로
file_path = os.path.expanduser("~/Downloads/words.txt")


try:
    infile = open(file_path, "r", encoding="utf-8")
    
    for line in infile:
        word = line.rstrip()
        word_list.append(word)
        
    infile.close()
    
# 파일이 없거나 읽기 오류가 날 때 처리할 except 추가
except IOError:
    print("다운로드 폴더에서 words.txt를 찾지 못해 기본 단어를 불러옵니다.")
    word_list = ["python", "apple", "code", "keyboard", "macbook"]

active_words = []  # 현재 화면에 떨어지고 있는 단어 객체들
score_success = 0
score_fail = 0


# ==========================================

# 2. 게임 로직 함수 정의

# ==========================================

def spawn_word():

    """3초마다 새로운 단어를 생성하는 함수"""

    if len(word_list) > 0:

        word = random.choice(word_list)

        speed = random.randint(1, 3)

        x = random.randint(50, 550)

        y = 0

        

        # 캔버스에 텍스트 생성 후 딕셔너리로 정보 저장

        text_id = canvas.create_text(x, y, text=word, font=("Arial", 16, "bold"), fill="black")

        fw = {

            "id": text_id,

            "word": word,

            "speed": speed,

            "y": y

        }

        active_words.append(fw)

    

    # 3초 뒤에 spawn_word 재호출

    root.after(3000, spawn_word)



def update_game():

    """단어들을 이동시키고 바닥에 닿았는지 체크하는 루프 함수"""

    global score_fail

    

    for fw in active_words[:]:

        # 단어 이동

        canvas.move(fw["id"], 0, fw["speed"])

        fw["y"] += fw["speed"]

        

        # 바닥(높이 400)에 도달했을 때 처리

        if fw["y"] > 400:

            canvas.delete(fw["id"])

            active_words.remove(fw)

            score_fail += 1

            update_score_label()



    # 50ms마다 update_game 재호출 (애니메이션 효과)

    root.after(50, update_game)



def check_word(event):

    """사용자가 엔터를 쳤을 때 정답 여부를 확인하는 함수"""

    global score_success

    

    user_input = entry.get().strip()

    entry.delete(0, END)



    matched = None

    for fw in active_words:

        if fw["word"] == user_input:

            matched = fw

            break



    if matched:

        canvas.delete(matched["id"])

        active_words.remove(matched)

        score_success += 1

        update_score_label()



def update_score_label():

    """점수를 화면에 갱신하는 함수"""

    label_score.config(text=f"맞춘 단어: {score_success} | 틀린 단어: {score_fail}")



# ==========================================

# 3. GUI 화면 구성 및 실행

# ==========================================

root = Tk()

root.title("GUI 타자 프로그램")

root.geometry("600x500")



# 캔버스 및 하단 프레임 생성

canvas = Canvas(root, width=600, height=400, bg="white")

canvas.pack()



frame = Frame(root)

frame.pack(fill=BOTH, expand=True, padx=10, pady=10)



label_score = Label(frame, text="맞춘 단어: 0 | 틀린 단어: 0", font=("Arial", 12))

label_score.pack(side=TOP, anchor=W)



entry = Entry(frame, font=("Arial", 14))

entry.pack(fill=X, pady=5)

entry.bind("<Return>", check_word)

entry.focus()



# 게임 시작

spawn_word()

update_game()



root.mainloop()

