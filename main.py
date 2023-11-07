import crawler
from argparse import ArgumentParser

def run():
    parser = ArgumentParser()
    parser.add_argument('-u', '--url', help='URL of the playlist')
    args = parser.parse_args()
    url = args.url

    # 输入歌单URL
    if args.url is None:
        url = input("请输入歌单URL：")

    crawler.get_musicList(url)


if __name__ == '__main__':
    run()
