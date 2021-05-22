import telebot
TOKEN = 'Вставьте сюда свой токен'
bot = telebot.TeleBot(TOKEN)
keyboard = telebot.types.ReplyKeyboardMarkup()
button_phone = telebot.types.KeyboardButton('Подтвердить номер', request_contact=True)
button_location = telebot.types.KeyboardButton('Подтвердить местоположение', request_location=True)
keyboard.add(button_phone, button_location)
@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать! Чтобы воспользоваться ботом, подтвердите ваш номер телефона и местоположение.', reply_markup = keyboard)
    @bot.message_handler(content_types=['contact'])
    def contact_handler(message):
        print('Номер телефона: +', message.contact.phone_number)
    @bot.message_handler(content_types=['location'])
    def handle_location(message):
        print('Геолокация: ', message.location.latitude, message.location.longitude)
print('Бот запущен!')
bot.polling()
