
def make_tokens(f):
    """
    Custom tokenizer to split URLs into meaningful words.
    """
    tokens_by_slash = str(f).split('/')
    total_tokens = []
    
    for i in tokens_by_slash:
        tokens = str(i).split('-')
        tokens_dot = []
        for j in range(0, len(tokens)):
            temp_tokens = str(tokens[j]).split('.')
            tokens_dot = tokens_dot + temp_tokens
        total_tokens = total_tokens + tokens + tokens_dot
    
    total_tokens = list(set(total_tokens))
    if 'com' in total_tokens:
        total_tokens.remove('com')
    if 'www' in total_tokens:
        total_tokens.remove('www')
        
    return total_tokens