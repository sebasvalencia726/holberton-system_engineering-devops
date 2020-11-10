#!/usr/bin/env ruby
ARGV.each do|a|
    var = a.scan(/hbt{1,4}n/)
    var.each do |i|
        print i
    end
    puts""
end
