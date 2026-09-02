import os
import json
from telebot import TeleBot, types

# የቦትህን Token እዚህ ጋር አስገባ
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    
    # የMini App አድራሻህ
    web_app = types.WebAppInfo(url="https://0945508024.github.io/-app/")
    button = types.KeyboardButton(text="ኩሉ ብሓደ (አዲስ ማስታወቂያ)", web_app=web_app)
    markup.add(button)
    
    bot.send_message(
        message.chat.id, 
        "ሰላም! አዲስ ማስታወቂያ ለማስገባት ከታች ያለውን 'ኩሉ ብሓደ' የሚለውን በተን ይጫኑ።", 
        reply_markup=markup
    )

# ከMini App የሚመጣውን መረጃ መቀበያ
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    try:
        # የገባውን JSON መረጃ መፍታት
        data = json.loads(message.web_app_data.data)
        
        category = data.get('category', 'ያልተጠቀሰ')
        title = data.get('title', 'ያልተጠቀሰ')
        price = data.get('price', 'ያልተጠቀሰ')
        description = data.get('description', 'የለም')

        # ለተጠቃሚው የሚላክ የተስተካከለ መልዕክት
        response_text = (
            f"📌 **አዲስ ማስታወቂያ ደርሷል!**\n\n"
            f"📂 **ዘርፍ:** {category}\n"
            f"📝 **ርዕስ:** {title}\n"
            f"💵 **ዋጋ:** {price} ETB\n"
            f"ℹ️ **መግለጫ:** {description}\n\n"
            f"👤 **ለካፊ:** @{message.from_user.username if message.from_user.username else message.from_user.first_name}"
        )

        bot.send_message(message.chat.id, response_text, parse_mode="Markdown")

    except Exception as e:
        bot.send_message(message.chat.id, "መረጃውን በማስተናገድ ላይ ስህተት ተፈጥሯል።")

if __name__ == '__main__':
    bot.infinity_polling()
