import re
import random
import pywhatkit

response_list = {
    r"youtube":["Ok, what do you want to watch on youtube?"],
    r"i (?:want to|wanna) (.*)": ["Why do you want to {}?"],
    r"chat":["Ok, who do you want to chat with?"],
    r"(?:hi|hello)": ["Hello, how may I help you."],
    r"(?:.*)i feel (.*)": ["Why do you feel {}?", "How long have you been feeling {}?"],
    r"\bi\s*\'?\s*a?m\b (.*)": ["Why are you {}?", "How long have you been {}?"],
    r"(?:.*)i need (.*)": ["Why do you need {}?", "How can I help you with that?"],
    r"i (.*) you": ["Why do you {} me?", "What makes you think you {} me?"],
    r"(?:.*)i (.*) myself": ["Why do you {} yourself?", "What makes you think you {} yourself?"],
    r"(.*)sorry": ["There's no need to apologize"],
    r"yes": ["Ok, but can you tell me more?", "Ok, but why do you say that?"],
    r"no": ["Why not?", "Are you sure?"],
    r"(?:thank you|thanks|thx)": ["You're welcome", "No problem", "I'm always here to help"],
    r" (.*)": ["Please tell me more.", "Ok, but let's talk about your day, how's your day going"],
    r"": ["Please tell me more.", "Ok, but let's talk about your day, how's your day going"]
}

negative_expressions = [
    "bored",
    "awful",
    "terrible",
    "not good",
    "can't stand",
    "worst",
    "disappointed",
    "letdown",
    "not impressed",
    "frustrated",
    "fed up",
    "disaster",
    "not happy",
    "nightmare",
    "mess",
    "not enjoying",
    "annoying",
    "not having a good time",
    "total failure",
    "die"
]

negative_pattern = re.compile(r"\b(" + "|".join(re.escape(exp) for exp in negative_expressions) + r")\b", re.IGNORECASE)

def match_response(input):
    for pattern, responses in response_list.items():
        match = re.match(pattern, input.lower())
        if match:
            response = random.choice(responses)
            return response.format(*match.groups())
        
    return "I'm sorry, I don't understand what you're saying."

contact_list = {
    "daniyal": "+6281226749611",
    "haikal": "+62895367597379",
}

def send_message(contact, message):
    if contact in contact_list:
        phone_no = contact_list[contact]
    else:
        phone_no = contact
    pywhatkit.sendwhatmsg_instantly(
        phone_no=phone_no,
        message=message,
        tab_close=True,
        close_time=10
        )
    
def handle_chat(name):
    print(f"Renee: Ok, who do you want to chat with?")
    contact = input("{}: ".format(name))
    print(f"Renee: What message do you want to send to {contact}?")
    message = input("{}: ".format(name))
    print(f"Renee: Here, I'll help you contact them. Opening WhatsApp...")
    send_message(contact.lower(), message)

def play_youtube(query):
    pywhatkit.playonyt(query)

def handle_youtube(name):
    print(f"Renee: Ok, what do you want to watch on YouTube?")
    query = input("{}: ".format(name))
    print(f"Renee: Yay, let's watch {query} on YouTube. Opening YouTube...")
    play_youtube(query)


def serene_chatbot():
    print("Renee: Welcome to Serene your personal companion. You can call me Renee. What's your name?")
    name=input(">>> ")
    print(f"Renee: Hi {name}, what brings you here today?")
    while True:
        input_text = input("{}: ".format(name))
        if input_text.lower() == "bye":
            print("Renee: Bye, have a nice day and don't forget to take a rest.")
            break
        elif negative_pattern.search(input_text):
            print("Renee: I'm sorry to hear that. Do you want to do something fun to cheer you up?")
            input_text = input("{}: ".format(name)).lower()
            if input_text.lower() == "bye":
                print("Renee: Bye, have a nice day and don't forget to take a rest.")
                break
            elif input_text.lower() == "no":
                print("Renee: alright, maybe we can do chitchat. What do you want to talk about?")
            elif input_text.lower() == "yes":
                print("Renee: Ok, what do you want to do. Maybe chat with your friend or watch some youtube?")
                input_text = input("{}: ".format(name)).lower()
                if re.search(r"youtube", input_text, re.IGNORECASE):
                    handle_youtube(name)
                elif re.search(r"chat", input_text, re.IGNORECASE):
                    handle_chat(name)
                else:
                    print(f"Renee: {match_response(input_text)}")
        elif re.search(r"youtube", input_text, re.IGNORECASE) :
            handle_youtube(name)
        elif re.search(r"chat", input_text, re.IGNORECASE):
            handle_chat(name)
        else:
            print(f"Renee: {match_response(input_text)}")


if __name__ == "__main__":
    serene_chatbot()
