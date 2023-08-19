var a = 10;
var b = 3;

console.log ("if com uma única condição:");
if (a > b){
    console.log("a é maior que b");
}
if (a == b){
   console.log("a é igual a b"); 
}
if (a < b){
    console.log("a é menor que b");
}
if (b < a){
	console.log("b é menor que a");
}

var c = 5;
var d = -1;

console.log("if com duas condições, onde ambas precisam ser verdadeiras:");
if (c > d && d > 0){
    console.log("c é maior que d E d é um número positivo");
}
if (c > d && d <= 0){
    console.log("c é maior que d E d não é um número positivo");
}
console.log("if com duas condições, onde pelo menos uma precisa ser verdadeira:");  
if (c < d || d > 0){
    console.log("c é menor que d OU d é um número positivo");
}
if (c < d || d <= 0){
    console.log("c é menor que d OU d não é um número positivo");
}

// UM MODO DIFERENTE DO EXERCICO ACIMA DAS VARIAVEIS A E B
var a = 10;
var b = 3;

console.log ("if com uma única condição:");
if (a > b){
   console.log("a é maior que b");
} else if (a == b){
   console.log("a é igual a b"); 
} else if (a < b){
   console.log("a é menor que b");
} else if (b < a){
   console.log("b é menor que a");
}