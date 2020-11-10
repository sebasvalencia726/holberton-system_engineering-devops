#!/usr/bin/env ruby
ARGV.each do|a|
    var = a.scan(/hbt+n/)
    var.each do |i|
        print i
    end
    puts""
end
