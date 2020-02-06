import urllib, requests
class pastebin:
    def __init__(self, paste_name, paste_body):
        self.url = "http://pastebin.com/api/api_post.php"
        self.values = {
          'api_dev_key' : 'cba0c68b866ae744b9bceabd80a8a2da', 
          'api_option' : 'paste',
          'api_paste_code' : f'{paste_body}',
          'api_user_key' : '7051ace19d8604a1c3f2f9a4360cee2f',
          'api_paste_private' : '0',
          'api_paste_name' : f'{paste_name}',
          'api_paste_expire_date' : 'N',
          'api_paste_format' : 'text'
          }
    def push(self):
        data = urllib.parse.urlencode(self.values)
        data = data.encode('utf-8') # data should be bytes
        req = urllib.request.Request(self.url, data)
        with urllib.request.urlopen(req) as response:
            link = response.read().decode('utf-8')
        return link    

