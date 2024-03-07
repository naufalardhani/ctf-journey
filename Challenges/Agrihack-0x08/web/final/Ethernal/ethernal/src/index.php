<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="style.css">
    <title>Cek Service Host</title>
</head>
<body>
    <div class="container mt-5">
        <h2 class="mb-4">Service Check</h2>


        <form method="post">
            <div class="form-group">
                <label for="host">Hostname atau IP Address:</label>
                <input type="text" class="form-control" id="host" name="host" required>
            </div>
            <button type="submit" name="submit" class="btn btn-primary">Cek Service</button>
        </form>
        
        <div class="mt-4">
        <?php
        $blacklist = ["10.10", "10.10.0.5", "127.0.0.1", "127.0"];
        $issafe = 1;

        if (isset($_POST['submit'])) {
            $host = $_POST['host'];
            foreach ($blacklist as $word) {
                if (stripos($host, $word) !== false) {
                    echo "no no no...";
                    $issafe = 0;
                    $result = "invalid";
                    break;
                } else {
                    $result = checkService($host);
                }
            }
            echo '<div class="alert ' . ($result ? 'alert-success' : 'alert-danger') . '">';
            echo htmlspecialchars($result);
            echo '</div>';
        }
        ?>

        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.0.7/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

<?php
function checkService($host)
{
    $ch = curl_init($host);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $result = curl_exec($ch);
    $statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    return $result;
}
?>
