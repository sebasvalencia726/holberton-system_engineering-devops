#!/usr/bin/env ruby
ARGV.each do|a|
    var = a.scan(/h.n/)
    var.each do |i|
        print i
    end
    puts""
end
