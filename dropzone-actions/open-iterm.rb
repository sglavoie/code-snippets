# Dropzone Action Info
# Name: Open Terminal at Path
# Description: Drop a file or folder on this action to open a new iTerm window at the files path. You can also drop a textual path.
# Handles: Files, Text
# Creator: Dennis Kuypers
# Modified by: Sébastien Lavoie
# URL: http://dk.kymedia.de
# Events: Clicked, Dragged
# SkipConfig: No
# RunsSandboxed: No
# Version: 1.2
# MinDropzoneVersion: 3.0
# UniqueID: 1030

def dragged
  dir = false
    
  case ENV['dragged_type']
  when 'files'
    # If it's a directory then cd to that directory, otherwise we will cd to the directory the file is in
    if File.directory?($items[0])
      dir = $items[0]
    else
      dir = File.dirname($items[0])
    end
  when 'text'
    # Verify that this is a directory path
    dir = $items[0] if File.directory?($items[0])
  end
  
  puts dir
    
  # Launch iTerm in desired directory
  if dir
    puts `osascript -so <<END
    tell application "iTerm"
      activate
      delay 0.2
      try
          tell current window
            create tab with default profile
              tell current session
                write text "cd '#{dir}'"
              end tell
          end tell
        on error
          create window with default profile
          tell current session of current window
            write text "cd '#{dir}'"
          end tell
        end try
    end tell
END`
  else
    # Could not figure out what the user wants. Dump to console and notify user.
    puts "Could not figure out what to do with data: #{$items.inspect}"
    $dz.fail("Not a file or directory path")
  end
  
  $dz.url(false)
end

def clicked
  puts `osascript -so <<END
  tell application "iTerm"
    activate
  end tell
END`
  $dz.url(false)
end
