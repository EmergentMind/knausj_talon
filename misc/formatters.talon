#Note: Appending $ will anchor the command
#provide both anchored and unachored commands via 'over'
<user.format_text>$: insert(format_text)
<user.format_text> over: insert(format_text)
phrase <user.text>$: insert(user.formatted_text(user.text, "ALL_LOWERCASE"))
phrase <user.text> over: insert(user.formatted_text(user.text, "ALL_LOWERCASE"))
speak <user.text>$: insert(user.formatted_text(user.text, "ALL_LOWERCASE"))
speak <user.text> over: insert(user.formatted_text(user.text, "ALL_LOWERCASE"))
#word <user.word>: insert(user.formatted_text(user.word, "ALL_LOWERCASE"))
list formatters: user.list_formatters()
hide formatters: user.hide_formatters()
