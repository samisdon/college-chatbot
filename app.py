import json
import gradio as gr

with open("faqs.json", "r") as f:
    faq_data = json.load(f)

def chatbot_response(user_input):
    user_input = user_input.lower()
    for keyword, answer in faq_data.items():
        if keyword in user_input:
            return answer
    return "I'm sorry, I couldn't understand. Ask about courses, admission, hostel, or placements."

iface = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Ask me about the college..."),
    outputs="text",
    title="🎓 College Enquiry Chatbot"
)

if __name__ == "__main__":
    iface.launch()
