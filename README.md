# cardinal-numeral-vietnamese
A module to transform cardinal numeral (integer) to Vietnamese word (string) with North side and South side accentaccent

How to use this?
Just call integer_to_vietnamese_numeral(n, region)
With n agrument is integer and region agrument is option have 2 string options "north" (default) or "south"

Example:  
`integer_to_vietnamese_numeral(256)`
`integer_to_vietnamese_numeral(512, region="south")`
