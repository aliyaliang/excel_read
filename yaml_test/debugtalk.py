import requests


def get_token(user="yoyo", psw="123456"):
    s = requests.session()
    r = s.request(method="POST",
                  url="http://49.235.92.12:7005/api/v1/login",
                  json={
                      "username": user,
                      "password": psw
                  },
                  headers={
                      "Content-Type": "application/json",
                      "User-Agent": "Fiddler"
                  })
    print(r.content)
    print(r.headers)
    return r.json().get("token")

if __name__ == '__main__':
    token = get_token()
    print(token)