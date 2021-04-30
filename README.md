# FreeDiscord
## Welcome to the official GitHub page of the FreeDiscord bot!
FreeDiscord is a Discord bot made by the FreeTechnologies team ([SKBotNL](https://github.com/SKBotNL), [ItsJustLag](https://github.com/ItsJustLag), [recallwhoiam](https://github.com/recallwhoiam), [Odysseus](https://github.com/Odysseus443), and [antistalker](https://github.com/stalker0000)) that you can edit and self host. This bot is 100% open source, so feel free to make forks of it, if you want. Just *please* at least give the original product some credit, and don't say you created the bot yourself. We appreciate it.
If you find an issue, or have a feature suggestion, please let us know by opening an issue [here](https://github.com/FreeTechnologies/FreeDiscord/issues). :)

## Documentation

### Starting the bot
#### Make sure you have [Python 3](https://www.python.org/downloads/) installed (and put in path, if you're on Windows 10)!!!
1. Clone the repository: `git clone https://github.com/FreeTechnologies/FreeDiscord.git` and go to step 2. An alternative is to download the ZIP file, unzip it, shift + right click in the `FreeDiscord-main` folder, click on `Open Powershell window here`, and continue with step 3.
2. `cd` to the repository folder: `cd FreeDiscord`.
3. Make sure all the dependencies are installed, Windows: `python -m pip install discord.py requests asyncio gitpython psutil datetime` Linux: `pip3 install discord.py requests asyncio gitpython psutil datetime`.
4. Run `python3 freesetup.py` for an interative configuration creator. The bot will not run if you don't do this.
5. Before starting, make sure the Server Members Intent is enabled in your bot settings in the Discord Developer Portal.
6. To make sure the `mute` and `unmute` commands work, please make a role called `muted` in your server. The bot will not (yet) do this for you.
7. Run the main bot file: `python3 bot.py`.

### Features

There are many features of the bot. These features include:

- VirusTotal file scanning
- Message encryption
- Moderation
- Fun commands
- Utility commands
- Custom playing status that you can customize per instance
- Lots more
- More being added regularly!

Like earlier said, if you have any feature requests or issues with the bot, open an issue [here](https://github.com/FreeTechnologies/FreeDiscord/issues)!
Enjoy the bot! We hope you have as much fun with it as we had programming it! :)

### Main Instance
You can find the main instance of FreeDiscord that is hosted for you here (really good uptime):

[![FreeDiscord Bot](https://top.gg/api/widget/829158610965495848.svg)](https://top.gg/bot/829158610965495848)

### Support Server
Having some problems? Have some suggestions? Tell us here:

[![Support Server Banner](https://discord.com/api/guilds/834927331655024640/widget.png?style=banner3)](https://discord.gg/UV3zAbdpVk)

Made with discord.py v9
