#!/usr/bin/env ruby
ARGV.each do|a|
    var = a.scan(/^\d{10}+$/)
    var.each do |i|
        print i
    end
    puts""
end
