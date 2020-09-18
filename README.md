# Discord Invite Checker
Generates and checks Discord invite codes.

## Features:
- Generates Codes
- Checks Codes
- See above

## Chances of getting a valid code
Given a randomly generated invite code, each character can be:
- ASCII Uppercase
- ASCII Lowercase
- ASCII Numerical

Which is 62 possible combinations per character.

For a default 6 character long invite code, that would be a `1/56,800,235,584` (56 billion 800 million 235 thousand 584) chance of guessing an invite code if there was only one invite code in existence (if you can't visualize this, see [here](https://www.youtube.com/watch?v=8YUWDrLazCg)). If there were two invite codes, you would be 1/2 as lucky to guess a code. If there were three invite codes, you would be 1/3 as lucky to guess a code. Same goes for the ammount of checks you complete.

This is a number that can be hard to cut down. Currently, the checker will guess willy-nilly. Future updates may include tracking for used codes. 

## TODO:
- Webhooks
- Used codes tracking
- Including server information in results
