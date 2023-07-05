/*
Algorithm inside a game that calculates how much damage
from monster encounters a player takes each turn, before 
losing the game. The monsters are classified into classes
ranging from class 1 to class 4, and the damage taken
grows accordingly
*/

let vida;
let classe;

while (vida < 0) {
  if (classe === 1) {vida -= 20;}
  else if (classe === 2) {vida -= 30;}
  else if (classe === 3) {vida -= 40;}
  else if (classe === 4) {vida -= 50;}
  console.log(vida);
}
console.log("YOU LOST")
