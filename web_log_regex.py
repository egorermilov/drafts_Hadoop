import re


line = '10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469'
regex = '([(\d\.)]+) ([w.-]+) ([w.-]+) \[(.*?)\] "(.*?) (.*?) (.*?)" (\d+) (\d+)'

ip, identity, username, time, method, path, protocol, status, size = re.match(regex, line).groups()

print(status)