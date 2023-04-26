@bot.command(name='meme', description='Get a random meme!')
async def mememememmeemememememe(ctx:commands.Context, subreddit:str=None):
    enter = '\n'
    subreddits = [
        'dankmemes',
        'memes',
        'me_irl',
        'wholesomememes',
        'funny',
        'comedyheaven'
    ]
    if subreddit and (subreddit.lower()).replace('r/', '', 1) in subreddits:
        subreddit = (subreddit.lower()).replace('r/', '', 1)
        randomly = ''
    elif subreddit:
        embedig = guilded.Embed(title='Invalid subreddit!', description=f'**Choose from one of the following subreddits:** {enter}r/{f"{enter}r/".join(subreddits)}')
        await ctx.reply(embed=embedig, private=ctx.message.private)
        return
    elif not subreddit:
        superrandom = random.SystemRandom()
        while True:
            superrandom.shuffle(subreddits)
            if superrandom.randint(1, 3) == 1:
                break
        subreddit = superrandom.choice(subreddits)
        randomly = 'randomly '
    embedig = guilded.Embed(title='Fetching meme...', description=f'Getting a meme from a {randomly}selected subreddit: **r/{subreddit}**')
    msg = await ctx.reply(embed=embedig, private=ctx.message.private)
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://meme-api.com/gimme/{subreddit}') as r:
            data = await r.json()
            while data['nsfw'] == True:
                data = await r.json()
            r.close()
        async with cs.get(data["postLink"]) as r:
            url = f'{str(r.url)}.json'
            r.close()
        async with cs.get(url) as r:
            dta = []
            try:
                rawdata = (json.loads(await r.text()))
                dta.append(rawdata[0]["data"]["children"][0]["data"]["num_comments"])
                dta.append(rawdata[0]["data"]["children"][0]["data"]["total_awards_received"])
            except:               
                class MyHTMLParser(HTMLParser):
                    def __init__(self):
                        HTMLParser.__init__(self)
                        self.recording = 0
                        self.data = []
                        self.dta = []

                    def handle_starttag(self, tag, attributes):
                        if tag != 'div':
                            return
                        if self.recording:
                            self.recording += 1
                            return
                        for name, value in attributes:
                            if name == 'id' and value == 'remository':
                                break
                            else:
                                return
                        self.recording = 1

                    def handle_endtag(self, tag):
                        if tag == 'div' and self.recording:
                            self.recording -= 1

                    def handle_data(self, data):
                        if self.recording and data.endswith("comments"):
                            self.dta.append(data[:-9])
                parser = MyHTMLParser()
                parser.feed(await r.text())
                dta = parser.dta
            r.close()
        async with cs.get(f'https://www.reddit.com/user/{data["author"]}/about.json') as r:
            rawauthordata = await r.json()
            try:
                avatar = rawauthordata['data']['snoovatar_img']
            except:
                avatar = None
            r.close()
        await cs.close()
    
    embedig = guilded.Embed(
        title=f'Posted in r/{data["subreddit"]}',
        url=f'https://reddit.com/r/{data["subreddit"]}',
        description=f'​{enter}[{data["title"]}]({data["postLink"]})'
        )
    embedig.set_image(url=f'{data["url"]}')
    embedig.set_author(name=f'Posted by u/{data["author"]}', url=f'https://www.reddit.com/user/{data["author"]}')
    if avatar:
        embedig.set_thumbnail(url=avatar)
    try:
        embedig.set_footer(text=f'👍 Upvotes {data["ups"]} - 💬 Comments {dta[0]} - 🏆 Awards {dta[1]}')
    except:
        embedig.set_footer(text=f'👍 Upvotes {data["ups"]} - 💬 Comments {dta[0]}')
    await msg.edit(embed=embedig)
