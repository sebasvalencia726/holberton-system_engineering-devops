#!/usr/bin/env ruby
ARGV.each do|a|
    var = a.scan(/(?<=from:)[A-Z|a-z|0-9|\+]+|(?<=to:)\+[0-9]+|(?<=flags:).{12}/)
    print var.join(',')
    puts""
end
