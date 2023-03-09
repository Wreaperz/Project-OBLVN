# Project OBLVN
Project OBLVN is an artificial intelligence project aimed at the game VALORANT. The ultimate goal is to create a self-sustaining AI agent that can play the game VALORANT at a competitive level.

# Settings
Monitor: 15.6" Monitor (Asus Strix 15) 1080p (1920x1080)

Enemy Outlines: Red (default)

DPI: 800

Sens: 1.06

Scoped: 1

ADS: 1

Important: The project is designed to be as dynamic as possible, but certain settings may need to be edited to suit individual needs.


# The Inspiration
I've always been into automation, but I've really enjoyed learning about Artificial Intelligence (AI) and Machine Learning (ML). The ORIGINAL inspiration for this project was actually OpenAI's "OpenAI Five" team that beat the top DOTA players in the world, several years ago. The idea that a machine can out-perform a human in a game that is so complex is probably what really piqued my interest. Bots have existed for a long time, and even AI has learned how to play Pong, etc. But... to be able to compete against the BEST of the best in a game with hundreds of thousands of minute variables, alongside the psychology of the game (baits, pushes, fakes, etc.)... that's a whole new level.

Mini-Documentary: https://www.youtube.com/watch?v=tfb6aEUMC04

Process and Structure: https://developer.valvesoftware.com/wiki/Dota_Bot_Scripting#Complete_takeover

# What I Have
I started out this project by breaking down the game into several "levels" of complexity, based on these general guidelines from a fairly-recent video about ML and computer-vision: https://www.youtube.com/watch?v=UvoyMGxN89Y

The TL;DR version is that Level 1, 2, and 3 are short-, medium-, and long-term performance. Short-term consists of reacting to enemies, shooting, moving, etc. Level 2 consists of map navigation and ammo/inventory management. Finally, Level 3 consists of long-term strategy, teamwork, and player coordination.

This project is definitely still on Level 1, thought fairly far into it. As of the moment, I have enemy detection and shooting, along with movement (if I script it out).

# Where from Here?
Of all the ways I could approach this project, I'm endeavoring to be as LEGAL as possible. I've already reached out to Riot Support (multiple times), but never got a satisfactory answer on whether or not the project is allowed (simply because it doesn't fall into the normal category of applications. This isn't a stat-tracker that uses the Riot API). I could've gone the hacking route and read the game's memory for all the data, but I'm fairly confident this route would've been/will be denied lol. Finally, there IS the computer-vision route (YOLO, etc.). This route IS possible, but is tedious, requires large amounts of data, and requires extensive computing resources. So is there a third? Well, I'd like to think so. My route is to teach the AI to play as if it is blind. See https://www.youtube.com/watch?v=4HR7t4lJsdY for inspiration. In essence, the goal is to treate the AI as if it has no clue how to play or where to go (it can't "SEE" the map and doesn't have depth-perception like we do).
