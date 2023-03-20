<?php

$im = imagecreatetruecolor(400, 400);

header("Content-Type: image/png");

$r = rand() % 256;
$g = rand() % 256;
$b = rand() % 256;

$xxx = imagecolorallocate($im, $r, $g, $b);
$orange = imagecolorallocate($im, 255, 128, 0);

imagefilledellipse($im, 200, 200, 270, 270, $xxx);
imageellipse($im, 200, 200, 270, 270, $orange);

imagepng($im);


