def order(sentence):
    result = " ".join(sorted(sentence.split(), key=lambda x: list(filter(str.isdigit, x))))
    return result
