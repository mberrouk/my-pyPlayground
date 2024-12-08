from channels.generic.websocket import AsyncJsonWebsocketConsumer


class GameConsumer(AsyncJsonWebsocketConsumer):
    active = False

    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["id"]
        print("id === ", self.room_id)
        self.group_name = "group_%s" % self.room_id
        await self.accept()

        check, membersCnt = await self.room_is_available()
        if check:
            await self.channel_layer.group_add(self.group_name, self.channel_name)

    async def init_game(self):
        chns = list(self.channel_layer.groups[self.group_name])
        chns.remove(self.channel_name)
        self.opponChan = chns[0]
        self.active = True
        # self.opponChan = chns.

        await self.channel_layer.send(
            self.opponChan,
            {
                "type": "opponent.proper",
                "event": "init_game",
                "data": {
                    "canvasH": self.canvasH,
                    "canvasW": self.canvasW,
                    "x": self.properties["x"],
                    "y": self.properties["y"],
                    # "id": ,
                    # "winner": self.symbl,
                },
            },
        )

    async def opponent_proper(self, data):
        event = data["event"]
        if event == "init_game":
            self.oppon = data["data"]
            await self.send_json(
                {
                    "event": "oppon_pos",
                    "data": {
                        "x": self.canvasW - self.properties["width"],
                        "y": self.oppon["y"],
                    },
                }
            )

            if not self.active:
                await self.init_game()

    def init_data(self, data):
        self.canvasH = int(data["canvasH"])  # data from front
        self.canvasW = int(data["canvasW"])  # ...
        self.ballprop = {
            "x": self.canvasW / 2,
            "y": self.canvasH / 2,
            "radius": int(data["ballradius"]),
            "speed": 5,
            "velocityX": 5,
            "velocityY": 5,
        }
        self.properties = {
            "x": 1,
            "y": (self.canvasH - (self.canvasH / 6)) / 2,
            "height": self.canvasH / 6,
            "width": self.canvasW / 45,
        }

    async def receive_json(self, content, **kwargs):
        event = content["event"]
        if event == "init":
            self.init_data(content)
            await self.send_json(
                {
                    "event": "initial",
                    "ball": self.ballprop,
                    "proper": self.properties,
                }
            )
            if len(self.channel_layer.groups[self.group_name]) == 2:
                await self.init_game()

        if event == "player_move":
            await self.send_json(
                {
                    "event": "move",
                    "y": content["y"],
                }
            )

            print("DEBUG :: ", self.opponChan)
            print("DEBUG :: ", self.channel_name)

            await self.channel_layer.send(
                self.opponChan,
                {
                    "type": "oppon.move",
                    "data": {
                        "y": content["y"],
                    },
                },
            )

    async def oppon_move(self, data):
        await self.send_json(
            {
                "event": "oppon_move",
                "y": data["data"]["y"],
            }
        )

    async def room_is_available(self) -> tuple[bool, int]:
        membersCnt: int = 0
        try:
            membersCnt = len(self.channel_layer.groups[self.group_name])
            if membersCnt > 2:
                await self.send_json({"event": "error_msg", "error": "room close."})
                await self.close(1000)
                return False, membersCnt

        except KeyError:
            pass
        return True, membersCnt
