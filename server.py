

import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 1234

server.bind((ip_address, port))
server.listen()

clients = []
nicknames = []

questions = [
    "Who was the original drummer for the beatles? \n a. Ringo Star \n b. Pete Best \n c. John Lennon \n d. George Harrison",
    "Who from the following was in one direction? \n a. Luke Hemmings \n b. Ed sheeran \n c. Louis Tomlinson \n d. Bradley Simpson",
    "How many memebers are there in BTS? \n a. 9 \n b. 4 \n c. 5 \n d. 7",
    "What is the best selling single of all time? \n a. White Christmas by Bing Crosby \n b. Shape of you by Ed Sheeran \n c. Something Just like this by The chainsmokers & Coldplay \n d. Perfect by Ed Sheeran ",
    "Who is the best selling female artist of all time? \n a. Adele \n b. Madonna \n c. Taylor Swift \n d. Katy Perry",
    "Who is the oldest female artist to reach no. 1 with the longest gap between hits? \n a. Kate bush \n b. Miley Cyrus \n c. Katy Perry \n d. Madonna",
    "Which song stayed 1 on Billboard for 15 weeks? \n a. Old Town Road by Lil Nas X \n b. All I want for christmas is you by Mariah Carey \n c. As it was by Harry Styles \n d. Macarena by Los Del Rio",
    "Who is the youngest person to win 'triple crown' film music award? \n a. Louis Tomlinson \n b. Billie Eillish \n c. Conan Gray \n d. Olivia Rodrigo",
    "Who is the first group to debut at no. 1 with their first 4 albums in the US? \n a. BTS \n b. The Beatles \n c. One Direction \n d. Backstreet Boys",
    "Which singer has most Guiness World Records? \n a. Asha Bhosle \n b. Taylor Swift \n c. Madonna \n d. Lata Mangeshkar",
    "Who is top listened artist? \n a. Just Bieber \n b. Drake \n c. BTS \n d. Taylor Swift"
]

answers = ['b', 'c', 'd', 'a', 'b', 'a', 'c', 'b', 'c', 'a', 'd']

print("Server has started...")

def get_random_question_answer(conn):
    random_index = random.randint(0,len(questions) - 1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index, random_question, random_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)

def clientthread(conn, nickname):
    score = 0
    conn.send("Welcome to this quiz game!".encode('utf-8'))
    conn.send("You will receive a question. The answer to that question should be one of a, b, c or d!\n".encode('utf-8'))
    conn.send("Good Luck!\n\n".encode('utf-8'))
    index, question, answer = get_random_question_answer(conn)
    print(answer)
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                if len(questions)!=0:
                    if message.split(": ")[-1].lower() == answer:
                        score += 1
                        conn.send(f"Bravo! Your score is {score}\n\n".encode('utf-8'))
                    else:
                        conn.send("Incorrect answer! Better luck next time!\n\n".encode('utf-8'))
                else:
                    break
                            
                remove_question(index)
                index, question, answer = get_random_question_answer(conn)
                print(answer)
            else:
                remove(conn)
                remove_nickname(nickname)
        except Exception as e:
            print(str(e))
            continue

def remove(connection):
    if connection in clients:
        clients.remove(connection)

def remove_nickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)

while True:
    conn, addr = server.accept()
    conn.send('NICKNAME'.encode('utf-8'))
    nickname = conn.recv(2048).decode('utf-8')
    clients.append(conn)
    nicknames.append(nickname)
    print (nickname + " connected!")
    new_thread = Thread(target= clientthread,args=(conn,nickname))
    new_thread.start()