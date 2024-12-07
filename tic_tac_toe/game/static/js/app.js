// Game Data
let board = null;
let myTurn = false;
let gameSymbl = '';

// HTML elements
const squares = document.getElementsByClassName('square');
const turnField = document.getElementById('turn');
const symbolField = document.getElementById('symbol');
const roundField = document.getElementById('round');
const victoryField = document.getElementById('victory');

// Connection
let ws;

/**
 * Makes a movement by marking the squre position with new
 * HTLM element.
 * Sets a custom attribute to indicate that the square has
 * been marked.
 */
function draw_move(element, player) {
  element.innerHTML = `<p class="player-letter" >${player}</p>`
  element.setAttribute('marked', player)

  // TODO: add styling for the marked squre
  // setTimeout(() => {
  //   element.children[0].classList.add('active')
  // }, 1);
  element.removeEventListener('click', handle_click);
}

/* *
 * Marks a square on the TTT board (player attempts to make a move).
 */
function handle_click(e) {
  // check & draw the player movement
  console.log(e);
  const checkMovement = myTurn && !e.currentTarget.innerHTML
    && !e.currentTarget.getAttribute('marked');

  if (checkMovement === true) {
    ws.send(JSON.stringify({
      event: 'player_movement',
      move: e.currentTarget.id,
    }));
    // draw_move(e.currentTarget);
  }
  // disable the event listener
}


function reset_the_board() {
  for (let i = 0; i < squares.length; ++i) {
    squares[i].removeAttribute('marked');
    squares[i].innerHTML = "";
    squares[i].addEventListener('click', handle_click);
  }
}

// WebSocket Client
{
  document.addEventListener('DOMContentLoaded', () => {
    ws = new WebSocket("ws://127.0.0.1:8000/ws/game/2/");
    // Setup the board
    for (let i = 0; i < squares.length; ++i) {
      squares[i].addEventListener('click', handle_click);
    }
    ws.onconnect = (e) => {
      console.log(e);
    }

    ws.onclose = (e) => {
      console.log(e);
    }

    ws.onmessage = (e) => {
      const data = JSON.parse(e.data);
      console.log(data)
      // check errors
      if (data.event === "error_msg") {
        Swal.fire({
          icon: 'error',
          title: data.error,
        }).then(() => window.location = '/')
      }
      else if (data.event === "game_start") {
        board = data.board;
        myTurn = data.myTurn;
        gameSymbl = data.symbl;
        symbolField.innerHTML = gameSymbl;
        turnField.innerHTML = (myTurn) ? gameSymbl : (gameSymbl === "O") ? "X" : "O";
        roundField.innerHTML = data.round;
        victoryField.innerHTML = data.winCnt;
        // print(turnField)
      }
      else if (data.event === "marke_square") {
        draw_move(squares[data.id - 1], data.symbl);
        myTurn = (data.symbl === gameSymbl) ? false : true;
        turnField.innerHTML = (myTurn) ? gameSymbl : (gameSymbl === "O") ? "X" : "O";
      }
      else if (data.event === "victory_announce") {
        draw_move(squares[data.id - 1], data.winner);
        // myTurn = (data.symbl === gameSymbl) ? false : true;
        Swal.fire({
          icon: (data.winner === gameSymbl) ? 'success' : 'error',
          title: (data.winner === gameSymbl) ? data.winner + " Congratulations!" : data.winner + " Is Win",
        }).then(reset_the_board)

      } else if (data.event === "") {
      } else if (data.event === "") {
      }

    }
  });
}
//



