# # 1: simple chatboat 
# import random
# Chat = ["hi","hello","how are you","i am good", "hey,What's up","Take care"]
# print("Random Chat" )
# for i in range (1):
#   input = input("hey i am chat_board Enter something...! ")
# print(random.choice(Chat))

# # 2: Simple chatbot using random responses
# import random
# # Define a list of chat responses
# chat_responses = [
#     "hi",
#     "hello",
#     "how are you",
#     "i am good",
#     "hey, what's up",
#     "take care"
# ]
# # Print a header for the random chat
# print("Random Chat")
# # Simulate a user input prompt
# user_input = input("Hey, I am chat_board. Enter something...! ")
# # Print a random chat response
# print(random.choice(chat_responses))

# # 3: Simple chatbot using if and else

# print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to end the conversation.")
# while True:
#     user = input("You: ")
#     if user == "hi" or user == "hello":
#         print("Chatbot: Hello! How can I help you?")
#     elif user == "how are you":
#         print("Chatbot: I'm just a program, but I'm doing fine. Thanks!")
#     elif user == "what is your name":
#         print("Chatbot: I'm called SimpleBot.")
#     elif user == "bye":
#         print("Chatbot: Goodbye! Have a great day!")
#         break
#     else:
#         print("Chatbot: I'm not sure how to respond to that.")

#  Again simple chatboat
# import random

# words = ["hello", "malika", "dua"]
# print("Welcome! Let's play a guessing game.")

# while True:
#     n = input("What's on your mind? (type 'exit' to quit): ").lower()
#     if n == "exit":
#         print("Goodbye!")
#         break

#     random_choice = random.choice(words)
#     if n == random_choice:
#         print("Wow! You guessed it!")
#     else:
#         print(f"Nope, I was thinking of '{random_choice}'. Try again!")

# 4: Simple chatbot with a guessing game

# import random
# print("Welcome to the Simple Chatbot Guessing Game!")
# words = ["hello", "malika", "dua"]
# while True:
#     user_input = input("What's on your mind? (type 'exit' to quit): ").lower()
#     if user_input == "exit":
#         print("Goodbye!")
#         break
#     random_choice = random.choice(words)
#     if user_input == random_choice:
#         print("Wow! You guessed it!")
#     else:
#         print(f"Nope, I was thinking of '{random_choice}'. Try again!")



import random 
chat = [ " hello", " hi", " how are you", " i am good", " hey, what's up", " take care"]
# print (" random chat")
while True:
    input = input("hey I am chatboat say anything you want or type 'exist' to exit: ")
    if input == "exist":
        print (" fine bye")
        break
choice = random.choice(chat)
if input == choice:
    print("Wow! You guessed it!")
else:
    print(f"Nope, I was thinking of '{choice}'. Try again!")
  
# print(random.choice(chat))

