from channels.generic.websocket import AsyncJsonWebsocketConsumer
import math
import asyncio


class GameConsumer(AsyncJsonWebsocketConsumer):
    active = False

    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["id"]
        self.group_name = "group_%s" % self.room_id
        await self.accept()

        check = await self.room_is_available()
        if check:
            await self.channel_layer.group_add(self.group_name, self.channel_name)

    async def init_game(self):
        chns = list(self.channel_layer.groups[self.group_name])
        chns.remove(self.channel_name)
        self.opponChan = chns[0]
        self.active = True

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
                    "width": self.properties["width"],
                    "height": self.properties["height"],
                    # "id": ,
                    # "winner": self.symbl,
                },
            },
        )

    async def opponent_proper(self, data):
        event = data["event"]
        if event == "init_game":
            self.oppon = data["data"]
            # self.oppon["x"] = self.canvasW - self.properties["width"]
            await self.send_json(
                {
                    "event": "oppon_pos",
                    "data": {
                        "x": self.oppon["x"],
                        "y": (self.oppon["y"] / self.oppon["height"])
                        * self.properties["height"],
                    },
                }
            )

            if not self.active:
                self.ballUP = False
                await self.init_game()

            else:
                self.ballUP = True
                await self.update_ball()

    def is_collistion(self, player):
        ballRa = int(self.ballprop["radius"])
        ballT = int(self.ballprop["y"]) - ballRa
        ballB = int(self.ballprop["y"]) + ballRa
        ballL = int(self.ballprop["x"]) - ballRa
        ballR = int(self.ballprop["x"]) + ballRa

        playerT = int(player["y"])
        playerB = int(player["y"]) + self.properties["height"]
        playerL = int(player["x"])
        playerR = int(player["x"]) + self.properties["width"]

        return (
            ballR > playerL and ballB > playerT and ballL < playerR and ballT < playerB
        )

    def after_collistion(self, player):
        print("AFTER COLL")
        # WHERE THE BALL HIT THE PLAYER
        collidePoint = self.ballprop["y"] - (player["y"] + player["height"] / 2)

        # NORMALIZATION
        collidePoint = collidePoint / (player["height"] / 2)
        # CALCULATE THE ANGLE IN RADIAN
        angleRad = collidePoint * math.pi / 4
        # X Direction of the ball when it's hit
        direction = 1 if self.ballprop["x"] < self.canvasW / 2 else -1
        # Change velocity of x and y
        self.ballprop["velocityX"] = (
            direction * self.ballprop["speed"] * math.cos(angleRad)
        )
        self.ballprop["velocityY"] = self.ballprop["speed"] * math.sin(angleRad)
        self.ballprop["speed"] += 0.5

    async def update_ball(self):
        if (
            self.ballprop["y"] + self.ballprop["velocityY"] > self.canvasH
            or self.ballprop["y"] + self.ballprop["speed"] < 0
        ):
            self.ballprop["velocityY"] *= -1

        # TODO: check for winner
        if int(self.ballprop["x"]) + int(self.ballprop["velocityX"]) > int(
            self.canvasW
        ):
            print("WIN 1")
            return await self.channel_layer.group_send(
                self.group_name,
                {
                    "type": "ball.movement",
                    "data": {
                        "ball": self.ballprop,
                        "moveX": self.canvasW / 2,
                        "moveY": self.canvasH / 2,
                    },
                },
            )
            # return self.close(1000)
        if int(self.ballprop["x"] + self.ballprop["velocityX"]) < 0:
            print(self.ballprop["x"], " ", self.ballprop["velocityX"])
            print("WIN 2")
            # return self.close(1000)
            return await self.channel_layer.group_send(
                self.group_name,
                {
                    "type": "ball.movement",
                    "data": {
                        "ball": self.ballprop,
                        "moveX": self.canvasW / 2,
                        "moveY": self.canvasH / 2,
                    },
                },
            )

        # check collistion
        if self.is_collistion(self.properties) is True:
            self.after_collistion(self.properties)
        elif self.is_collistion(self.oppon) is True:
            self.after_collistion(self.oppon)

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "ball.movement",
                "data": {
                    "ball": self.ballprop,
                    "moveX": self.ballprop["x"] + self.ballprop["velocityX"],
                    "moveY": self.ballprop["y"] + self.ballprop["velocityY"],
                },
            },
        )

    async def ball_movement(self, data):
        self.ballprop = data["data"]["ball"]
        self.ballprop["x"] = data["data"]["moveX"]
        self.ballprop["y"] = data["data"]["moveY"]
        await self.send_json(
            {
                "event": "ball_movement",
                "y": data["data"]["ball"]["y"],
                "x": data["data"]["ball"]["x"],
                "velocityY": data["data"]["ball"]["velocityY"],
                "velocityX": data["data"]["ball"]["velocityX"],
                "moveX": data["data"]["moveX"],
                "moveY": data["data"]["moveY"],
            }
        )

        if self.ballUP:
            await asyncio.sleep(0.02)
            await self.update_ball()

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
            "height": self.canvasH / 6,
            "width": self.canvasW / 45,
            "x": (
                1
                if len(self.channel_layer.groups[self.group_name]) == 1
                else (self.canvasW - (self.canvasW / 45))
            ),
            "y": (self.canvasH - (self.canvasH / 6)) / 2,
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
            # Send movement data to the front end.
            self.properties["y"] = content["y"]
            await self.send_json(
                {
                    "event": "move",
                    "y": content["y"],
                }
            )
            # Send movement data to the opponent.
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
        self.oppon["y"] = (data["data"]["y"] / self.oppon["height"]) * self.properties[
            "height"
        ]
        await self.send_json(
            {
                "event": "oppon_move",
                "y": (data["data"]["y"] / self.oppon["height"])
                * self.properties["height"],
            }
        )

    async def room_is_available(self) -> bool:
        try:
            membersCnt: int = len(self.channel_layer.groups[self.group_name])
            if membersCnt > 2:
                await self.send_json({"event": "error_msg", "error": "room close."})
                await self.close(1000)
                return False

        except KeyError:
            pass
        return True
