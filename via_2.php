<html>
<head>
<title>Abrir vía 2</title>
</head>
<body>
<?php
  $ar=fopen("./php_files/test.txt","w") or
    die("Problemas en la creacion");
  fputs($ar,"2");
  fclose($ar);
  echo "Los datos se cargaron correctamente.";
  ?>
</body>
</html>
