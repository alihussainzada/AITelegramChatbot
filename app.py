import telebot 
from groq import Groq
bot = telebot.TeleBot('7684583591:AAFdEs1CoPvNqgLSWfB-DN0o9RqtYZdukRo')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "umm lets start to have fun :)")

@bot.message_handler(content_types=['text'])




def handle_text_messages(message):
    client = Groq(api_key="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")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{message.text}",

             
            }
        ],
        model="llama3-8b-8192",
    )
    finalmsg =  chat_completion.choices[0].message.content
    bot.reply_to(message, f"{finalmsg}")
    
    
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.infinity_polling()
