<?php
$host = "127.0.0.1";
$username = "sqli";
$password = "sqli";
$database = "sqli";

$conn = mysqli_connect($host, $username, $password, $database);

$input = $_POST["user"];
$pass = $_POST["pass"];


if (!empty($input) && !empty($input)) {
    $sql = "SELECT * FROM users WHERE user='".filter_var($input, FILTER_SANITIZE_STRING)."' AND pass='".$pass."'";
    //echo $sql;
    $result = $conn - > query($sql);
    print_r($result);
    $results = mysqli_fetch_all($result, MYSQLI_ASSOC);#
    echo count($results);
    print_r($results);
    if (count($results) == 1) {#
        die("gg ;) try to get the flag!");
        echo "<script>";
        echo "alert('Bypassed! Try to get the flag!')";
        echo "</script>";
    }
    $conn - > close();
}

?>

<html>

<head>
<link rel="stylesheet" href="cool.css">
</head>

<body>

<div class="log-form">
  <h2>Login to your account</h2>
  <form method="POST">
    <input type="text" title="username" placeholder="username" name="user" />
    <input type="password" title="username" placeholder="password" name="pass"/>
    <button type="submit" class="btn">Login</button>
  </form>
</div><!--end log form -->

</body>

</html>
