import requests


def default_failure(response):
    return response.status_code == 404


class DirBuster:

    def __init__(self, url, failure=default_failure):

        self.url = url
        self.found = []
        self.failure = failure

    def start(self, filename='dirbust/wordlist.txt'):

        with open(filename, 'r') as fp:
            for word in fp:
                word = word.strip()
                url_to_check = '{}{}'.format(self.url, word)
                response = requests.get(url_to_check)
                if not self.failure(response):
                    success = {
                        'url': url_to_check,
                        'status': response.status_code
                    }
                    print("SUCCESS: ", success)
                    self.found.append(success)
                    self.write()
                else:
                    print('FAIL: ', word)

    def write(self):

        with open('out.txt', 'w+') as fp:
            fp.write(str(self.found))
