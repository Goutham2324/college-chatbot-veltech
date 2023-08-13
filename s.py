from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Create a chatbot
bot = ChatBot('College Bot')

# Set up the trainer
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english.college')

# Define the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define the chatbot response function
@app.route('/get')
def get_bot_response():
    user_text = request.args.get('msg')
    bot_response = str(bot.get_response(user_text))
    return bot_response

if __name__ == '__main__':
    app.run(debug=True)
