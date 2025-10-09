"""
A function called make_snippet that takes 
a string as an argument and returns the first 
five words and then a '...' if there are more than that.
"""
def make_snippet(str):
    if len(str.split(" ")) > 5:
        words = str.split(" ")
        snippet = ' '.join(words[:5]) + ' ...'
        return snippet
    else:    
        return str