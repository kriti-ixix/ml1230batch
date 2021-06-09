<?php

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
    $query = "select * from students";
    $result = $conn->query($query);

    if ($result -> num_rows > 0)
    {
        echo "Found some rows";
    }
    else
    {
        echo "Found nothing";
    }
// }

?>