#!/usr/bin/python3
# encoding: utf-8

from i3pystatus import Status
    
status = Status(standalone=True)

status.register("clock",
                format=" %d/%m/%Y %H:%M",)

status.register("battery",
    format="{percentage:.2f}% | {remaining:%E%hh:%Mm}",
    alert=False,
    alert_percentage=5,
    status={
        "DIS": "↓",
        "CHR": "↑",
        "FULL": "=",
    },)

# status.register("network",
#                 interface="veth40851ef",
#                 format_up="{v4cidr}",)

status.register("disk",
                path="/",
                format="{used}/{total}G [{avail}G]",)

status.register("mem", format="{avail_mem:.0f} Mb")

status.register("pulseaudio",
                format="♪ {volume}% {muted}",)

status.run()
