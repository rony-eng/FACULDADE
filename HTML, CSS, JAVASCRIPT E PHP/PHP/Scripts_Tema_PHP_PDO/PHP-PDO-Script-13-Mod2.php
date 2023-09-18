<?php
 
//...
 
//Realizando uma consulta no BD através do login e senha recebidos por POST
$login = $_POST['login'];
$pswd = $_POST['pswd'];
 
$instrucaoSQL = "Select * 
                From Usuario 
                Where 
                login = '' OR true = true;/* 
                And password = '*/--'";
 
//...
