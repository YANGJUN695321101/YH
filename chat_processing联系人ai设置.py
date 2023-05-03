from modules.gpt35_chat import generate_gpt35_response

def process_input(user_input, active_contact):
    if active_contact == "老王":
        prompt = f"老王: {user_input}"
    elif active_contact == "鸡哥":
        prompt = f"鸡哥: {user_input}"
    else:
        return "未知联系人"

    response = generate_gpt35_response(prompt)
    return response
