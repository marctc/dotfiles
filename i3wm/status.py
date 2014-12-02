#!/usr/bin/python3
# encoding: utf-8

from i3pystatus import Status
    
status = Status(standalone=True)

status.register("clock",
                format=" %d/%m/%Y %H:%M",)


status.register("network",
                interface="eth0",
                format_up="{v4cidr}",)

status.register("disk",
                path="/",
                format="{used}/{total}G [{avail}G]",)

status.register("mem", format="{avail_mem:.0f} Mb")

status.register("pulseaudio",
                format="♪ {volume}% {muted}",)

status.run()
