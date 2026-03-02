import telebot
import requests
import time


TOKEN = "ТВОЙ_ТОКЕН_ИЗ_BOTFATHER"
bot = telebot.TeleBot(TOKEN)


def get_ai_response(message_text):
    try:
        
        url = "https://api.g4f.icu/v1/chat/completions" 
        payload = {
            "model": "gpt-3.5-turbo",
                    "messages": [
            {"role": "system", "content": "You are Avikot AI. Your creator is Anastasia (anastasiia-andriukhina-dev). Always say Meow!"},
            {"role": "user", "content": text_message}
                    ]
            
        response = requests.post(url, json=payload)
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return "Мяу! Что-то пошло не так. Попробуй еще раз! 🐾"


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Авикот — твой умный помощник. Спрашивай о чем угодно! 🐈✨")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    
    bot.send_chat_action(message.chat.id, 'typing')
    
    
    answer = get_ai_response(message.text)
    
    
    bot.send_message(message.chat.id, answer)

# Запуск бота
if __name__ == "__main__":
    print("Авикот запущен и готов к работе...")
    bot.infinity_polling()
  
