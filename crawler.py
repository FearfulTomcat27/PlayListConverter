import requests
from bs4 import BeautifulSoup


# 获取网页内容
def get_html(url):
    try:
        # 设置请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        return response
    except Exception as e:
        print(e)


def write_to_file(songList, singerList):
    file = open("PlayList.txt", "w+", encoding="utf-8")
    try:
        # 写入歌单
        for song, singer in zip(songList, singerList):
            file.write(song + " - " + singer + "\n")
        return "success"
    except Exception as e:
        print(e)
        return "fail"
    finally:
        file.close()


# 获取歌单
def get_musicList(url):
    # 获取网页内容
    html = get_html(url).text
    soup = BeautifulSoup(html, features="html.parser")

    # 定义歌曲列表和歌手列表
    songList = []
    singerList = []

    # 筛选出歌单所在的标签
    p_tag = soup.select('div[style="margin-top:8px"] p')

    # 循环遍历歌单
    for p in p_tag:
        # 判断是歌手还是歌曲
        if (p.text.find("•") != -1):
            singerList.append(p.text.split("•")[0].strip())
        else:
            songList.append(p.text)

    # 写入文件
    # write_to_file(songList, singerList)
    for song, singer in zip(songList, singerList):
        print(song + "-" + singer)
    print("共写入了" + str(len(songList)) + "首歌曲")
