# cardinal-numeral-vietnamese
A module to transform cardinal numeral (integer) to Vietnamese word (string) with North side and South side accent

How to use this?
Just call integer_to_vietnamese_numeral(n, region)
With n agrument is integer and region agrument is option have 2 string options "north" (default) or "south"

Example:  
`integer_to_vietnamese_numeral(2005)`
`Hai nghìn linh năm`

`integer_to_vietnamese_numeral(2008, region="south")`
`Hai ngàn lẻ tám`
