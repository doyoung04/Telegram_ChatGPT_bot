import telegram
from telegram.ext import Updater, MessageHandler, Filters
import openai

# Replace with your Telegram bot API token
telegram_token = 'YOUR_API_TOKEN'

# Replace with your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Initialize the Telegram bot
bot = telegram.Bot(token=telegram_token)
print("Telegram bot initialized.")

# Define a function to handle incoming messages
def handle_message(update, context):
    message = update.message.text
    print(f"Received message: {message}")
    
    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=128,
        n=1,
        stop=None,
        temperature=0.8,
        presence_penalty=0.6,
    )
    print(f"Generated response: {response.choices[0].text}")
    
    # Send the response back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)
    print("Response sent.")

# Start the Telegram bot
updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
updater.start_polling()
print("Bot started, listening for incoming messages...")
