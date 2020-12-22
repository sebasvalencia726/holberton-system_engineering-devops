# 0x0F. Load balancer

## Foundations - System engineering & DevOps ― Web stack

by Sylvain Kalache, co-founder at Holberton School

For this project, students are expected to look at these concepts:

## Load balancer

Ever wonder how Facebook, Linkedin, Twitter and other web giants are handling such huge amounts of traffic? They don’t have just one server, but tens of thousands of them. In order to achieve this, web traffic needs to be distributed to these servers, and that is the role of a load-balancer.

![Holberton image](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/6cefdd14b2f8c36789cba132bd5a10d42d88a177.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201221%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201221T180830Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=52417cbe2964efef41df4d77076afa84a63c27527c4ef4b02140f1d09bbb4f33)

### Readme:

* [Load-balancing](https://www.thegeekstuff.com/2016/01/load-balancer-intro/)
* [Load-balancing algorithms](https://devcentral.f5.com/s/articles/intro-to-load-balancing-for-developers-ndash-the-algorithms)


## Web stack debugging

Debugging usually takes a big chunk of a software engineer’s time. The art of debugging is tough and it takes years, even decades to master, and that is why seasoned software engineers are the best at it… experience. They have seen lots of broken code, buggy systems, weird edge cases and race conditions.

## Non-exhaustive guide to debugging
### Holberton specific

If you are struggling to get something right that is run on the checker, like a Bash script or a piece of code, keep in mind that you can simulate the flow by starting a Docker container with the distribution that is specified in the requirements and by running your code. Check the Docker concept page for more info.

## Test and verify your assumptions

The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:

* Is the web server started? - You can check using the service manager, also double check by checking process list.
* On what port should it listen? - Check your web server configuration
* Is it actually listening on this port? - `netstat -lpdn` - run as root or sudo so that you can see the process for each listening port
* It is listening on the correct server IP? - `netstat` is also your friend here
* Is there a firewall enabled?
* Have you looked at logs? - usually in `/var/log` and `tail -f` is your friend
* Can I connect to the HTTP port from the location I am browsing from? - `curl` is your friend

There is a good chance that at this point you will already have found part of the issue.

## Get a quick overview of the machine state

[Youtube video First 5 Commands When I Connect on a Linux Server](https://www.youtube.com/watch?v=1_gqlbADaAw&feature=youtu.be)

When you connect to a server/machine/computer/container you want to understand what’s happened recently and what’s happening now, and you can do this with [5 commands](https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/) in a minute or less:

### w

* shows server [uptime](https://whatis.techtarget.com/definition/uptime-and-downtime) which is the time during which the server has been continuously running
* shows which users are connected to the server
* load average will give you a good sense of the server health - (read more about load [here](https://scoutapm.com/blog/understanding-load-averages) and [here](http://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html))

### history

* shows which commands were previously run by the user you are currently connected to
* you can learn a lot about what type of work was previously performed on the machine, and what could have gone wrong with it
* where you might want to start your debugging work

### top

* shows what is currently running on this server
* order results by CPU, memory utilization and catch the ones that are resource intensive

### df

* shows disk utilization

### netstat

* what port and IP your server is listening on
* what processes are using sockets
* try netstat -lpn on a Ubuntu machine

## Machine

Debugging is pretty much about verifying assumptions, in a perfect world the software or system we are working on would be working perfectly, the server is in perfect shape and everybody is happy. But actually, it NEVER goes this way, things ALWAYS fail (it’s tremendous!).

For the machine level, you want to ask yourself these questions:

* Does the server have free disk space? - `df`
* Is the server able to keep up with CPU load? - `w`, `top`, `ps`
* Does the server have available memory? `free`
* Are the server disk(s) able to keep up with read/write IO? - `htop`

If the answer is no for any of these questions, then that might be the reason why things are not going as expected. There are often 3 ways of solving the issue:

* free up resources (stop process(es) or reduce their resource consumption)
* increase the machine resources (adding memory, CPU, disk space…)
* distributing the resource usage to other machines

## Network issue

For the machine level, you want to ask yourself these questions:

* Does the server have the expected network interfaces and IPs up and running? ifconfig
* Does the server listen on the sockets that it is supposed to? netstat (netstat -lpd or netstat -lpn)
* Can you connect from the location you want to connect from, to the socket you want to connect to? telnet to the IP + PORT (telnet 8.8.8.8 80)
* Does the server have the correct firewall rules? iptables, ufw:
    * `iptables -L`
    * `sudo ufw status`

## Process issue

If a piece of Software isn’t behaving as expected, it can obviously be because of above reasons… but the good news is that there is more to look into (there is ALWAYS more to look into actually).

* Is the software started? init, init.d:
    * `service NAME_OF_THE_SERVICE status`
    `/etc/init.d/NAME_OF_THE_SERVICE status`
* Is the software process running? pgrep, ps:
    * `pgrep -lf NAME_OF_THE_PROCESS`
    * `ps auxf`
* Is there anything interesting in the logs? look for log files in /var/log/ and tail -f is your friend


![Holberton image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png)

## Background Context

You have been given 2 additional servers:

* gc-[STUDENT_ID]-web-02-XXXXXXXXXX
* gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Resources

### Read or watch:

* [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
* [HTTP header](https://www.techopedia.com/definition/27178/http-header)
* [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)
