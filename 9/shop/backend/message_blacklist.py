import requests
_message_list = None

def get_message_blacklist():
    global _message_list
    if _message_list is None:
        try:
            response = requests.get('https://raw.githubusercontent.com/swarzech/nlp-1/refs/heads/master/dict/badwords/wulgaryzmy.txt')
            for line in response.text.splitlines():
                line = line.strip()
                if line and not line.startswith('*'):
                    if _message_list is None:
                        _message_list = []
                    _message_list.append(line)
        except requests.RequestException as e:
            print(f"Error fetching message blacklist: {e}")
    return _message_list