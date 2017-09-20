import urllib.request

if __name__ == "__main__"
    print("Hello")
    req = urllib.request.Request("http://www.google.com")
    data = urllib.request.urlopen(req).read() # data = 구글로

    print(data)

    f = open("./response.txt", "w")
    f.write(str(data))
    f.close()
