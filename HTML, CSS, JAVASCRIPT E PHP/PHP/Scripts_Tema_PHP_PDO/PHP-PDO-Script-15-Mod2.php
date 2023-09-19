<?php
 
//...
 
$stmt = $dsn->prepare("Select * From Usuario Where login = ? And password = ?");
$stmt->execute([$login, $pswd]);
 
//...
