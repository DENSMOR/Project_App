<?
require_once "../connect.php";

$id=$_POST["id"];
$Price=$_POST["Price"];
$Adres=$_POST["Adres"];
$info=$_POST["info"];

mysqli_query($conn, "INSERT INTO `deals_history` VALUES ('$Price')");
header("Location: /index.php");
exit;