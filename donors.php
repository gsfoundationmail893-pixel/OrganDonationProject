<?php
include 'dbconnect.php';

$sql = "SELECT * FROM Donors";
$result = mysqli_query($conn,$sql);
?>

<html>
<body>
<h1>Donor Records</h1>

<table border="1">

<tr>
<th>DonorID</th>
<th>DonorCode</th>
<th>BloodGroup</th>
<th>OrganType</th>
<th>City</th>
</tr>

<?php
while($row=mysqli_fetch_assoc($result))
{
?>

<tr>
<td><?php echo $row['DonorID']; ?></td>
<td><?php echo $row['DonorCode']; ?></td>
<td><?php echo $row['BloodGroup']; ?></td>
<td><?php echo $row['OrganType']; ?></td>
<td><?php echo $row['City']; ?></td>
</tr>

<?php
}
?>

</table>

</body>
</html>