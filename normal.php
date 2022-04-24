<html>
<head>
<title>Volver al ciclo normal</title>
</head>
<body>
<?php
  $ar=fopen("./php_files/test.txt","w") or
    die("Problemas en la creacion");
  fputs($ar,"0");
  fclose($ar);
  echo "Los datos se cargaron correctamente.";
  ?>
</body>
</html>
