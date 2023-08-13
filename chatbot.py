from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os.path
# Creating ChatBot Instance
#print(os.path.exists("CollgeChatbot-main\training_data"))
chatbot = ChatBot(
    'CollegeBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)
# with open('CollegeChatbot-main\training_data\personal_ques.txt') as f:
#     contents = f.read()
#     print(contents)

a=os.listdir("D:/CollgeChatbot-main/CollgeChatbot-main/training_data")
print(a)
 #Training with Personal Ques & Ans 
training_data_quesans = open("D:/CollgeChatbot-main/CollgeChatbot-main/training_data/personal_ques.txt").read().splitlines()
training_data_personal = open("D:/CollgeChatbot-main/CollgeChatbot-main/training_data/ques_ans.txt").read().splitlines()
a=os.path.join('D:\CollgeChatbot-main\CollgeChatbot-main\training_data\personal_ques.txt')
training_data = training_data_quesans + training_data_personal

trainer = ListTrainer(chatbot)
trainer.train(training_data) 

#Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
   'chatterbot.corpus.english'
)