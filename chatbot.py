
import re  # For pattern matching

def chatbot():
    print("Chatbot: Hello! I'm Rule-based Chatseek. Ask me anything about AI, or type 'bye' to exit.")

    while True:
        user_input = input("Ask: ").lower().strip()

        # Exit condition
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day.")
            break

        # Greetings
        elif re.search(r'\b(hi|hello|hey)\b', user_input):
            print("Chatbot: Hello! How can I assist you with AI today?")

        # Asking about chatbot
        elif "your name" in user_input:
            print("Chatbot: I'm Chatseek, your AI-friendly chatbot.")

        # Asking about well-being
        elif "how are you" in user_input:
            print("Chatbot: I'm just code, but I'm functioning perfectly! Ready to talk AI.")

        # Asking for help
        elif "help" in user_input or "support" in user_input:
            print("Chatbot: You can ask me basic questions about Artificial Intelligence like 'what is AI' or 'why is AI important'.")

        # AI-specific Q&A (lowercase match)
        elif "what is ai" in user_input:
            print("Chatbot: AI stands for Artificial Intelligence. It means machines that perform tasks requiring human intelligence, like learning or problem-solving.")

        elif "why is ai important" in user_input:
            print("Chatbot: AI helps automate tasks, improve decisions, and enhance experiences in fields like healthcare, education, and finance.")

        elif "can ai think" in user_input:
            print("Chatbot: AI can simulate thinking by analyzing data and making decisions, but it doesn’t truly understand or feel.")

        elif "what is machine learning" in user_input:
            print("Chatbot: Machine learning is a subfield of AI that allows systems to learn from data and improve over time without explicit programming.")

        elif "does ai have emotions" in user_input:
            print("Chatbot: No, AI doesn't have emotions. It can simulate emotional responses but doesn’t truly experience feelings.")

        elif "where is ai used" in user_input:
            print("Chatbot: AI is used in self-driving cars, virtual assistants, recommendation systems, fraud detection, and more.")

        elif "who invented ai" in user_input:
            print("Chatbot: The term 'AI' was coined by John McCarthy in 1956, one of the founders of the field.")

        else:
            print("Chatbot: I'm not sure I understand. Please ask a basic question about AI.")

# Run the chatbot
chatbot()
