from bandwidth_bxml import Response


def test_speak():
    response = Response()
    response.speak("Hello World")
    expected = '<?xml version="1.0" encoding="UTF-8"?><Response><SpeakSentence gender="female" locale="en_US" voice="susan">Hello World</SpeakSentence></Response>'
    actual = response.to_string()
    assert actual == expected


def test_gather():
    response = Response()
    gather = response.gather("https://gather.url/nextBXML")
    gather.speak("Please, press a digit")
    expected = '<?xml version="1.0" encoding="UTF-8"?>' \
               '<Response>' \
               '<Gather requestUrl="https://gather.url/nextBXML">' \
               '<SpeakSentence gender="female" locale="en_US" voice="susan">Please, press a digit</SpeakSentence>' \
               '</Gather>' \
               '</Response>'
    actual = response.to_string()
    assert actual == expected
