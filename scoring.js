/*
Shows the final score of a game between two teams and
who wins
*/
let placar = [7, 8];
let golsTimeA = placar[0]
let golsTimeB = placar[1]

if (golsTimeA > golsTimeB) {
  console.log("Team A", golsTimeA, "x", golsTimeB, "Team B")
  console.log("TEAM A WINS");
} else if (golsTimeA < golsTimeB) {
  console.log("Team A", golsTimeA, "x", golsTimeB, "Team B")
  console.log("TEAM B WINS");
} else {
  console.log("Team A", golsTimeA, "x", golsTimeB, "Team B")
  console.log("DRAW")
}