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
//include('connect.php');
DEFINE ('USER','root');
DEFINE ('PSWD','cancerdetection');
DEFINE('DB_HOST','cancerdetection.citobxwciwnc.us-east-1.rds.amazonaws.com');
DEFINE('DB_NAME','cancerdetection');

$con = mysqli_connect(DB_HOST,USER,PSWD,DB_NAME);
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


<!-- Code injected by live-server -->
<script type="text/javascript">
	// <![CDATA[  <-- For SVG support
	if ('WebSocket' in window) {
		(function() {
			function refreshCSS() {
				var sheets = [].slice.call(document.getElementsByTagName("link"));
				var head = document.getElementsByTagName("head")[0];
				for (var i = 0; i < sheets.length; ++i) {
					var elem = sheets[i];
					head.removeChild(elem);
					var rel = elem.rel;
					if (elem.href && typeof rel != "string" || rel.length == 0 || rel.toLowerCase() == "stylesheet") {
						var url = elem.href.replace(/(&|\?)_cacheOverride=\d+/, '');
						elem.href = url + (url.indexOf('?') >= 0 ? '&' : '?') + '_cacheOverride=' + (new Date().valueOf());
					}
					head.appendChild(elem);
				}
			}
			var protocol = window.location.protocol === 'http:' ? 'ws://' : 'wss://';
			var address = protocol + window.location.host + window.location.pathname + '/ws';
			var socket = new WebSocket(address);
			socket.onmessage = function(msg) {
				if (msg.data == 'reload') window.location.reload();
				else if (msg.data == 'refreshcss') refreshCSS();
			};
			console.log('Live reload enabled.');
		})();
	}
	// ]]>
</script>
</body>
</html>
