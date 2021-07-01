from FoundingTitanRobot import mongodb as db_x

eren = db_x["CHATBOT"]


def add_chat(chat_id):
    stark = eren.find_one({"chat_id": chat_id})
    if stark:
        return False
    else:
        eren.insert_one({"chat_id": chat_id})
        return True


def remove_chat(chat_id):
    stark = eren.find_one({"chat_id": chat_id})
    if not stark:
        return False
    else:
        eren.delete_one({"chat_id": chat_id})
        return True


def get_all_chats():
    r = list(eren.find())
    if r:
        return r
    else:
        return False


def get_session(chat_id):
    stark = eren.find_one({"chat_id": chat_id})
    if not stark:
        return False
    else:
        return stark
