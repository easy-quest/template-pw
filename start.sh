#!/usr/bin/env fish

set text (uname --operating-system), (date);git add -A .;git commit -am "$text";git push $argv;
# set text (uname --operating-system), (date);echo $text