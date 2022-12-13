from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import model_game
import my_token


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(f'/start\n/help\n/calc')


async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """calculator"""
    msg = (update.message.text).split()
    a = int(msg[1])
    b = int(msg[3])
    if msg[2] == '+':
        result = model_game.sum(a, b) 
    elif msg[2] == '-':
        result = model_game.dif(a, b)
    elif msg[2] == '*':
        result = model_game.mult(a, b)
    elif msg[2] == '/':
        result = model_game.div(a, b)
    await update.message.reply_text(f'{msg[1]}{msg[2]}{msg[3]}={result}')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(my_token.read_token('your_token.txt')).build()


    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("calc", calc_command))
    

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()