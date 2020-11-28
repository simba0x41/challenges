<?php

function xor_encrypt($in) {
    #$key = 'abcgggggggggggggggggggggggggggggg';
    $key = "showpasswordbgcolor";
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$in = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSFAsuRkQMaAw");
#echo xor_encrypt($in);

#echo "{\"showpassword\":\"yes\",\"bgcolor\":\"#c3d734\"}" |base64

$js = '{"showpassword":"yes","bgcolor":"#c3d734"}';

var_dump(json_decode($js,true));

?>
