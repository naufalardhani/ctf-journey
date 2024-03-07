<?php require 'flag.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Cookie</title>
</head>
<body>
    <?php
    if ($_COOKIE['admin'] == 'isTrue') {
        echo "<h1 class='text-center'>$flag</h1>";
    } else {
        echo "Welcome to user page!";
    }
    ?>
</body>
</html>