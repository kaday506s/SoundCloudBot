# Misha Kaday
# Telegram bot
import telebot
from telebot import types
import getmusicsound
import emojis
import parse_music_text
import threading


# create bot
bot = telebot.TeleBot("TOKEN")


# create btn Author
def create_btn():
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Author', url='https://web.telegram.org/#/im?p=@MyNin')
    markup.add(btn_my_site)
    return markup


# create btn list music
def create_btn_data(data):
    markup = types.InlineKeyboardMarkup()
    for i in data:
        markup.add(types.InlineKeyboardButton(text=str(i['name']), callback_data=str(i['url'])))
    return markup


# create list music
def create_text_data(data):
    text = ""
    for i in data:
        text += str(i['id'])+' : '+i['name']+"\n"
    return text


# send audio file
def send_audio(chat_id, url):
    # send wait
    wait_m = bot.send_message(chat_id,
                              emojis.encode(':stopwatch:') +
                              ' Wait please . . . ')
    # get song
    media_file = getmusicsound.down_load(str(url))
    # delete message
    bot.delete_message(chat_id, wait_m.message_id)
    # send song
    bot.send_audio(chat_id, media_file, title=str(url).split('/')[-1])
    return None


#  function to find sound
def data_finder(text, chat_id):
    # find list music from SC
    data = parse_music_text.search_music(text)
    # Create list
    text = create_text_data(data)
    # send result with list music
    bot.send_message(chat_id,
                     text,
                     reply_markup=create_btn_data(data))
    return None


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    url = 'https://soundcloud.com' + call.data
    threading.Thread(target=send_audio, args=(call.from_user.id, url)).start()
    return None


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Bot for downloading music from the soundcloud.\n"
                     "For example:\n" +
                     emojis.encode(':black_circle:') +
                     " Send track link: ****.com/gvibez/another-rainy-day\n" +
                     emojis.encode(':white_circle:') +
                     " In response, get the file. \n" +
                     " Command: /about \n" +
                     emojis.encode(':warning:') +
                     " You can search track in soundcloud. Now this work in BETA."+
                     emojis.encode(':warning:')
                     )
    return None


@bot.message_handler(commands=['about'])
def url(message):
    bot.send_message(message.chat.id,
                     emojis.encode(':small_blue_diamond:') + " Author: Misha Kaday.\n" +
                     emojis.encode(':small_orange_diamond:') + " Email: kaday506@gmail.com\n" +
                     emojis.encode(':small_blue_diamond:') + " Telegram: @MyNin\n" +
                     emojis.encode(':envelope_with_arrow:') + " I will be glad to hear suggestions.",
                    )
    return None


@bot.message_handler()
def function_name(message):
    print(message.text)

    if 'https://soundcloud.com' in message.text:
        url = str(message.text).split('\n')[-1]
        threading.Thread(target=send_audio, args=(message.chat.id, url,)).start()

    # if send other url
    elif 'https' in message.text and '.com' in message.text or '.ru' in message.text or '.ua' in message.text:
        bot.send_message(message.chat.id,
                         'Bad url, i cant work whit this site. \n'
                         'You can write to the creator with suggestions',
                         reply_markup=create_btn(),
                         )

    else:
        threading.Thread(target=data_finder, args=(message.text, message.chat.id)).start()


# Start
while True:
    bot.polling(none_stop=True)
