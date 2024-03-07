<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $targetDirectory = "files/"; // Direktori tempat file akan diunggah
    $targetFile = $targetDirectory . basename($_FILES["file"]["name"]);
    $fileType = pathinfo($targetFile, PATHINFO_EXTENSION);

    // Izinkan hanya file teks (.txt)
    if ($fileType == "txt") {
        if (move_uploaded_file($_FILES["file"]["tmp_name"], $targetFile)) {
            echo '<div class="alert alert-success" role="alert">';
            echo 'File berhasil diunggah:<br>';
            echo '<strong>Nama file:</strong> ' . $_FILES["file"]["name"] . '<br>';
            echo '<strong>Lokasi file:</strong> ' . $targetFile;
            echo '</div>';
        } else {
            echo '<div class="alert alert-danger" role="alert">Maaf, terjadi kesalahan saat mengunggah file.</div>';
        }
    } else {
        echo '<div class="alert alert-warning" role="alert">Hanya file dengan ekstensi .txt yang diizinkan.</div>';
    }
}
?>
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Upload File</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
  </head>
  <body>
    <div class="p-5 mb-4 bg-light rounded-3">
        <div class="container-fluid py-5">
          <h1 class="display-5 fw-bold">Upload File</h1>
          <p class="col-md-8 fs-4">File upload is a process that allows users to transfer files from their local device to a remote server or system. In web development, it is commonly used to enable users to share documents, images, or other types of files with a website or application. 
            
          <br><br>Upload your txt file

        <form action="pageview.php?page=upload.php" method="post" enctype="multipart/form-data">
            <div class="form-group">
                <!-- <label for="file">Pilih file .txt:</label> -->
                <input type="file" class="form-control-file" id="file" name="file">
                <button type="submit" class="btn btn-primary">Unggah</button>
            </div>
        </form>

</p>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
  </body>
</html>
