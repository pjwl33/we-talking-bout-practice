# Question 2: Look and Say
# Implement a function that outputs the Look and Say sequence:
# 1
# 11
# 21
# 1211
# 111221
# 312211
# 13112221
# 1113213211
# 31131211131221
# 13211311123113112211
# Solution
# This problem is fairly straightforward and should not take a long time to solve. However, be sure you do proper error checking of the input first! (Empty and invalid inputs should be taken into account). Additionally, you can ask yourself:
# How does the output length scale?
# What is the max single digit that can exist in the output?
# What is the only starting sequence that never grows in length?
# Sample Solution in PHP
# <?php
# print_look_and_say_seq(100);
#
# function print_look_and_say_seq($count = 0) {
#   $val = 1;
#   for ($i = 1; $i <= $count; $i++) {
#    echo "$val\n";
#    $val = output_val($val);
#   }
# }
#
# function output_val($input) {
#   $input = "$input"; // Normalize from int to string
#   if (strlen($input) == 1) {
#    return "1$input";
#   }
#
#   $ret = '';
#   $cur = $input[0];
#   $count = 1;
#   for ($i = 1; $i <= strlen($input); $i++) {
#    if ($cur != $input[$i] || $i == strlen($input)) {
#     $ret .= "$count$cur";
#     $count = 1;
#     $cur = $input[$i];
#    } else {
#     $count++;
#    }
#   }
#   return $ret;
# }
def nextLookAndSay(n):
    res = []
    count = 1
    # Iterate through the str to build next sequence
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            res.append(str(count) + s[i - 1])
            count = 1

    # Append last counted seuqnece`
    res.append(str(count) + s[i - 1])

    return ''.join(res)

def lookAndSay(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    res = "1" # base case is string 1

    for i in range(1, n):
        res = nextLookAndSay(res)

    return res
