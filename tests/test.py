from Tool.headers import Headers

if __name__ == '__main__':
    data = {"data": 1234}
    headers_tool = Headers().content_length(data=data)
    assert headers_tool == 13

    print(Headers().user_agent(random_mode=True))
