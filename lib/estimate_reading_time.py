

def estimate_reading_time(text):
    if text == None or text == "":
            raise Exception("Invalid input!")
    words = len(text.split())
    return words / 200