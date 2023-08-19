// Estrutura de Decisão

// IF
// if (condição) instrução.
// Nessa forma, é verificada uma única condição. Caso seja verdadeira, a instrução será executada. 
// Do contrário, não. Antes de continuarmos, é importante destacar os elementos da instrução:


// Nesse segundo caso, além de mais de uma instrução, também temos mais de uma condição. 
// Quando é necessário verificar mais de uma condição, em que cada uma delas precisará ser verdadeira, utilizamos os caracteres “&&”.
if (condição1 && condição2){
    instrução1;
    instrução2;
}


// Repare que, nesse código, os caracteres “&&” foram substituídos por “||”. 
// Esses últimos são utilizados quando uma ou outra condição precisa ser verdadeira para que as instruções condicionais sejam executadas.
if (condição1 || condição2){
    instrução1;
    instrução2;    
}


// Execute as instruções 1 e 2 SE ambas forem verdadeiras OU se a condição 3 for verdadeira.
if ( (condição1 && condição2) || condição3){
    instrução1;
    instrução2;
}


// O sinal “!” é utilizado para negar a condição. As instruções 1 e 2 serão executadas caso a condição 1 não seja verdadeira.
if (!condição1){
    instrução1;
    instrução2;
}


// ELSE
// A instrução "else” acompanha a instrução "if". Embora não seja obrigatória, como vimos nos exemplos, sempre que a primeira for utilizada, 
// deve vir acompanhada da segunda. O "else" indica se alguma instrução deve ser executada caso a verificação feita com o "if" não seja atendida. Vejamos:

if(número fornecido é inteiro e positivo){

    Guarde o número em uma variável;

}else{

    Avise ao usuário que o número não é válido;

    Solicite ao usuário que insira novamente um número;

}

// ELSE IF

if (numero1 < 0){
    instrução1;
}else if(numero == 0){
    instrução2;
}else{
    instrução3;
}


// SWITCH
// A instrução "switch" é bastante útil quando uma série de condições precisa ser verificada. É bastante similar à "else if". Vejamos:

switch(numero1){

    case 0:
            instrução1;
            break;
    case 1:
            instrução2;
            break;
    default:
            instrução3;
            break;
}

// OPERADOR TERNÁRIO
if (time < 10){
    greeting = "Good morning";
} else if(time < 20){
    greeting = "Good day";
} else{
    greeting = "Good evening";
}
// COM O OPERADOR TERNÁRIO FICARIA ASSIM:
greeting = (time<10) ? "Good morning" :
            (time<20) ? "Good day" :
            "Good evening"