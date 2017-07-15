# bandwidth_bxml
Bandwidth BXML Generator for Python

Pure python implmenetation of Bandwidth BXML generator that works without needing to install lxml. This library works on AWS Lambda without needing to compile lxml.

# installation
```
pip install bandwidth_bxml
```

# usage
```python
from bandwidth_bxml import Response

def speak():
    response = Response()
    response.speak("Hello World")
    return response.to_string()


def gather():
    response = Response()
    gather = response.gather("https://gather.url/nextBXML")
    gather.speak("Please, press a digit")
    return response.to_string()
    
```

    
# Build instructions
python setup.py build sdist
