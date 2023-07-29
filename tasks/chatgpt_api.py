import openai
from conversation import Conversation


class ApiChatGPT:
    gpt_model = 'gpt-3.5-turbo-0613'
    embedding_model = 'text-embedding-ada-002'

    sentiment_prompt = """
    Given the article below, assess the impact of that news on the price of coins in the article. Pretend you are a financial expert.
    You are a financial expert with crypto currency recommendation experience. Then summarize the article. Answer “YES” if good news, “NO” if bad news, or “UNKNOWN” if uncertain, and explain why.
    Short answer, no explanation.
    Response format: 
    - YES or NO or UNKNOWN
    - EXPLAIN: explain why
    - SUMMARY: summarization of the article
    
    Article: {}
    """

    @staticmethod
    def get_all_models():
        models = openai.Model.list()
        return models

    def chat_completion(self, messages, functions):
        payload = {
            "model": self.gpt_model,
            "messages": messages
        }
        if functions is not None:
            payload.update({"functions": functions})
        chat_completion = openai.ChatCompletion.create(**payload)
        return chat_completion.choices[0]

    def get_embedding(self, text, api_key):
        try:
            openai.api_key = api_key
            payload = {
                "input": [text],
                "model": self.embedding_model
            }
            embedding = openai.Embedding.create(**payload)
            return embedding.data[0].embedding
        except Exception as e:
            return None

    def get_sentiment(self, text, api_key):
        try:
            openai.api_key = api_key
            conversation = Conversation()
            conversation.add_message("system", self.sentiment_prompt.format(text))
            response = self.chat_completion(conversation.get_messages(), None)
            return response
        except Exception as e:
            return None


api_chat_gpt = ApiChatGPT()


def test_conversation():
    api_chat_gpt = ApiChatGPT()
    conversation = Conversation()
    conversation.add_message("system",
                             "You are an company administrator who can access to Rikkeisoft's internal resources and can answer any questions about Rikkeisoft company. While answering, think step-by-step and justify your steps")
    conversation.add_message("user",
                             "Hello")
    # "Has tungtt received any notable recognition or awards during their time at Rikkeisoft?")
    response = api_chat_gpt.chat_completion(conversation.get_messages(), None)
    print(response)


def test_embedding():
    api_chat_gpt = ApiChatGPT()
    response = api_chat_gpt.get_embedding(
        "Block.one ICO damages ‘far beyond’ $22M, ENF founder says. Block.one owes much more to EOS investors than just $22 million after the $4-billion ICO, EOS Network Foundation CEO Yves La Rose believes.")
    print(len(response))


if __name__ == '__main__':
    test_embedding()
