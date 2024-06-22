import yt_dlp


def download_app():
    url = input("Enter a video link: ")

    ydl = yt_dlp.YoutubeDL()
    ydl.download(url)


def get_resolutions(formats: list):
    resolutions = list()

    print(formats[0])

    for format in formats:
        res: str = format.get("resolution")

        if "audio" in res:
            continue

        if format.get("acodec") == "none":
            continue

        if format.get("vcodec") == "none":
            continue

        if res is None:
            continue

        if format.get("format_note") == "storyboard":
            continue

        if res not in resolutions:
            resolutions.append(res)

    return resolutions


if __name__ == "__main__":
    download_app()
