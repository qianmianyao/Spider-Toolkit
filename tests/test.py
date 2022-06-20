from Tool.headers import Headers


if __name__ == '__main__':
    data = {"data": 1234}
    headers_tool = Headers(data=data).content_length()
    print(headers_tool)