#!/usr/bin/env ruby
ARGV.each do|a|
    var = a.scan(/hbt{2,5}n/)
    var.each do |i|
        print i
    end
    puts""
end
