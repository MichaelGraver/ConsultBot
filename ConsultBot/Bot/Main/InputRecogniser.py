import re, difflib
# Functions for populating the knowledge base
from Bot.Main.SentimentDict import pos_files, neg_files, read_det_file, read_negate_file
#from classify import classify
from Bot.Main.Topic import topic_match
from Bot.Main.Sentiment import sent_match
from Bot.Main.Template import template_gen
from Bot.models import Sessions, Statements

# Generates a list of known determiners
basal_determiner_bank = read_det_file()
# Generates a list of known negators
negators_bank = read_negate_file()
posWords = pos_files()
negWords = neg_files()
# # Text to be parsed
def InputRec(text, Session):
    t = Sessions.objects.get(SessionKey=Session)
    if t.TemplatesUsed == False:
        sent = sent_match(text, posWords, negWords, negators_bank)
        topic = topic_match(text)
        t.CurrentTopic = topic
        t.save()
        Reply = template_gen(sent, topic, Session)
    elif t.TemplatesUsed == True:
        if t.TopicComplete == False:
            if t.ReasonGiven == False:
                Set = {}
                for i in Statements.objects.filter(topic=t.CurrentTopic):
                    trial = i.statement
                    Score = difflib.SequenceMatcher(None, trial, text).ratio()
                    Set[trial] = Score
                print(Set)
                Confidence = max(Set.values())
                Match = max(Set, key=lambda i: Set[i])
                if Confidence >= 0.6:
                    Reply = "Why do you think that?"
                    t.CurrentStatement = Match
                    t.ReasonGiven = True
                    t.save()
                else:
                    Reply = "What do you suggest?"
                    t.TopicComplete = True
                    t.save()
            elif t.ReasonGiven == True:  
                    S = Statements.objects.get(statement__icontains=t.CurrentStatement)
                    link = S.counters
                    T = Statements.objects.get(id=link)
                    if T.response == "False":
                        Reply = ("Do you not think " + str(T.statement) + "?")
                        t.ReasonGiven = False
                        t.CurrentStatement = ""
                        t.save()
                    else:
                        Reply = str(T.response)
                        t.ReasonGiven = False
                        t.CurrentStatement = ""
                        t.save()
        else:
            topicsused = t.Topics
            if topicsused == "Cost":
                NextTopic = "Location"
                Reply = ("Do you have any other concerns? What about the " + NextTopic + "?" + '\n' + " If you have no other concerns click End to stop.")
            elif topicsused == "Location":
                NextTopic = "Cost"
                Reply = ("Do you have any other concerns? What about the " + NextTopic + "?" + '\n' + "If you have no other concerns click End to stop.")
            else:
                Reply = "Thank you for taking part, please remember to complete the questionnaire"
            t.TemplatesUsed = False
            t.ReasonGiven = False
            t.TopicComplete = False
            t.CurrentTopic = ""
            t.save()
    return Reply

			