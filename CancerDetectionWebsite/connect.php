<?php
DEFINE ('USER','root');
DEFINE ('PSWD','cancerdetection');
DEFINE('DB_HOST','cancerdetection.citobxwciwnc.us-east-1.rds.amazonaws.com');
DEFINE('DB_NAME','cancerdetection');

$con = mysqli_connect(DB_HOST,USER,PSWD,DB_NAME);
 ?>
