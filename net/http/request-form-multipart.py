import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

data = MultipartEncoder(
    fields={
        'field0': 'value0',
        'field1': 'value1',
        'field2': 'value2'
    }
)

headers = {'Content-Type': data.content_type}

response = requests.post('http://httpbin.org/post', data=data, headers=headers)

# The response body can be accessed with response.text or response.json() for JSON responses
print(response.text)
