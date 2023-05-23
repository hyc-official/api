<?php

$n = 125;
$i = rand(1, $n);
$p = "/src/img/sukasuka/$i.jpg";

die(header('Location:' . $p));

?>