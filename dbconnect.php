<?php
$conn = mysqli_connect("127.0.0.1","root","JAYASHREE@12345678","OrganDonationDB",3306);

if(!$conn){
    die("Connection Failed: " . mysqli_connect_error());
}
?>