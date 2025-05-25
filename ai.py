from g4f.client import Client

class AI:
    def __init__(self):
        self.client = Client()
        self.chat_history = {}
    def clear_dialog(self, uid):
        self.chat_history[uid] = []

    def generate_text(self,query,uid):
        if uid not in self.chat_history:
            self.chat_history[uid] = []

        self.chat_history[uid].append({
            'role': 'user',
            'content': query
        })

        try:
            response = self.client.chat.completions.create(
                model = 'gpt-4',
                messages = self.chat_history[uid],
                web_search = False
            )

            text = response.choices[0].message.content
            self.chat_history[uid].append({
                'role':'assistant',
                'content': text
            })
            return text
        except Exception as e:
            return f'Произошла ошибка ({str(e)})'
        
    def generate_image(self, promt):
        try:
            response = self.client.images.generate(
                model = 'flux',
                prompt = promt,
                response_format = 'url'
            )
            url = response.data[0].url
            return url
        except Exception as e:
            raise e
