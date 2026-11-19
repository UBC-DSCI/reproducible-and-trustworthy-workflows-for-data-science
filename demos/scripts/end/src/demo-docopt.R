# author: Tiffany Timbers
# date: 2024-11-29

"This script prints out docopt args and the type of object they are stored as.
Usage: demo-docopt.R <arg1> <arg2> <arg3>
Options:
<arg1>  Takes any value 
<arg2>  Takes any value
<arg3>  Takes any value 
" -> doc

library(docopt)

opt <- docopt(doc)

print(opt)
print(typeof(opt))
