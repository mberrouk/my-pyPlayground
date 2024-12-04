from channels.generic.websocket import AsyncJsonWebsocketConsumer


class GameConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["id"]
        self.group_name = "group_%s" % self.room_id
        print("room id: ", self.room_id, " group: ", self.group_name)

        await self.accept()
        # check group
        try:
            if len(self.channel_layer.groups[self.group_name]) == 2:
                print("Room closed!")
                await self.send_json({"event": "error_msg", "error": "room close."})
                return await self.close(1000)

        except KeyError:
            pass

        await self.channel_layer.group_add(self.group_name, self.channel_name)

    async def send(self):
        print("send")
        pass

    async def receive(self, text_data):
        print("receive ", text_data)
        pass
