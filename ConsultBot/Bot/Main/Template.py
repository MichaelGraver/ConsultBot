from Bot.models import Sessions

def template_gen(sent, topic, Session):
    template = ""
    temp_used = ""
    if sent == "Positive":
        if topic == "Unclear":
            temp_used = "Do you not have any concerns?"
            template = False
        else:
            temp_used = "Why are you not concerned about the " + topic + "?"
            template = True
    elif sent == "Negative":
        if topic == "Unclear":
            temp_used = "What are your concerns?"
            template = False
        else:
            temp_used = "What concerns you most about the " + topic + "?"
            template = True
    else:
        temp_used = "I'm sorry I don't understand, please try to keep responses about the cost or location."
        template = False
    t = Sessions.objects.get(SessionKey=Session)
    topiccontent = t.Topics
    if topic == "Unclear":
        pass
    elif topic in topiccontent:
        pass
    else:
        t.Topics = (topiccontent + topic)
    t.TemplatesUsed = template
    t.save()
    return temp_used