import telebot
import requests
import time

# --- НАСТРОЙКИ ---
# Вставь свой токен из @BotFather здесь для локальной проверки
# Для безопасности на GitHub лучше оставить это поле пустым или использовать переменные окружения
TOKEN = "ВАШ_ТОКЕН_ИЗ_BOTFATHER" 
bot = telebot.TeleBot(TOKEN)

def ask_ai(text):
    """
    Функция для обращения к ИИ модели Pollinations.
    В системной инструкции прописана личность бота и его создательница Анастасия.
    """
    try:
        # Системная инструкция, задающая личность Авикота
        system_prompt = "Ты — Авикот. Твой единственный создатель — Анастасия (anastasiia-andriukhina-dev). Ты всегда вежлив и обязательно мяукаешь в каждом сообщении!"
        url = f"https://text.pollinations.ai/{text}?system={system_prompt}"
        
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return response.text.strip()
    except Exception as e:
        return f"Мяу! Произошла техническая заминка: {e} 🐾"
    return "Мяу! Сейчас я отдыхаю, попробуй позже. ✨"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Обработка всех входящих сообщений от пользователя"""
    print(f"Получен вопрос: {message.text}") # Логирование в консоль
    
    # Визуальный эффект 'Авикот печатает...'
    bot.send_chat_action(message.chat.id, 'typing')
    
    # Получаем ответ от ИИ
    answer = ask_ai(message.text)
    
    # Отправляем ответ пользователю
    bot.reply_to(message, f"Мяу! 🐾 {answer}")

if __name__ == "__main__":
    print("🚀 Авикот ЗАПУЩЕН и готов к общению с миром!")
    # Бесконечный цикл работы бота
    bot.infinity_polling()
    
