from channels.routing import route


channel_routing = {
    # route('http.request',
    #     'chats.consumers.http_request_consumer')

    'websocket.connect': 'chats.consumers.ws_connect',
    'websocket.receive': 'chats.consumers.ws_message',
    'websocket.disconnect': 'chats.consumers.ws_disconnect'
}