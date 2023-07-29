class Conversation:
    def __init__(self):
        self.conversation_history = []

    def add_message(self, role, content):
        message = {"role": role, "content": content}
        self.conversation_history.append(message)

    def get_messages(self):
        return list(filter(lambda conversation: conversation['content'] is not None, self.conversation_history))

    def display_conversation(self, detailed=False):
        for message in self.conversation_history:
            if message['content'] is None:
                print(f"{message['role']}: {message['function_call']}\n")
            else:
                print(f"{message['role']}: {message['content']}\n")
