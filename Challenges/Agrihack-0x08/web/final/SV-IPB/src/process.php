<?php
error_reporting(0);
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
$dom = new DOMDocument();
$dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
$info = simplexml_import_dom($dom);
$username = $info->username;
$password = $info->password;

echo "Sorry, $username couldn't be registered!";
?>
