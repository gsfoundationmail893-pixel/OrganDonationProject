<?php
include 'dbconnect.php';

$sql = "SELECT * FROM Recipients";
$result = mysqli_query($conn,$sql);
?>

<html>

<head>
<title>Recipient Records</title>
<link rel="stylesheet" href="style.css">
</head>

<body>

<h1>Recipient Records</h1>

<table border="1">

<tr>
<th>ID</th>
<th>Recipient Code</th>
<th>Blood Group</th>
<th>Required Organ</th>
<th>Urgency Level</th>
<th>City</th>
</tr>

<?php

while($row=mysqli_fetch_assoc($result))
{
?>

<tr>

<td><?php echo $row['RecipientID']; ?></td>

<td><?php echo $row['RecipientCode']; ?></td>

<td><?php echo $row['BloodGroup']; ?></td>

<td><?php echo $row['RequiredOrgan']; ?></td>

<td><?php echo $row['UrgencyLevel']; ?></td>

<td><?php echo $row['City']; ?></td>

</tr>

<?php
}
?>

</table>

</body>
</html>
