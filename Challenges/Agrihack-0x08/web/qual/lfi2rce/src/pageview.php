<?php
error_reporting(0);
// echo "lfi2rce";
if (isset($_GET['page'])) {
    $page = $_GET['page'];
    include $page;
}
?>