"""
d8888b. db    db d888888b db   db  .d8b.  d8b   db db    db   d888888b
88  `8D `8b  d8' `~~88~~' 88   88 d8' `8b 888o  88 `8b  d8'     `88'
88oooY'  `8bd8'     88    88ooo88 88ooo88 88V8o 88  `8bd8'       88
88~~~b.    88       88    88~~~88 88~~~88 88 V8o88    88         88
88   8D    88       88    88   88 88   88 88  V888    88        .88.
Y8888P'    YP       YP    YP   YP YP   YP VP   V8P    YP      Y888888P


db       .d88b.  db    db d88888b   db    db  .d88b.  db    db
88      .8P  Y8. 88    88 88'       `8b  d8' .8P  Y8. 88    88
88      88    88 Y8    8P 88ooooo    `8bd8'  88    88 88    88
88      88    88 `8b  d8' 88~~~~~      88    88    88 88    88
88booo. `8b  d8'  `8bd8'  88.          88    `8b  d8' 88b  d88
Y88888P  `Y88P'     YP    Y88888P      YP     `Y88P'  ~Y8888P'

"""

#!/usr/bin/env python 
#encoding: utf-8
import socket
print("""Thanks for Using this Tool
 ______        _____ ____  _   _ _____ ____
/ ___\ \      / /_ _|  _ \| | | | ____|  _ \\
\___ \\\ \ /\ / / | || |_) | |_| |  _| | |_) |
 ___) |\ V  V /  | ||  __/|  _  | |___|  _ <
|____/  \_/\_/  |___|_|   |_| |_|_____|_| \_\\

请输入以下数字来实现功能:
[1]后台扫描
[2]arp欺骗
[3]关于作者
""")

while 1:
    type=int(input("-->"))
    if(type>3 or type<1):
        print("请输入[1~3]")
    else:
        break
if(type==1):
    import wwwscan
