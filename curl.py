import sys
import requests

from urllib.parse import urlparse


def parse(argument):

    parsed_url = urlparse(argument)
    print(f'Connecting to: {parsed_url.hostname}')
    print(f'Sending request: {parsed_url.scheme}:{parsed_url.path} {parsed_url.query}')
    print(f'Fragment: {parsed_url.fragment}')

    response = requests.get(argument)
    # Print the status code
    print(response.status_code)

    # Print the response body
    print(response.text)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(f'Parsing url, {sys.argv[1]}!')
        parse(sys.argv[1])
    else:
        print('Invalid argument')
