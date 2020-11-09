#!/usr/bin/env ruby
ARGV.each do|a|
    var = a.scan(/Holberton/)
    var.each do |i|
        print i
    end
    puts""
end
