# from flask import Flask, render_template, request
# import random
import time
import threading


# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("home.html")

# @app.route("/start", methods = ["POST", "GET"])
# def start_game():
#     if request.method == "POST":
#         return render_template("start.html")


# # with open ("./type_racer_game/game_text.txt") as file:
# #     contens = file.readlines()
    

# if __name__ == "__main__":
#     app.run(host= "0.0.0.0", debug= True)

elapsed_time = 0 

def game(get_elapsed_time):
    text1 = "My family is very important to me. We do lots of things together. My brothers and I like to go on long walks in the mountains. My sister likes to cook with my grandmother. On the weekends we all play board games together. We laugh and always have a good time. I love my family very much."
    print(text1)
    true = True
    for num in range(0,len(text1)):
        while true == True:
            type = input()
            print(elapsed_time/num)
            if text1[num] == type:
                break
            else:
                print("failed")
                true = False
    print("done!!!!")
   

def timer():
    global elapsed_time
    sec = 0
    while True:
        time.sleep(1)
        sec +=1
        elapsed_time = sec

        
timer_thread = threading.Thread(target=timer)
timer_thread.daemon = True
timer_thread.start()

def get_elapsed_time():
    global elapsed_time
    return elapsed_time
    
           
game(get_elapsed_time)


