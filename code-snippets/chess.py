def handleboard(board, last_move):
    import json, chess, os, chess.svg, io, time
    import urllib.parse as url_parse
    from uplink_python.uplink import Uplink
    from cairosvg import svg2png
    from PIL import Image
    timed = time.time()
    otime = timed
    with open('./tmp/cache.json', 'r', encoding="utf-8") as config:
        chesscache = json.load(config)
        config.close()
    print(f'{round(time.time()-timed, 2)} seconds for config loading.')
    timed = time.time()
    path = boardid(board, last_move)
    print(f'{round(time.time()-timed, 2)} seconds for boardid.')
    timed = time.time()
    found = any(obj['key'] == f"chess/{path}" for obj in chesscache)
    print(f'{round(time.time()-timed, 2)} seconds for cache checking.')
    if not found:
        timed = time.time()
        uplink = Uplink()
        access = uplink.request_access_with_passphrase(configdata["storjreq"], configdata["storjtoken"], configdata["storjpasshrase"])
        project = access.open_project()
        print(f'{round(time.time()-timed, 2)} seconds for Uplink loading.')
        timed = time.time()
        if last_move:
            image = Image.open(io.BytesIO(svg2png(bytestring=chess.svg.board(board=board, lastmove=last_move, colors={"square lastmove": "#a3a3a3"}))))
        else:
            image = Image.open(io.BytesIO(svg2png(bytestring=chess.svg.board(board))))
        image.save(f'tmp/{path}', format="webp")
        print(f'{round(time.time()-timed, 2)} seconds for board conversion to webp.')
        timed = time.time()
        with open(f"tmp/{path}", 'r+b') as file_handle:
            upload = project.upload_object(configdata["storjbucket"], f"chess/{path}")
            upload.write_file(file_handle)
            upload.commit()
        os.remove(f"./tmp/{path}")
        print(f'{round(time.time()-timed, 5)} seconds for uploading.')
    print(f'Returning url now - total time: {round(time.time()-otime, 2)}')
    return (
        "https://link.storjshare.io/s/"
        + url_parse.quote(configdata["storjsharetoken"])
        + "/"
        + configdata["storjbucket"]
        + "/chess/"
        + path
        + "?wrap=0"
    )