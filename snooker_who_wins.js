/*
Calculates who wins a game of snooker, between 2 players
using the value of balls dropped by one of them
*/
let jogadorA = [11,8,12,14,15];

let totalJogadorA = 0;

for (const bola of jogadorA) {
  totalJogadorA += bola;
}

let totalJogadorB = 120 - totalJogadorA;


if (totalJogadorA > totalJogadorB) {
  console.log("JOGADOR A GANHOU")
} else if (totalJogadorA < totalJogadorB) {
  console.log("JOGADOR B GANHOU")
} else {
  console.log("EMPATE")
}