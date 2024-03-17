import openai 

class AdversaGen():
    def __init__(self, key, messages):
        self.api_key = key
        openai.api_key = self.api_key
        self.messages = messages
        print('AdversaGen initialized!')

    def query(self, message):
        #message = input("User : ") 
        if message: 
            self.messages.append( 
                {"role": "user", "content": message}, 
            ) 
            self.chat = openai.ChatCompletion.create( 
                model="gpt-3.5-turbo", messages=self.messages 
            ) 

    def get_reply(self):
        reply = self.chat.choices[0].message.content 
        self.messages.append({"role": "assistant", "content": reply})
        return reply

    def make_call(self, message):
        # send query
        #message = input("User : ") 
        self.query(message)
        print(f"Q: {message}") 

        # get response
        reply = self.get_reply()
        print(f"A: {reply}") 
        return reply
        

