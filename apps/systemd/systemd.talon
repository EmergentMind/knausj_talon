tag: user.systemd
tag: user.terminal
-

# System-wide services
action(user.service): user.insert_cursor("systemctl --no-pager [|].service")
action(user.service_stop): user.insert_cursor("systemctl --no-pager stop [|].service")
action(user.service_start): user.insert_cursor("systemctl --no-pager start [|].service")
action(user.service_status): user.insert_cursor("systemctl --no-pager status [|].service")
action(user.service_enable): user.insert_cursor("systemctl --no-pager enable [|].service")
action(user.service_disable): user.insert_cursor("systemctl --no-pager disable [|].service")

# System-Wide timers
action(user.timer): user.insert_cursor("systemctl --no-pager [|].timer")
action(user.timer_stop): user.insert_cursor("systemctl --no-pager stop [|].timer")
action(user.timer_start): user.insert_cursor("systemctl --no-pager start [|].timer")
action(user.timer_status): user.insert_cursor("systemctl --no-pager status [|].timer")
action(user.timer_enable): user.insert_cursor("systemctl --no-pager enable [|].timer")
action(user.timer_disable): user.insert_cursor("systemctl --no-pager disable [|].timer")

# User timers
action(user.timer_user): user.insert_cursor("systemctl --user --no-pager [|].timer")
action(user.timer_user_stop): user.insert_cursor("systemctl --user --no-pager stop [|].timer")
action(user.timer_user_start): user.insert_cursor("systemctl --user --no-pager start [|].timer")
action(user.timer_user_status): user.insert_cursor("systemctl --user --no-pager status [|].timer")
action(user.timer_user_enable): user.insert_cursor("systemctl --user --no-pager enable [|].timer")
action(user.timer_user_disable): user.insert_cursor("systemctl --user --no-pager disable [|].timer")


# TODO - generic
timer user list: "systemctl --user list-timers\n"
timer user all: "systemctl --user --all list-timers\n"
timer list: "systemctl list-timers\n"
timer all: "systemctl --all list-timers\n"

system cuttle: "systemctl "
