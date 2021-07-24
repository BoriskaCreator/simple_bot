import logging
from telegram.ext import Updater, CommandHandler, CallbackContext

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
	                level=logging.INFO,
	                filename='bot.log'
	                )

def start_bot(update: Updater, context: CallbackContext):
	print(update)
	mytext = """ Hello {}

	I have only /start command! =)""".format(update.message.chat.first_name)
	update.message.reply_text(mytext)

def main():
	updtr = Updater()
	
	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))

	updtr.start_polling()
	updtr.idle()

if __name__ == "__main__":
	logging.info('Bot started!')
	main()
