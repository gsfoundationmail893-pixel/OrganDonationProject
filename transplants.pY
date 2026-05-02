<?php
include 'dbconnect.php';

$sql = "SELECT * FROM Transplants";
$result = mysqli_query($conn,$sql);
?>

<html>

<head>
<title>Transplant Status</title>
<link rel="stylesheet" href="style.css">
</head>

<body>

<h1>Transplant Status</h1>

<table border="1">

<tr>
<th>Transplant ID</th>
<th>Donor ID</th>
<th>Recipient ID</th>
<th>Hospital ID</th>
<th>Status</th>
</tr>

<?php

while($row=mysqli_fetch_assoc($result))
{
?>

<tr>

<td><?php echo $row['TransplantID']; ?></td>

<td><?php echo $row['DonorID']; ?></td>

<td><?php echo $row['RecipientID']; ?></td>

<td><?php echo $row['HospitalID']; ?></td>

<td><?php echo $row['Status']; ?></td>

</tr>

<?php
}
?>

</table>

</body>
</html>
