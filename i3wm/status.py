from i3pystatus import Status

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock", format="%H:%M:%S %d/%m/%y",)

# This would look like this:
# Discharging 6h:51m
status.register("battery",
    format="{status} {percentage:.2f}% {remaining:%H:%M}",
    alert=True,
    alert_percentage=5,
    status={
        "DIS":  "⚡",
        "CHR":  "⚇",
        "FULL": "Bat full",
    },)

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
 #status.register("network",interface="eth0", format_up="{v4cidr}",)

# Note: requires both netifaces and basiciw (for essid and quality)
# status.register("network",
#     interface="wlan0",
#     format_up="{essid}"
#     #format_up="{essid} {quality:03.0f}%",
# )

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk", path="/home", format="⛁ {used}/{total}G",)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio", format="♪ {volume}",)

status.run()
