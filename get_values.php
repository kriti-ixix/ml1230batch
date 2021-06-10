<?php

$sid = array();
$sname = array(); 
$marks = array(); 
$pass = array();

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
    //$result = mysqli_query($conn, $query);

    if ($result -> num_rows > 0)
    {
        while ($arr = mysqli_fetch_array($result))
        {
            array_push($sid, $arr['sid']);
            array_push($sname, $arr['sname']);
            array_push($marks, $arr['marks']);
            array_push($pass, $arr['pass']);
        }
        // $sname = $arr['sname'];
        // $marks =  $arr['marks'];
        // $pass = $arr['pass'];
    }
    else
    {
        echo "Found nothing";
    }

    echo json_encode(array('sid' => $sid, 'sname' => $sname, 'marks' => $marks, 'pass' => $pass));

// }

?>
