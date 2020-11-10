#!/usr/bin/env ruby
ARGV.each do|a|
    var = a.scan(/(?:from:)[A-Z|a-z|0-9|\+]+|(?:to:)\+[0-9]+|(?:flags:).{12}/)
    var.each do |i|
        print i+','
    end
    puts""
end
