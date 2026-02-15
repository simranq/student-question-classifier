def get_urgency(text):

    text = text.lower()

    high_words = ["urgent","asap","immediately","right now","exam tomorrow","deadline today"]
    medium_words = ["soon","quick","help","important","exam","test"]

    if any(word in text for word in high_words):
        return "high"

    elif any(word in text for word in medium_words):
        return "medium"

    else:
        return "low"
