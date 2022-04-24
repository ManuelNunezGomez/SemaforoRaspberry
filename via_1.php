<html>
<head>
<title>Abrir vía 1</title>
</head>
<body>
<?php
  $ar=fopen("./php_files/test.txt","w") or
    die("Problemas en la creacion");
  fputs($ar,"1");
  fclose($ar);
  echo "Los datos se cargaron correctamente.";
  ?>
</body>
</html>
