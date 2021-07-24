from telegram.ext import Updater, CommandHandler

def start_bot(bot, updater):
	print("Hello")

def main():
	updtr = Updater('1774377160:AAFG2PTkuLAY08J4lFzhlKwkouDstICKxhw')

updtr.dispatcher.add_handler(CommandHandler("start", start_bot))

	updtr,start_polling()
	updtr.idle()

if __name__ == "__main__":
	main()

