<?php

$response = ""; $sid = 2; $sname = "ABC"; $marks = 20; $pass = 0;

require 'db_connect.php';

// #boolean value = mysqli_connect(ip address, username, password, database)
// $conn = mysqli_connect('localhost', 'root', '', 'demodb');

// if ($conn == false) 
// {
//     echo "Error connecting <br>";  
// }

// else
// {
    echo "Connected to the database <br>";
    $query = "insert into students values ($sid, '$sname', $marks, $pass)";
    $result = mysqli_query($conn, $query);

    if ($result)
    {
        echo "Values inserted";
    }
    else
    {
        echo "Values not inserted";
    }
// }

?>