from argparse import Action
from ast import Return
from cgitb import text
from email import message
from fileinput import filename
from socket import timeout
from turtle import update
from telegram import Update
import random
import qrcode
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ChatAction, InlineKeyboardButton, InlineKeyboardMarkup
import os
from PIL import Image


#Ingresa en esta parte el token de tu box generado con BotFather
updater = Updater('***ACA VA EL TOKEN DE TU BOT')

INPUT_QR= 0
arrayFras= ['A veces quieres rendirte con la guitarra, la odiarás, pero si no te rindes con ella, serás recompensado - Jimi Hendrix', 'No seré una estrella del rock. Seré una leyenda - Freddie Mercury', 'Prefiero que la gente me odie por ser quien soy a que me ame por lo que no soy - Kurt Cobain', 'El verano de 1973 fue fantástico. No me acuerdo de nada, pero nunca lo olvidaré - Lemmy Kilmiste', 'Hay quien piensa que si vas muy lejos, no podrás volver donde están los demás - Frank Zappa', 'Tu mejor amigo y mi peor enemigo son uno mismo - Bob Dylan', 'Que seas un paranoico no quiere decir que no te persigan - Kurt Cobain', 'Si no sabes adónde vas, cualquier camino te llevará - George Harrison', 'Todo lo que necesitas es amor - John Lennon', 'Tienes que aprender a caer antes de aprender a volar - Paul Simon', ]

def start(update: Update, context: CallbackContext):
    update.message.reply_text(f'{update.effective_user.first_name} Rock and roll nenenennn!!!')

def frase (update: Update, context: CallbackContext):
    tex= random.choice(arrayFras)
    update.message.reply_text(tex)
    
def cancion(update: Update, context: CallbackContext):
    text= update.message.reply_text(f"Selecciona un boton y te recomendamos una cancion o un disco",
    reply_markup=InlineKeyboardMarkup([
    [InlineKeyboardButton(text='Cancion 1', callback_data='cancion01')],
    [InlineKeyboardButton(text='Cancion 2', callback_data='cancion02')],
    [InlineKeyboardButton(text='Cancion 3', callback_data='cancion03')],
    [InlineKeyboardButton(text='Cancion 4', callback_data='cancion04')],
    [InlineKeyboardButton(text='Cancion 5', callback_data='cancion05')],
    [InlineKeyboardButton(text='Cancion 6', callback_data='cancion06')],
    [InlineKeyboardButton(text='Cancion 7', callback_data='cancion07')],
    [InlineKeyboardButton(text='Cancion 8', callback_data='cancion08')],
    [InlineKeyboardButton(text='Cancion 9', callback_data='cancion09')],
    [InlineKeyboardButton(text='Cancion 10', callback_data='cancion10')]
    ])
)
    

def qr_command_handler(update: Update, context: CallbackContext):
    update.message.reply_text(f"Envia el texto para generar el codigo QR")
    return INPUT_QR

def cancion_callback01(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
    text= "Soy la piñata del Rock And Roolll... Escucha Ac Dc - It's a Long Way to the Top"
    )
    
def cancion_callback02(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
    text= "Por si aun no conoces este discazo... The Rolling Stones - Exile On Main St"
    )

def cancion_callback03(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
    text= "Janis Joplin - Summertime"
    )
    
def cancion_callback04(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
    text= "Ozzy Osbourne - Crazy Train"
    )

def cancion_callback05(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
    text= "Te tiro uno de Pink Floyd - Coming Back To Life"
    )
    
def cancion_callback06(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
    text= "The Ramones - I Wanna Live"
    )

def cancion_callback07(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
    text= "Te gusta el progresivo? King Crimson - Starless"
    )

def cancion_callback08(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
    text= "Keith Richards - Eileen"
    )

def cancion_callback09(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
    text= "Sumo Estallando Desde El Oceano"
    )

def cancion_callback10(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
    text= "Lou Reed Hangin Round"
    )

def generate_qr(text):
    filename= text + '.jpg'
    
    img=  qrcode.make(text)
    img.save(filename)
    
    return filename

def send_qr(filename, chat):
    
    chat.send_action(
        action = ChatAction.UPLOAD_PHOTO,
        timeout = None
    )

    chat.send_photo(
        photo = open(filename, 'rb')
    )

    os.unlink(filename)

def input_text (update: Update, context: CallbackContext):
    text= update.message.text
    print(text)
    filename = generate_qr(text)
    chat = update.message.chat
    
    send_qr(filename, chat)
    
    return ConversationHandler.END

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('frase', frase))
updater.dispatcher.add_handler(CommandHandler('cancion', cancion))
updater.dispatcher.add_handler(ConversationHandler(
    entry_points=[
        CommandHandler('qr', qr_command_handler),
        CallbackQueryHandler(pattern='cancion01', callback=cancion_callback01),
        CallbackQueryHandler(pattern='cancion02', callback=cancion_callback02),
        CallbackQueryHandler(pattern='cancion03', callback=cancion_callback03),
        CallbackQueryHandler(pattern='cancion04', callback=cancion_callback04),
        CallbackQueryHandler(pattern='cancion05', callback=cancion_callback05),
        CallbackQueryHandler(pattern='cancion06', callback=cancion_callback06),
        CallbackQueryHandler(pattern='cancion07', callback=cancion_callback07),
        CallbackQueryHandler(pattern='cancion08', callback=cancion_callback08),
        CallbackQueryHandler(pattern='cancion09', callback=cancion_callback09),
        CallbackQueryHandler(pattern='cancion10', callback=cancion_callback10)
        ],
            
    states={
        INPUT_QR: [MessageHandler(Filters.text, input_text)]
        },
    
    fallbacks=[],
))

updater.start_polling()
updater.idle()