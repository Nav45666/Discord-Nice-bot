<h1 align="center">Discord Nice Bot</h1>

<p align="center">
A lightweight Discord bot written in <b>Python</b> that automatically replies <b>"Nice."</b> when trigger phrases such as <code>69</code> appear in chat.
</p>

<hr>

<h2>Features</h2>

<ul>
<li>Detects trigger phrases like <code>69</code>, <code>sixty nine</code>, etc.</li>
<li>Sends randomized "Nice" responses</li>
<li>Ignores configured channels</li>
<li>Lightweight and easy to deploy</li>
<li>Built using the <b>discord.py</b> library</li>
</ul>

<hr>

<h2>How It Works</h2>

<p>
The bot listens to messages sent in a Discord server.  
Whenever a message contains a configured trigger phrase, the bot replies with a randomized response from its response list.
</p>

<p><b>Example</b></p>

<pre>
User: That number is 69
Bot: Nice.
</pre>

<hr>

<h2>Tech Stack</h2>

<ul>
<li>Python</li>
<li>discord.py</li>
<li>Event-driven message handling</li>
</ul>

<hr>

<h2>Installation</h2>

<h3>1. Clone the Repository</h3>

<pre>
git clone https://github.com/Nav45666/Discord-Nice-bot.git
cd Discord-Nice-bot
</pre>

<h3>2. Install Dependencies</h3>

<pre>
pip install discord.py
</pre>

<h3>3. Add Your Bot Token</h3>

<p>Insert your Discord bot token into the configuration file:</p>

<pre>
TOKEN = "your_discord_bot_token"
</pre>

<h3>4. Run the Bot</h3>

<pre>
python bot.py
</pre>

<hr>

<h2>Configuration</h2>

<p>You can customize triggers, responses, and ignored channels.</p>

<pre>
ignored_channels = []

triggers = [
"69",
"sixty nine",
"sixty-nine"
]

responses = [
"Nice.",
"Naisu."
]
</pre>

<hr>

<h2>Bot Functions</h2>

<h3>on_ready()</h3>

<p>
Triggered when the bot successfully connects to Discord.
</p>

<b>Purpose</b>

<ul>
<li>Confirms the bot is online</li>
<li>Prints login information to the console</li>
</ul>

<pre>
Bot connected as NiceBot#1234
</pre>

<hr>

<h3>on_message(message)</h3>

<p>
Event listener that runs whenever a message is sent in the server.
</p>

<b>Responsibilities</b>

<ul>
<li>Reads incoming messages</li>
<li>Checks if the message contains a trigger phrase</li>
<li>Ignores messages from the bot itself</li>
<li>Ensures the channel is not ignored</li>
<li>Sends a response when a trigger is detected</li>
</ul>

<hr>

<h3>contains_trigger(message_content)</h3>

<p>
Helper function that checks if a message contains any trigger phrase.
</p>

<b>Input</b>

<pre>
message_content (string)
</pre>

<b>Output</b>

<pre>
True or False
</pre>

<hr>

<h3>get_random_response()</h3>

<p>
Returns a random response from the predefined list.
</p>

<pre>
Nice.
Naisu.
</pre>

<hr>

<h3>is_ignored_channel(channel_id)</h3>

<p>
Checks if the current channel is listed in the ignored channels.
</p>

<pre>
True  → Bot will not respond
False → Bot will respond normally
</pre>

<hr>

<h2>Project Structure</h2>

<pre>
Discord-Nice-bot
│
├── bot.py
├── config.py
└── README.md
</pre>

<hr>

<h2>Future Improvements</h2>

<ul>
<li>Add slash commands</li>
<li>External configuration file</li>
<li>Command to dynamically add triggers</li>
<li>Cooldown system to prevent spam</li>
</ul>

<hr>

<h2>Author</h2>

<p>
<b>Nav</b><br>
Electronics Engineering Student<br>
Interested in Python, Embedded Systems, and Web Development
</p>
