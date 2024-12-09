//
const pcount = document.getElementById("player-score");
const cocount = document.getElementById("computer-score");
//
let pcnt = 0;
let ccnt = 0;

pcount.textContent = pcnt;
cocount.textContent = ccnt;
// Setup canvas
const canvasWidth = 800;
const canvasHeight = 600;
const canvas = document.getElementById('game-canvas');
if (!canvas.getContext) { alert('canvas is not supported'); }
const canvasCtx = canvas.getContext('2d');
//

//Game environment
const boardColor = 'green';
const boardCentre = 'grey';
const ballColor = 'white';
const ballradius = 10;
const playerColor = 'red';
const opponeColor = 'yellow';
//

//
let BALL;        // the ball object
let player;
let opponent;
//

//
let ballDim;
//


class Player {
  constructor(x, y, color) {
    this.x = x;
    this.y = y;
    this.color = color;
    this.width = canvas.width / 45;
    this.height = canvas.height / 6;
  }

  draw() {
    draw_rect(this.color, ({ x: this.x, y: this.y }), ({ width: this.width, height: this.height }));
    draw_rect("blue", ({ x: this.x, y: this.y }), ({ width: 10, height: this.height }));
  }

  move(y) {
    print(`oppon-move: ${y}`)
    draw_rect(boardColor, ({ x: this.x, y: this.y }), ({ width: this.width + 2, height: this.height }));
    this.y = y;
    this.draw();

  }
}

function print(msg) {
  console.log(msg);
}



function init_data(data) {
  BALL = data.ball;
  BALL.color = ballColor;

  BALL.draw = function(color = this.color, pos = ({
    x: canvasWidth / 2,
    y: canvasHeight / 2
  }),
    radius = this.radius) {
    draw_circle(color, radius, pos, ({ statrAngle: 0, endAngle: 2 * Math.PI }));
  };

  BALL.move = function(x, y) {
    this.draw(boardColor, ({ x: this.x, y: this.y }), this.radius + 3);   // clean location
    draw_rect(boardCentre, ({ x: canvasWidth / 2 - 10, y: 0 }), ({ width: 20, height: canvasHeight })); // draw net
    [this.x, this.y] = [x, y]; // update position
    this.draw(this.color, ({ x: this.x, y: this.y })); // draw ball 
  };

  player = data.proper;
  player.color = playerColor;
  player.draw = function() {
    print(this.x)
    draw_rect(this.color, ({ x: this.x, y: this.y }), ({ width: this.width, height: this.height }));
    draw_rect("blue", ({ x: this.x, y: this.y }), ({ width: 10, height: this.height }));
  }
  player.move = function(y) {
    draw_rect(boardColor, ({ x: this.x, y: this.y }), ({ width: this.width + 2, height: this.height }));
    this.y = y;
    this.draw();
  }
}

const ws = new WebSocket('ws://127.0.0.1:8000/ws/game/' + roomID + '/');

ws.onopen = (e) => {
  ws.send(JSON.stringify({
    'event': 'init',
    'canvasW': canvasWidth,
    'canvasH': canvasHeight,
    'ballradius': ballradius,
  }));

};

ws.onmessage = function(e) {
  const data = JSON.parse(e.data);
  const bdEvent = data["event"]

  print("EVENT[[ " + bdEvent + " ]")

  // error messages from backend
  if (bdEvent === "error_msg") {
    Swal.fire({
      icon: "error",
      title: data["error"],
    }).then(() => window.location = '/')
  }

  if (bdEvent === "initial") {
    init_data(data);
    player.draw();
    BALL.draw();
  }

  if (bdEvent === "oppon_pos") {
    pos = data.data;
    opponent = new Player(pos.x, pos.y, "yellow");
    opponent.draw()
  }

  if (bdEvent === "move") {
    player.move(data.y);
  }

  if (bdEvent === "oppon_move") {
    print(data.y)
    opponent.move(data.y);
  }

  if (bdEvent === "ball_movement") {
    print(data)
    print(data.moveX)
    // ball.move(ball.x + ball.velocityX, ball.y + ball.velocityY);
    BALL.velocityX = data.velocityX;
    BALL.velocityY = data.velocityY;
    BALL.move(data.moveX, data.moveY);
  }
  // print(e);
  // print("data received --> ", data)
  // Handle incoming message
};

ws.onclose = function(e) {
  // console.err
};

// // Send message to server
// function sendMessage(message) {
//   chatSocket.send(JSON.stringify({
//     'message': message
//   }));
// }


// // init backend
// function init_step() {
//     chatSocket.send(JSON.stringify({
//         'type': 'init',
//         'canvasW
//     }))
// }



/** 
 * Draws a rectangle on the canvas context.
 * @param {string} style - The fill color of the rectangle.
 * @param {object} pos - The poition of the rectangle (pos.x/pos.y).
 * @param {object} dim - The dimensions of the rectangle.
 */
function draw_rect(style, pos, dim) {
  //canvasCtx.beginPath();
  canvasCtx.fillStyle = style;
  canvasCtx.fillRect(pos.x, pos.y, dim.width, dim.height);
  //canvasCtx.closePath();
}

/**
 * Draws the ping-pong board game
 */
function draw_gameBoard() {
  draw_rect(boardColor, ({ x: 0, y: 0 }), ({ width: canvasWidth, height: canvasHeight }));
  // draw_rect("red", ({x: 0, y: 0}), ({width: canvasWidth / 2, height: canvasHeight / 2})); // !DEBUG
  draw_rect(boardCentre, ({ x: canvasWidth / 2 - 10, y: 0 }), ({ width: 20, height: canvasHeight }));
  draw_rect(boardCentre, ({ x: 0, y: canvasHeight / 2 }), ({ width: canvasWidth, height: 2 }));
}


/**
 * Draws a circle.
 */
function draw_circle(style, radius, pos, anglePos) {
  canvasCtx.beginPath();
  canvasCtx.arc(pos.x, pos.y, radius, anglePos.statrAngle, anglePos.endAngle);
  canvasCtx.fillStyle = style;
  canvasCtx.fill();
  canvasCtx.closePath();
}

/**
 * Player
 */
// class Player {
//   constructor(x, y, color) {
//     this.x = x;
//     this.y = y;
//     this.color = color;
//     this.width = canvas.width / 45;
//     this.height = canvas.height / 6;
//   }

//   draw() {
//     draw_rect(this.color, ({ x: this.x, y: this.y }), ({ width: this.width, height: this.height }));
//     draw_rect("blue", ({ x: this.x, y: this.y }), ({ width: 10, height: this.height }));
//   }

//   move(y) {
//     draw_rect(boardColor, ({ x: this.x, y: this.y }), ({ width: this.width + 2, height: this.height }));
//     this.y = y;
//     this.draw();

//   }
// };

draw_gameBoard();

// const pl = new Player(0, 0, 'red');
// pl.draw();


// const op = new Player(canvasWidth - 20, 0, 'yellow');
// op.draw();
// let direc = 1;

// op.update = () => {

//   if (direc === 1) {

//     if (op.y + ((op.height / 6) / 2) + (op.height / 6) < canvasHeight) {


//       op.move(op.y + (op.height / 6));
//     } else {

//       op.move(op.y + (canvasHeight - (op.y + (op.height / 6))));
//       direc = -1;
//     }
//   }
//   else {
//     if (op.y - (op.height / 6) >= 0) {
//       op.move(op.y - (op.height / 6));
//     } else {

//       op.move(op.y - (canvasHeight - (canvasHeight - op.y)));
//       direc = 1;
//     }
//   }
// };
// // create the ball
// const ball = {
//   x: canvasWidth / 2,
//   y: canvasHeight / 2,
//   radius: ballradius,
//   speed: 5,
//   velocityX: 5,
//   velocityY: 5,
//   color: ballColor,

//   draw(color = this.color, pos = ({ x: canvasWidth / 2, y: canvasHeight / 2 }), radius = this.radius) {
//     draw_circle(color, radius, pos, ({ statrAngle: 0, endAngle: 2 * Math.PI }));
//   },

//   move(x, y) {
//     this.draw(boardColor, ({ x: this.x, y: this.y }), this.radius + 3);   // clean location
//     draw_rect(boardCentre, ({ x: canvasWidth / 2 - 10, y: 0 }), ({ width: 20, height: canvasHeight })); // draw net
//     [this.x, this.y] = [x, y]; // update position
//     this.draw(this.color, ({ x: this.x, y: this.y })); // draw ball 
//   },
// };


// rendring
function reset() {
  ball.velocityX *= -1;
  ball.move(canvasWidth / 2, canvasHeight / 2);
  //ball.move(19, 60);
}

// colision detection
function is_collision(player) {
  // console.log("CHECK COLLISION");
  const ballPos = {
    top: ball.y - ballradius,
    bott: ball.y + ballradius,
    left: ball.x - ballradius,
    right: ball.x + ballradius,
  };

  const playerPos = {
    top: player.y,
    bott: player.y + player.height,
    left: player.x,
    right: player.x + player.width,
  };

  // console.log(player.y, playerPos.top);
  return ballPos.right > playerPos.left && ballPos.bott > playerPos.top
    && ballPos.left < playerPos.right && ballPos.top < playerPos.bott;
}

function ballAct() {
  if (ball.y + ball.velocityY > canvasHeight) {
    ball.velocityY *= -1;
  } else if (ball.y + ball.speed < 0) {
    ball.velocityY *= -1;
  }

  if (ball.x + ball.velocityX > canvasWidth) {
    pcnt++;
    pcount.textContent = pcnt;
    reset();
  } else if (ball.x + ball.velocityX < 0) {
    ccnt++;
    cocount.textContent = ccnt;
    reset();
  }


  if (is_collision(pl)) {
    // console.log("IS COLLISION!! ");
    //WHERE THE BALL HIT THE PLAYER
    let collidePoint = ball.y - (pl.y + pl.height / 2);

    //NORMALIZATION
    collidePoint = collidePoint / (pl.height / 2);

    //CALCULATE THE ANGLE IN RADIAN
    let angleRad = collidePoint * Math.PI / 4;

    //X DIRECTION OF THE BALL WHEN IT'S HIT
    let direction = (ball.x < canvas.width / 2) ? 1 : -1;


    //CHANGE VELOCITY OF X AND Y
    ball.velocityX = direction * ball.speed * Math.cos(angleRad);

    ball.velocityY = ball.speed * Math.sin(angleRad);

    //Everytime a ball is hit by a paddle, we increase its speed
    ball.speed += 0.5;
  }

  else if (is_collision(op)) {
    // console.log("IS COLLISION!! ");
    //WHERE THE BALL HIT THE PLAYER
    let collidePoint = ball.y - (op.y + op.height / 2);

    //NORMALIZATION
    collidePoint = collidePoint / (op.height / 2);

    //CALCULATE THE ANGLE IN RADIAN
    let angleRad = collidePoint * Math.PI / 4;

    //X DIRECTION OF THE BALL WHEN IT'S HIT
    let direction = (ball.x < canvas.width / 2) ? 1 : -1;


    //CHANGE VELOCITY OF X AND Y
    ball.velocityX = direction * ball.speed * Math.cos(angleRad);

    ball.velocityY = ball.speed * Math.sin(angleRad);

    //Everytime a ball is hit by a paddle, we increase its speed
    // ball.speed += 0.5;
  }


  // console.log(ball.x, ball.y);
  // ball.y += ball.velocityY;
  // ball.x += ball.velocityX;
  ball.move(ball.x + ball.velocityX, ball.y + ball.velocityY);
  pl.draw();
  op.draw();
  op.update();
  requestAnimationFrame(ballAct);
}

// ballAct();

async function move_send(move) {
  ws.send(JSON.stringify({
    'event': 'player_move',
    'canvasW': canvasWidth,
    'canvasH': canvasHeight,
    'y': move,
  }));
}

// handling keypress
document.addEventListener('keypress', (e) => {
  if (e.key === 's') {
    if (player.y + (player.height / 2) + player.height < canvasHeight) {
      move_send(player.y + player.height);
    } else {
      move_send(player.y + (canvasHeight - (player.y + player.height)));
    }
  } else if (e.key === 'w') {
    if (player.y - player.height >= 0) {
      move_send(player.y - player.height);
    } else {
      move_send(player.y - (canvasHeight - (canvasHeight - player.y)));
    }
  }
});




// const text = document.getElementById("text");

// document.addEventListener(('click'), (e) => {
//     // console.log(text.value);
//     sendMessage(text.value);
// });
