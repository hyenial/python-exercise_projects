import urllib

def read_text():
    quotes = open("movie_quotes (1).txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    safe_text = urllib.parse.quote(text_to_check)
    #print(safe_text)
    req = urllib.request.Request("http://www.wdylike.appspot.com/?q="+safe_text)
    response = urllib.request.urlopen(req)
    output = str(response.read())

    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words.")
    else:
        print("Unable to scan the document.")
