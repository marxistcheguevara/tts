<html>

<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/> 
<meta http-equiv="Content-Language" content="az">
<?php

$url = "http://".$_SERVER['SERVER_NAME'].$_SERVER['REQUEST_URI'];


echo $url;

?>
</head>

<body>
<?php
$deyisilmeli = array("А", "а", "Б", "б", "Ҹ", "ҹ", "Ч", "ч", "Д", "д", "Е", "е", "Ә", "ә", "Ф", "ф", "Ҝ", "ҝ", "Ғ", "ғ", "Һ", "һ", "Х", "х", "Ы", "ы", "И", "и", "Ж", "ж", "К", "к", "Г", "г", "Л", "л", "М", "м", "Н", "н", "О", "о", "Ө", "ө", "П", "п", "Р", "р", "С", "с", "Ш", "ш", "Т", "т", "У", "у", "Ү", "ү", "В", "в", "Ј", "ј", "З", "з");
$bunaDeyisilsin = array("A", "a", "B", "b",  "C", "c", "Ç", "ç", "D", "d", "E", "e", "Ə", "ə", "F", "f", "G", "g", "Ğ", "ğ", "H", "h", "X", "x", "I", "ı", "İ", "i", "J", "j", "K", "k", "Q", "q", "L", "l", "M", "m", "N", "n", "O", "o", "Ö", "ö", "P", "p", "R", "r", "S", "s", "Ş", "ş", "T", "t", "U", "u", "Ü", "ü", "V", "v", "Y", "y", "Z", "z");

$yazi = $_POST["metn"];
?>

<p align="center"> daxil olunan mətn, latın qrafikasında: <br/>
<textarea rows="15" cols="60" >

<?php
print str_replace($deyisilmeli, $bunaDeyisilsin, $yazi);
?>
</textarea>


<a href="kiril_metn.html">təzə mətn daxil et</a>
</body>
</html>
