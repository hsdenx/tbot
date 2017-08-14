<?php
require_once ('konfiguration.php');
$db_link = mysqli_connect (
                     MYSQL_HOST, 
                     MYSQL_BENUTZER, 
                     MYSQL_KENNWORT, 
                     MYSQL_DATENBANK
                    );
if ( $db_link )
{
    // print_r( $db_link);
}
else
{
    die('no Connection: ' . mysqli_error());
}
mysqli_select_db($db_link, "database");

$sql = "SELECT * FROM tbot_results ORDER BY tbot_id DESC";
 
$db_erg = mysqli_query( $db_link, $sql );
if ( ! $db_erg )
{
  die('invalid query: ' . mysqli_error());
}

# get number of rows
$num = mysqli_num_rows($db_erg);

#echo '
#<head>
#<link rel="stylesheet" type="text/css" href="mystyle.css">
#</head>
#';

echo '
<!DOCTYPE html>
<html>
<head>
<title>TBot U-Boot testresults</title>
<style>
body {
    background-color: linen;
}

h1 {
    color: maroon;
    margin-left: 40px;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    padding: 8px;
    text-align: left;
    border: 1px solid #ddd;
    font-family:arial, "lucida console", sans-serif; /* Schriftart */
}

tr:hover {background-color: #f5f5f5}
</style>
</head>
<meta http-equiv="refresh" content="10" >
<body>
';

echo '<table border="1">';
echo "<tr bgcolor= #e67e22>";
  echo "<td> ID </td>";
  echo "<td> Date </td>";
  echo "<td> Toolchain </td>";
  echo "<td> Version </td>";
  echo "<td> defconfig </td>";
  echo "<td> Testcase name </td>";
  echo "<td> Statistic </td>";
  echo "<td> dot graph </td>";
  echo "<td> nice log </td>";
  echo "<td> test/py result </td>";
  echo "<td> Logfile </td>";
  echo "</tr>\n";
$count = 0;
while (($zeile = mysqli_fetch_array( $db_erg, MYSQL_ASSOC)) && ($count < 6))
{
  if ($zeile['success'] == 0) {
    echo "<tr bgcolor=#FA8072>";
  } else {
    echo "<tr bgcolor= #58d68d>";
  }
  echo "<td id=". $zeile['tbot_id'] ." >". $zeile['tbot_id'] ."</td>";
  echo "<td>". $zeile['test_date'] . "</td>";
  echo "<td>". $zeile['toolchain'] . "</td>";
  echo "<td>". $zeile['binaryversion'] . "</td>";
  if (file_exists("tbot/id_". $zeile['tbot_id'] ."/.config")) {
    echo "<td> <a href='tbot/id_". $zeile['tbot_id'] ."/.config'> ". $zeile['defname'] . " </a>  </td>";
  } else {
    echo "<td>". $zeile['defname'] . "</td>";
  }
  echo "<td> <a href='https://github.com/hsdenx/tbot/tree/master/src/tc/board/". $zeile['testcase'] ."' target='_blank'> ". $zeile['testcase'] ." </a> </td>";
  echo "<td> <a href='tbot/id_". $zeile['tbot_id'] ."/statistic.jpg'> statistic </a> </td>";
  echo "<td> <a href='tbot/id_". $zeile['tbot_id'] ."/graph.png'> tc graph </a> </td>";
  if (file_exists("tbot/id_". $zeile['tbot_id'] ."/html_log.html")) {
    echo "<td> <a href='tbot/id_". $zeile['tbot_id'] ."/html_log.html'> nice log </a> </td>";
  } else {
    echo "<td> none </a> </td>";
  }

  if (file_exists("tbot/id_". $zeile['tbot_id'] ."/test-log.html")) {
    echo "<td> <a href='tbot/id_". $zeile['tbot_id'] ."/test-log.html'> test py result </a> </td>";
  } else {
    echo "<td> none </a> </td>";
  }
  echo "<td> <a href='tbot/id_". $zeile['tbot_id'] ."/tbot.log'> rawlog </a> </td>";
  echo "</tr>\n";
  $count = $count + 1;
}
echo "</table>";
 
echo'
</body>
</html>
';

mysqli_free_result( $db_erg );
?>
