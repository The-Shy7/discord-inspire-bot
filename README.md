# Discord Inspire Bot 
A Discord bot that sends positive and encouraging messages. Built using Python through Repl.it. 
The bot responds to users with positive messages when it detects a negative word such as "sad", "angry", etc.
Clients can add new encouragements through the $new command and delete encouragements using the $del command. 
Clients can also use the $inspire command for the bot to generate a random inspirational quote (with the author) and send it as a message.
Lastly, clients have the ability to turn off the bot's responses to negative words by using the $responding command.

## Example usage of $new and $del
$new Good luck! (adds "Good luck!" to a list of user-added encouragements; current list: ['Good luck!'])

$new Cheer up! (current list: ['Good luck!', 'Cheer up!'])

$del 1 (deletes the element at index 1 of the list; current list: ['Good luck!'])

## Example usage of $responding
$responding true (the bot will respond to negative words)

$responding [any word besides true] (the bot will not respond to negative words)
