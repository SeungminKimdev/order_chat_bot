import re
from nltk.corpus import wordnet
# Building a list of Keywords
list_words=['hello','reservation','cancel','entrance','order','information']
list_syn={}
for word in list_words:
    synonyms=[]
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            # Remove any special characters from synonym strings
            lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
            synonyms.append(lem_name)
    list_syn[word]=set(synonyms)
print (list_syn)

# Building dictionary of Intents & Keywords
keywords={}
keywords_dict={}
# Defining a new key in the keywords dictionary
keywords['greet']=[]
# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for synonym in list(list_syn['hello']):
    keywords['greet'].append('.*\\b'+synonym+'\\b.*')

keywords['reservation']=[]
# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for synonym in list(list_syn['reservation']):
    keywords['reservation'].append('.*\\b'+synonym+'\\b.*')

keywords['entrance']=[]
# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for synonym in list(list_syn['entrance']):
    keywords['entrance'].append('.*\\b'+synonym+'\\b.*')

keywords['cancel']=[]
# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for synonym in list(list_syn['cancel']):
    keywords['cancel'].append('.*\\b'+synonym+'\\b.*')

keywords['information']=[]
# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for synonym in list(list_syn['information']):
    keywords['information'].append('.*\\b'+synonym+'\\b.*')

keywords['order']=[]
# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for synonym in list(list_syn['order']):
    keywords['order'].append('.*\\b'+synonym+'\\b.*')
    
for intent, keys in keywords.items():
    # Joining the values in the keywords dictionary with the OR (|) operator updating them in keywords_dict dictionary
    keywords_dict[intent]=re.compile('|'.join(keys))
print (keywords_dict)


# Building a dictionary of responses
responses={
    'greet':'Hello! How can I help you?',
    'reservation':'Thank you for visiting',
    'cancel':'Help you cancel your reservation.',
    'entrance':'Please come in',
    'order':'Current waiting situation',
    'information':'This is the store information',
    'fallback':'I dont quite understand. Could you repeat that?',
}

import linked_list
customers = linked_list.LinkedList()

global keyNumber, isReserve, cusName, cusNumber
keyNumber = 0
isReserve = 0
cusName = ""
cusNumber = ""

from tkinter import *

# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


# Send function
def send(event):
    global keyNumber, isReserve, cusName, cusNumber
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)

    user_input = e.get().lower()
    #quit입력시 종료
    if user_input == 'quit':
        root.forget(root)
    key = 'temp'
    if isReserve == 0: #예약자 정보가 필요 없는 경우
        matched_intent = None
        for intent,pattern in keywords_dict.items():
            if re.search(pattern, user_input): 
                matched_intent=intent  
        key='fallback' 
        if matched_intent in responses:
            key = matched_intent

    #상황별 질문 관리 responses[key] = 키워드
    if keyNumber == 0: #기본 질문 상황
        if key == "greet": #인사
            txt.insert(END, "\n" + "Bot -> " + responses[key])
        elif key == "reservation": #예약
            txt.insert(END, "\n" + "Bot -> " + responses[key])
            keyNumber = 1
            isReserve = 1
            txt.insert(END, "\n" + "Bot -> 성함을 입력해주세요")
        elif key == "cancel": #취소
            txt.insert(END, "\n" + "Bot -> " + responses[key])
            keyNumber = 3
            isReserve = 1
            txt.insert(END, "\n" + "Bot -> 성함을 입력해주세요")
        elif key == "order": #순서
            txt.insert(END, "\n" + "Bot -> " + responses[key])
            keyNumber = 5
            isReserve = 1
            txt.insert(END, "\n" + "Bot -> 성함을 입력해주세요")
        elif key == "entrance": #입장
            txt.insert(END, "\n" + "Bot -> " + responses[key])
            txt.insert(END, "\n" + "입장자 정보 : " + customers.entry())
        elif key == "information": #가계 정보
            txt.insert(END, "\n" + "Bot -> " + responses[key])
        else:
            txt.insert(END, "\n" + "다시 한번 입력해주세요")
    elif keyNumber == 1: #예약 신청(이름)
        txt.insert(END, "\n" + "이름 : " + user_input)
        cusName = user_input
        keyNumber = 2
        isReserve = 1
        txt.insert(END, "\n" + "전화번호를 입력해주세요")
    elif keyNumber == 2: #예약 신청(전화번호)
        txt.insert(END, "\n" + "전화번호 : " + user_input)
        cusNumber = user_input
        customers.add(linked_list.Node(cusName,cusNumber))
        txt.insert(END, "\n" + "예약이 완료되었습니다.")
        keyNumber = 0
        isReserve = 0
    elif keyNumber == 3: #예약 취소(이름)
        txt.insert(END, "\n" + "이름 : " + user_input)
        cusName = user_input
        keyNumber = 4
        isReserve = 1
        txt.insert(END, "\n" + "전화번호를 입력해주세요")
    elif keyNumber == 4: #예약 취소(전화번호)
        txt.insert(END, "\n" + "전화번호 : " + user_input)
        cusNumber = user_input
        customers.delete(cusName, cusNumber)
        txt.insert(END, "\n" + "취소가 완료되었습니다.")
        keyNumber = 0
        isReserve = 0
    elif keyNumber == 5: #순서 찾기(이름)
        txt.insert(END, "\n" + "이름 : " + user_input)
        cusName = user_input
        keyNumber = 6
        isReserve = 1
        txt.insert(END, "\n" + "전화번호를 입력해주세요")
    elif keyNumber == 6: #순서 찾기(전화번호)
        txt.insert(END, "\n" + "전화번호 : " + user_input)
        cusNumber = user_input
        cusCount = str(customers.get_count(cusName, cusNumber))
        if cusCount == -1:
            txt.insert(END, "\n" + "해당 고객님의 정보가 존재하지 않습니다.")
        else:
            txt.insert(END, "\n" + "고객님의 현재 대기번호는 : " + cusCount)
        keyNumber = 0
        isReserve = 0
    
    e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

root.bind('<Return>', send)
root.mainloop()
