async def ispremium(user:guilded.User) -> bool:
    '''
    Returns bool,tier
    Tier = 'None', 'copper', 'silver', 'gold'
    '''
    ss = await bot.fetch_server(supportserverid)
    a = False
    if len(ss.members) < 3:
        await ss.fill_members()
    if user in ss.members:
        a = True
    if not a:
        return False, 'None'
    premium = []
    roles = await (await ss.fetch_member(user.id)).fetch_role_ids()
    for i in premiumroles:
        if int(i[0]) in roles:
            premium.append([True, (i[1]).lower()])
    if premium == []:
        return False, 'None'
    return premium[-1][0], premium[-1][1]
