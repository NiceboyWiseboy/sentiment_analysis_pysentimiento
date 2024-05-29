from pysentimiento import create_analyzer


def process_text(text: str):
    analyzer = create_analyzer(task='sentiment', lang='en')
    result = analyzer.predict(text)
    if result.output == 'POS':
        return result.output, result.probas['POS']
    elif result.output == 'NEU':
        return result.output, result.probas['NEU']
    else:
        return result.output, result.probas['NEG']
