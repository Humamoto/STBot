class FeedbackProcessor:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.feedback_data = []

    def add_feedback(self, question, answer, feedback_type):
        feedback_entry = {
            "question": question,
            "answer": answer,
            "feedback": feedback_type
        }
        self.feedback_data.append(feedback_entry)

        if feedback_type == "bom":
            self.knowledge_base.add_text(f"Q: {question} A: {answer}")