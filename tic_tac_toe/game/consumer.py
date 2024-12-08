from django.http.request import RAISE_ERROR
from django.utils.functional import empty
from channels.generic.websocket import AsyncJsonWebsocketConsumer

import random


class GameConsumer(AsyncJsonWebsocketConsumer):
    symbl: str = ""
    myTurn: bool = False
    winCount: int = 0
    rounds: int = 0
    board: dict = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
    }

    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["id"]
        self.group_name = "group_%s" % self.room_id

        # accept connection
        await self.accept()

        check, membersCnt = await self.room_is_available()
        if check:
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            if membersCnt == 1:
                await self.init_game()

    async def init_game(self):
        playersL = list(self.channel_layer.groups[self.group_name])
        firstP = random.choice(playersL)
        playersL.remove(firstP)
        playersL.insert(0, firstP)
        self.rounds += 1
        for i, chName in enumerate(playersL):  # chName:  the channel name
            await self.channel_layer.send(
                chName,
                {
                    "type": "syncGameData",
                    "data": {
                        "event": "game_start",
                        "board": self.board,
                        "myTurn": True if i == 0 else False,
                        "symbl": "X" if i == 0 else "O",
                        "winCnt": self.winCount if chName == self.channel_name else "",
                        "round": self.rounds,
                    },
                },
            )

    async def syncGameData(self, context):
        if context["data"]["event"] == "game_start":
            self.symbl = context["data"]["symbl"]
            self.myTurn = context["data"]["myTurn"]
            self.rounds = int(context["data"]["round"])
            if context["data"]["winCnt"] == "":
                context["data"]["winCnt"] = self.winCount
            for key in self.board.keys():
                self.board[key] = ""

        elif context["data"]["event"] == "marke_square":
            pos = int(context["data"]["id"])
            symbl = context["data"]["symbl"]
            self.board[pos] = symbl
            self.myTurn = True if symbl is not self.symbl else False

        await self.send_json(context["data"])

    def is_winMove(self, move) -> bool:
        board = self.board
        horizontalCheck: bool = (
            (len(board[1]) > 0 and (board[1] == board[2] == board[3]))
            or (len(board[4]) > 0 and board[4] == board[5] == board[6])
            or (len(board[7]) > 0 and board[7] == board[8] == board[9])
        )
        verticalCheck: bool = (
            (len(board[1]) > 0 and (board[1] == board[4] == board[7]))
            or (len(board[2]) > 0 and board[2] == board[5] == board[8])
            or (len(board[3]) > 0 and board[3] == board[6] == board[9])
        )
        diagonalCheck: bool = (
            len(board[1]) > 0 and (board[1] == board[5] == board[9])
        ) or (len(board[3]) > 0 and board[3] == board[5] == board[7])

        return horizontalCheck or verticalCheck or diagonalCheck

    async def frontEndRecv_traitMove(self, move):
        movement: int

        try:
            movement = int(move)
            isAvalidMove = (
                movement >= 1 and movement <= 9 and not len(self.board[movement])
            )

            if isAvalidMove is False:
                raise ValueError

            self.board[movement] = self.symbl
            if self.is_winMove(movement) is True:
                self.winCount += 1
                await self.channel_layer.group_send(
                    self.group_name,
                    {
                        "type": "syncGameData",
                        "data": {
                            "event": "victory_announce",
                            "id": movement,
                            "winner": self.symbl,
                        },
                    },
                )
                await self.init_game()
            else:
                await self.channel_layer.group_send(
                    self.group_name,
                    {
                        "type": "syncGameData",
                        "data": {
                            "event": "marke_square",
                            "id": movement,
                            "symbl": self.symbl,
                        },
                    },
                )

        except ValueError:
            await self.send_json({"event": "error_msg", "error": "invalid movement!"})

    async def receive_json(self, content, **kwargs):
        if content["event"] == "player_movement":
            await self.frontEndRecv_traitMove(content["move"])

    async def room_is_available(self) -> tuple[bool, int]:
        membersCnt: int = 0
        try:
            membersCnt = len(self.channel_layer.groups[self.group_name])
            if membersCnt >= 2:
                await self.send_json({"event": "error_msg", "error": "room close."})
                await self.close(1000)
                return False, membersCnt

        except KeyError:
            pass
        return True, membersCnt

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        # TODO: stop game
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "syncGameData",
                "data": {
                    "event": "error_msg",
                    "error": "the Player %s has disconnect." % self.symbl,
                },
            },
        )
