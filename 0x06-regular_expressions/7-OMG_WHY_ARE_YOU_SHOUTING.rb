#!/usr/bin/env ruby
ARGV.each do|a|
    var = a.scan(/[A-Z]/)
    var.each do |i|
        print i
    end
    puts""
end
