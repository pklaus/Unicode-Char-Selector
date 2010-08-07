on run argv
	tell application "System Events"
		tell process "finder"
			activate
			keystroke tab using {command down}
		end tell
		set front_app to (path to frontmost application as Unicode text)
		tell application front_app
			activate
			set clipboardStack to the clipboard
			set the clipboard to item 1 of argv
			keystroke "v" using {command down}
			delay 0.1
			set the clipboard to clipboardStack
		end tell
	end tell
end run