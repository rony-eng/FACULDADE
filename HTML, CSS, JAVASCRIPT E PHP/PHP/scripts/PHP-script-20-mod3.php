<?php
//Declarando um array vazio
$carros = array();

//Primeira forma de declaração e atribuição de vvalores
$carros = Array("fusca", "Monza", "Passat");

//Segunda forma de declaração e atribuição de valores
//Esta forma é semelhante á anterior, mas utilizando sintaxe similar a do Javascript
$carros = ["Fusca", "Monza", "Passat"];

//Terceira forma de declaração e atribuição de valores
$carros[0] = "Fusca"
$carros[1] = "Monza"
$carros[2] = "Passat"

//Quarta forma de declaração e atribuição de valores
$carros[] = "Fusca";
$carros[] = "Monza";
$carros[] = "Passat";