from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six

def listEntities(text):
    """Detects entities in the text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    entities = client.analyze_entities(document).entities

    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

    result = [entity.name for entity in entities if entity.name.lower() != "home"]
    return result

def showSentiment(text):
    "Calculates sentiment of given text"
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    
    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects sentiment in the document. You can also analyze HTML
    #  document.type == enums.Document.Type.HTML

    sentiment = client.analyze_sentiment(document).document_sentiment

    result = [int(sentiment.score)]
    result.append(int(sentiment.magnitude))

    return result
