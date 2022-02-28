# Regex to check for beta versions explained
-----------------------------------------------------

    ^(?:0|(?:0|[1-9][0-9]*)\.[0-9]*[13579])(?:\.[0-9]+)*$

Options: Case insensitive; Exact spacing; Dot doesn’t match line breaks; ^$ match at line breaks; Regex syntax only

* Assert position at the beginning of a line (at beginning of the string or after a line break character) (line feed) `^`
* Match the regular expression below `(?:0|(?:0|[1-9][0-9]*)\.[0-9]*[13579])`
    * Match this alternative (attempting the next alternative only if this one fails) `0`
        * Match the character “0” literally `0`
    * Or match this alternative (the entire group fails if this one fails to match) `(?:0|[1-9][0-9]*)\.[0-9]*[13579]`
        * Match the regular expression below `(?:0|[1-9][0-9]*)`
            * Match this alternative (attempting the next alternative only if this one fails) `0`
                * Match the character “0” literally `0`
            * Or match this alternative (the entire group fails if this one fails to match) `[1-9][0-9]*`
                * Match a single character in the range between “1” and “9” `[1-9]`
                * Match a single character in the range between “0” and “9” `[0-9]*`
                    * Between zero and unlimited times, as many times as possible, giving back as needed (greedy) `*`
        * Match the character “.” literally `\.`
        * Match a single character in the range between “0” and “9” `[0-9]*`
            * Between zero and unlimited times, as many times as possible, giving back as needed (greedy) `*`
        * Match a single character from the list “13579” `[13579]`
* Match the regular expression below `(?:\.[0-9]+)*`
    * Between zero and unlimited times, as many times as possible, giving back as needed (greedy) `*`
    * Match the character “.” literally `\.`
    * Match a single character in the range between “0” and “9” `[0-9]+`
        * Between one and unlimited times, as many times as possible, giving back as needed (greedy) `+`
* Assert position at the end of a line (at the end of the string or before a line break character) (line feed) `$`

Created with [RegexBuddy](https://www.regexbuddy.com/)

