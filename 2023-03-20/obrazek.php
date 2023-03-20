<?php

// dokumentacja GD: https://www.php.net/manual/en/ref.image.php

$im = imagecreatetruecolor(400, 400);

header("Content-Type: image/png");

$yellow = imagecolorallocate($im, 255, 255, 0);
$orange = imagecolorallocate($im, 255, 128, 0);

imagefilledellipse($im, 200, 200, 270, 270, $orange);
imageellipse($im, 200, 200, 270, 270, $yellow);


imagepng($im);

