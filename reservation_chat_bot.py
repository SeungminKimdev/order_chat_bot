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
import tkinter as tk

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
    #quit????????? ??????
    if user_input == 'quit':
        root.forget(root)
    key = 'temp'
    if isReserve == 0: #????????? ????????? ?????? ?????? ??????
        matched_intent = None
        for intent,pattern in keywords_dict.items():
            if re.search(pattern, user_input): 
                matched_intent=intent  
        key='fallback' 
        if matched_intent in responses:
            key = matched_intent

    #????????? ?????? ?????? responses[key] = ?????????
    if keyNumber == 0: #?????? ?????? ??????
        if key == "greet": #??????
            txt.insert(END, "\n" + "Bot -> " + responses[key])
        elif key == "reservation": #??????
            txt.insert(END, "\n" + "Bot -> " + responses[key])
            txt.see(END)
            keyNumber = 1
            isReserve = 1
            txt.insert(END, "\n" + "Bot -> ????????? ??????????????????")
        elif key == "cancel": #??????
            txt.insert(END, "\n" + "Bot -> " + responses[key])
            txt.see(END)
            keyNumber = 3
            isReserve = 1
            txt.insert(END, "\n" + "Bot -> ????????? ??????????????????")
        elif key == "order": #??????
            txt.insert(END, "\n" + "Bot -> " + responses[key])
            txt.see(END)
            keyNumber = 5
            isReserve = 1
            txt.insert(END, "\n" + "Bot -> ????????? ??????????????????")
        elif key == "entrance": #??????
            tempName = customers.entry()
            if tempName == "-1":
                txt.insert(END, "\n" + "?????? ????????? ????????????.")
                txt.see(END)
            else:
                txt.insert(END, "\n" + "Bot -> " + responses[key])
                txt.see(END)
                txt.insert(END, "\n" + "????????? ?????? : " + tempName)
                enterance.delete("1.0",END)
                enterance.insert(END,tempName,'center')
        elif key == "information": #?????? ??????
            txt.insert(END, "\n" + "Bot -> " + responses[key])
        else:
            txt.insert(END, "\n" + "?????? ?????? ??????????????????")
        txt.see(END)
    elif keyNumber == 1: #?????? ??????(??????)
        txt.insert(END, "\n" + "?????? : " + user_input)
        txt.see(END)
        cusName = user_input
        keyNumber = 2
        isReserve = 1
        txt.insert(END, "\n" + "??????????????? ??????????????????")
        txt.see(END)
    elif keyNumber == 2: #?????? ??????(????????????)
        txt.insert(END, "\n" + "???????????? : " + user_input)
        txt.see(END)
        cusNumber = user_input
        customers.add(linked_list.Node(cusName,cusNumber))
        txt.insert(END, "\n" + "????????? ?????????????????????.")
        txt.see(END)
        keyNumber = 0
        isReserve = 0
    elif keyNumber == 3: #?????? ??????(??????)
        txt.insert(END, "\n" + "?????? : " + user_input)
        txt.see(END)
        cusName = user_input
        keyNumber = 4
        isReserve = 1
        txt.insert(END, "\n" + "??????????????? ??????????????????")
        txt.see(END)
    elif keyNumber == 4: #?????? ??????(????????????)
        txt.insert(END, "\n" + "???????????? : " + user_input)
        txt.see(END)
        cusNumber = user_input
        customers.delete(cusName, cusNumber)
        txt.insert(END, "\n" + "????????? ?????????????????????.")
        txt.see(END)
        keyNumber = 0
        isReserve = 0
    elif keyNumber == 5: #?????? ??????(??????)
        txt.insert(END, "\n" + "?????? : " + user_input)
        txt.see(END)
        cusName = user_input
        keyNumber = 6
        isReserve = 1
        txt.insert(END, "\n" + "??????????????? ??????????????????")
        txt.see(END)
    elif keyNumber == 6: #?????? ??????(????????????)
        txt.insert(END, "\n" + "???????????? : " + user_input)
        txt.see(END)
        cusNumber = user_input
        cusCount = str(customers.get_count(cusName, cusNumber))
        if cusCount == '-1':
            txt.insert(END, "\n" + "?????? ???????????? ????????? ???????????? ????????????.")
        else:
            txt.insert(END, "\n" + "???????????? ?????? ??????????????? : " + cusCount)
        txt.see(END)
        keyNumber = 0
        isReserve = 0
    
    e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Entrance", font=FONT_BOLD, pady=10 , width=10, height=1).grid(
    row=0,column=0)
enterance = Text(root,bg="#FFFFFF",fg="#000000", font=FONT_BOLD, pady= 10, width=50, height=1)
enterance.grid(row=0,column=1)
enterance.tag_configure("center", justify='center')

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row = 1, column = 0, columnspan = 2, sticky=tk.W+tk.E+tk.N+tk.S)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row = 2, column = 0, columnspan = 2, sticky=tk.W+tk.E+tk.N+tk.S)

root.bind('<Return>', send)
root.mainloop()