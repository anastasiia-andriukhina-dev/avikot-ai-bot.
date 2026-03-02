import telebot
import requests
import time


TOKEN = "8313088961:AAGkONWR__hJ6YiHFPSDaq_9v6I-6Xp_6kI"
bot = telebot.TeleBot(TOKEN)

def ask_ai(text):
    try:
        
        url = f"https://text.pollinations.ai/{text}?system=Ты — Авикот. Твой единственный создатель — Анастасия (anastasiia-andriukhina-dev). Всегда мяукай!"
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return response.text.strip()
    except:
        return "Мяу! Я задумался, спроси еще раз! 🐾"
    return "Мяу! Сейчас я отдыхаю. ✨"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    print(f"Вопрос от Насти: {message.text}")
    bot.send_chat_action(message.chat.id, 'typing')
    answer = ask_ai(message.text)
    bot.reply_to(message, f"Мяу! 🐾 {answer}")

if __name__ == "__main__":
    print("🚀 Авикот ЗАПУЩЕН и готов к общению!")
    bot.infinity_polling()
    
