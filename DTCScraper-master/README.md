# DTCScrapper

## Features

This class is used to fetch the quotes of the French quote website danstonchat.com. It's the French equivalent of bash.org.

## Installing

Just copy the class in your folder, then call it with `from DTCScrapper import DTCScrapper`

## Using

You can us it like any python class.
I recommend using the main() function, it returns a list with alternatively the user name and the text.

## Example

> As found in example.py

```
from DTCScrapper import DTCScrapper
import sys

# Get the quote number from the arguments
user_limit = sys.argv[1]

# Initiate the class
e = DTCScrapper()

# Create the url
url_dtc = "http://danstonchat.com/"+str(user_limit)+".html"

# Get the results
result_from_scrapper =  e.main(url_dtc)

final_quote = ""

iter = 0

for a in result_from_scrapper:
    if iter % 2 == 0 :
        final_quote += a
    else:
        final_quote += a + "\n"
    iter += 1

print final_quote
```

## License

DTCScrapper - A Python class to scrap danstonchat.com
Copyright (C) 2015  N07070

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
