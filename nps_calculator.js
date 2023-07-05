/*Calculating NPS (Net Promoter Score) based on answers of
clients, in which 0-6 score means the client is a detractor,
9-10, a promoter, and 7-8, neutral.
*/

let respostas = [6, 6, 7, 9, 10, 5, 9, 9]
let promotores = 0;
let detratores = 0;
let totalDeClientes = respostas.length;

for (const resposta of respostas) {
  if (resposta >= 9 && resposta <= 10) {
    promotores += 1;
  }
  else if (resposta <= 6 && resposta >= 0) {
    detratores += 1;
  }
}

let nps = (promotores - detratores) / totalDeClientes * 100

console.log("-----------------------------------")
console.log("NPS (Net Promoter Score) Calculator")
console.log("The NPS is:", nps)
console.log("-----------------------------------")