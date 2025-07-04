import telebot
import os
import time
import threading

# Variabili d'ambiente da Railway
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = telebot.TeleBot(TOKEN)

# Comando di test per confermare che il bot funziona
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Amazon Hunter attivo e funzionante!")

# Funzione per inviare un messaggio ogni X tempo (test ogni ora)
def loop_annuncio():
    while True:
        try:
            messaggio = "🔥 Offerta di prova da Amazon Hunter"
            bot.send_message(CHANNEL_ID, messaggio)
            print("Messaggio inviato correttamente.")
        except Exception as e:
            print("Errore nell'invio del messaggio:", e)
        time.sleep(3600)  # ogni ora (3600 secondi)

# Avvio del bot e del loop messaggi
if __name__ == "__main__":
    print("Avvio Amazon Hunter...")
    threading.Thread(target=loop_annuncio).start()
    bot.infinity_polling()
