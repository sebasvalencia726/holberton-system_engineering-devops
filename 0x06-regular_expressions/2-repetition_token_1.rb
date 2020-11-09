#!/usr/bin/env ruby
ARGV.each do|a|
    var = a.scan(/hbtn|htn/)
    var.each do |i|
        print i
    end
    puts""
end
