<?php

$n = 125;
$i = rand(1, $n);
// $p = "/src/img/sukasuka/$i.jpg";
$p = "https://raw.githubusercontent.com/hyc1230/Chtholly-img/main/$i.jpg";

die(header('Location:' . $p));

?>