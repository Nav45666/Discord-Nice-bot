<h1 align="center">Discord Utility Bot</h1>

<p align="center">
A multifunctional Discord bot built using <b>Python</b> and <b>discord.py</b>.  
The bot provides interactive commands including games, quizzes, polls, direct messaging utilities, and YouTube search functionality.
</p>

<hr>

<h2>Overview</h2>

<p>
This project is a Python-based Discord bot designed to demonstrate event-driven programming using the 
<code>discord.py</code> library. The bot includes multiple interactive commands such as games, quizzes,
utility tools, and automated responses for server interaction.
</p>

<p>
The project also integrates external libraries including <code>yt_dlp</code> for YouTube search functionality
and <code>dotenv</code> for secure environment variable management.
</p>

<hr>

<h2>Technologies Used</h2>

<ul>
<li>Python</li>
<li>discord.py</li>
<li>yt_dlp</li>
<li>python-dotenv</li>
<li>Asyncio</li>
<li>Logging</li>
</ul>

<hr>

<h2>Installation</h2>

<h3>1. Clone the Repository</h3>

<pre>
git clone https://github.com/Nav45666/Discord-Nice-bot.git
cd Discord-Nice-bot
</pre>

<h3>2. Install Required Dependencies</h3>

<pre>
pip install discord.py python-dotenv yt_dlp
</pre>

<h3>3. Configure Environment Variables</h3>

Create a <code>.env</code> file and add your Discord bot token.

<pre>
DISCORD_TOKEN=your_bot_token_here
</pre>

<h3>4. Run the Bot</h3>

<pre>
python bot.py
</pre>

<hr>

<h2>Bot Events</h2>

<h3>on_ready()</h3>

<p>
Triggered when the bot successfully connects to Discord.
</p>

<ul>
<li>Confirms the bot has started</li>
<li>Displays the bot name in the console</li>
</ul>

<pre>
We are ready to go in, BotName
</pre>

<h3>on_member_join(member)</h3>

<p>
Executed when a new user joins the server.
</p>

<ul>
<li>Sends a welcome direct message to the new member</li>
</ul>

<h3>on_message(message)</h3>

<p>
Handles incoming messages and ensures commands are processed properly.
</p>

<ul>
<li>Ignores messages from the bot itself</li>
<li>Passes messages to the command handler</li>
</ul>

<hr>

<h2>Commands</h2>

<h3>!hello</h3>

<p>
Greets the user who invoked the command.
</p>

<pre>
!hello
</pre>

Example response:

<pre>
Hello @username!
</pre>

<hr>

<h3>!dm</h3>

<p>
Sends a direct message to the user containing their input message.
</p>

<pre>
!dm Hello there
</pre>

Response:

<pre>
You said Hello there
</pre>

<hr>

<h3>!reply</h3>

<p>
Replies directly to the user's message in the channel.
</p>

<pre>
!reply
</pre>

<hr>

<h3>!poll</h3>

<p>
Creates a simple reaction-based poll in the channel.
</p>

<pre>
!poll Do you like this bot?
</pre>

Features:

<ul>
<li>Creates an embedded poll message</li>
<li>Adds 👍 and 👎 reaction options</li>
</ul>

<hr>

<h3>!flip (aliases: coin, coinflip)</h3>

<p>
Simulates a coin flip game. Users can optionally guess the outcome.
</p>

<pre>
!flip
!flip heads
!flip tails
</pre>

Possible outcomes:

<ul>
<li>Coin result displayed</li>
<li>Win / Lose message if guessing</li>
</ul>

<hr>

<h3>!rps (aliases: rockpaperscissors)</h3>

<p>
Play Rock-Paper-Scissors against the bot.
</p>

<pre>
!rps rock
!rps paper
!rps scissors
</pre>

Features:

<ul>
<li>Random bot choice</li>
<li>Win/Lose/Tie result calculation</li>
</ul>

<hr>

<h3>!medquiz</h3>

<p>
Launches an interactive medical multiple-choice quiz.
</p>

Features:

<ul>
<li>User selects number of questions</li>
<li>Randomized question selection</li>
<li>Score tracking</li>
<li>Explanation display after incorrect answers</li>
<li>Timeout protection</li>
</ul>

Example:

<pre>
!medquiz
</pre>

<hr>

<h3>!quiz</h3>

<p>
General knowledge quiz with multiple-choice questions.
</p>

Features:

<ul>
<li>Randomized questions</li>
<li>Interactive answer system</li>
<li>Score calculation</li>
<li>Timed responses</li>
</ul>

Example:

<pre>
!quiz
</pre>

<hr>

<h3>!yt (aliases: youtube, search)</h3>

<p>
Searches YouTube and returns the top video results.
</p>

Example:

<pre>
!yt python tutorial
</pre>

Output example:

<pre>
1. Video Title
2. Video Title
3. Video Title
</pre>

Features:

<ul>
<li>Uses yt_dlp for searching</li>
<li>Returns top 3 YouTube results</li>
<li>Provides clickable video links</li>
</ul>

<hr>

<h2>Logging</h2>

<p>
All bot activity and debugging information are logged to:
</p>

<pre>
discord.log
</pre>

This assists with debugging and monitoring bot behavior.

<hr>

<h2>Project Structure</h2>

<pre>
Discord-Nice-bot
│
├── bot.py
├── .env
├── discord.log
└── README.md
</pre>

<hr>

<h2>Future Improvements</h2>

<ul>
<li>Slash command support</li>
<li>Music playback functionality</li>
<li>Database-backed quiz system</li>
<li>Advanced moderation commands</li>
<li>Improved error handling</li>
</ul>

<hr>

<h2>Author</h2>

<p>
<b>Abhinav</b><br>
Python • Embedded Systems • Software Development
</p>
