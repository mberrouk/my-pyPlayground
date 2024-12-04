from channels.consumer import AsyncConsumer


class EchoConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        self.room_name = "hello"
        self.room_group = "helloG"
        self.channel_layer.group_add(self.room_group, self.channel_name)
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, event):
        await self.send({"type": "websocket.send", "text": event["text"]})

    async def websocket_disconnect(self, event):
        pass
