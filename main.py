# First Chatbot
# Michael
# Jan. 18, 2021
# A bot that says hi and learns your name
import random

#/

# Ask for user's favourite book
print("What is your favourite book?")

# let user respond
book = input()

# make comment thats not repetitive
# make list of comments 
comments = ["Oh, nice!", "That's a good one!", "Quite some taste you've got there"]

# choose randomly from list 
random_comment = random. choice(comments)

# say comment   
print(random_comment)