from bs4 import BeautifulSoup
import requests


def bugs_song_chart():
    result = []
    request = requests.get("https://music.bugs.co.kr/chart")
    html = request.text
    bsObj = BeautifulSoup(html, "html.parser")
    chart = bsObj.findAll("p", {"class": "title"})
    artists = bsObj.findAll("p", {"class": "artist"})

    for i in range(len(chart)):
        # # print(artists[i].text)
        artist = artists[i].text.strip().split("\n")[0]
        titles = chart[i].text.strip()
        result += ["{0:3d}위 {1} - {2}".format((i-1) * 50 + j + 1, artist, titles)]

    if len(result) > 0:
        for r in result:
            print(r)

    file = open('bugsTop100.txt', 'w', -1, 'UTF-8')
    for i in range(len(chart)):
        # artist 는 밑에 두 줄에 공백이 나오기 때문에
        # 0번 배열로 적어 놓았습니다.
        artist = artists[i].text.strip().split('\n')[0]
        titles = chart[i].text.strip()
        data = '{0:3d}위 {1} - {2}'.format(i+i, artist, titles)
        file.write(data + '\n')

    print("파일 쓰기 완료")
    file.close()


if __name__ == "__main__":
    bugs_song_chart()
#     song_chart = bugs_song_chart()
#     artist_chart = bugs_song_chart()
#     # for i in range(len(song_chart)):
#     #    print("{0:3d}위 {1} - {2}".format(i+1, artist_chart[i], song_chart[i]))
