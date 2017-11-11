<html>
<head>
  <title>Database Search</title>
  <style type = "text/css">

  table {
    background-color: #FCF
  }

  th {
    width: 150px;
    text-align: left;
  }
  </style>

</head>
<body>
<h1>Database Search</h1>
<form method = "post" action ="search1.php">
<input type ="hidden" name ="submitted" value ="true"/>
<label>Search Category:
<select name = "category">
    <option value = "cancer_id">ID</option>
    <option value = "Gene">Gene</option>
    <option value = "Variation">Variation</option>
    <option value = "Class">Class</option>

</select>

<label>Search Criteria: <input type = "text" name = "criteria" /></label>
<input type ="submit"/>


</form>

<?php
if (isset($_POST['submitted'])){
// connect to the database
include('connect.php');
$category = $_POST['category'];
$criteria = $_POST['criteria'];
$query = "SELECT cancer_id,Gene,Variation,Class FROM cancer WHERE $category = '$criteria'";
$result = mysqli_query($con,$query) or die('error getting data');

echo "<table>";
echo "<tr> <th>ID</th> <th>Gene</th> <th>Variation</th> <th style ='text-align:right'>Class</th> </tr>";

while($row = mysqli_fetch_array($result, MYSQLI_ASSOC)){
  echo"<tr><td>";
  echo $row['cancer_id'];
  echo "</td><td>";
  echo $row['Gene'];
  echo "</td><td>";
  echo $row['Variation'];
  echo "</td><td style ='text-align:right'>";
  echo $row['Class'];
  echo "</td></tr>";
}


echo"</table>";
}//


?>


</body>
</html>
