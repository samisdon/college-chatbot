import gradio as gr

def college_chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! 👋 How can I help you today?"
    elif "admission" in user_input:
        return "🎓 Admissions are based on entrance exams followed by counseling."
    elif "courses" in user_input or "subjects" in user_input:
        return "📚 We offer B.Tech, B.Sc, BBA, and MCA programs."
    elif "hostel" in user_input:
        return "🏠 We have separate hostels for boys and girls with Wi-Fi and mess facilities."
    elif "library" in user_input:
        return "📖 Our library has over 20,000 books and digital resources for all departments."
    elif "placement" in user_input or "company" in user_input:
        return "💼 Top recruiters include TCS, Infosys, Wipro, and Amazon."
    elif "fees" in user_input or "fee" in user_input:
        return "💰 Course fees vary by program. Please visit our website or contact the admin office for details."
    elif "sports" in user_input or "gym" in user_input:
        return "🏅 We have cricket, football, basketball grounds, and a fully equipped gym."
    elif "faculty" in user_input or "teacher" in user_input:
        return "👩‍🏫 Our faculty members are highly qualified with industry and research experience."
    elif "location" in user_input or "where" in user_input:
        return "📍 The college is located near the city center with easy transport access."
    else:
        return "🤔 I'm sorry, I couldn't understand that. Please ask something about the college."

# Gradio interface
iface = gr.Interface(
    fn=college_chatbot,
    inputs=gr.Textbox(label="Ask something about the college"),
    outputs="text",
    title="🎓 College Chatbot",
    description="Ask about admissions, courses, fees, hostels, placements, and more!"
)

iface.launch()
