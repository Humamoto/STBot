class KnowledgeBase:
    def __init__(self):
        # Simples implementação para exemplo
        self.data = "Senff é uma empresa de tecnologia financeira."

    def search(self, query):
        # Implementação simplificada
        return self.data

    def add_text(self, text):
        self.data += " " + text