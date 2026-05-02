<?php
include 'dbconnect.php';

$sql = "SELECT * FROM Hospitals";
$result = mysqli_query($conn,$sql);
?>

<html>

<head>
<title>Hospital Records</title>
<link rel="stylesheet" href="style.css">
</head>

<body>

<h1>Hospital Records</h1>

<table border="1">

<tr>
<th>Hospital ID</th>
<th>Hospital Name</th>
<th>Location</th>
<th>Transplant Type</th>
</tr>

<?php

while($row=mysqli_fetch_assoc($result))
{
?>

<tr>

<td><?php echo $row['HospitalID']; ?></td>

<td><?php echo $row['HospitalName']; ?></td>

<td><?php echo $row['Location']; ?></td>

<td><?php echo $row['TransplantType']; ?></td>

</tr>

<?php
}
?>

</table>

</body>
</html>
