import requests as re

def request(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        # 'cookie': 'CWC=snQlgc4KhlhXnTIIiROlDIpnt; _cwutmzsrc=D; _cwutmzmed=NN; _cwutmz=utmcsr%3D%28direct%29%7Cutmgclid%3D%7Cutmccn%3D%28direct%29%7Cutmcmd%3D%28none%29%7Cutmtrm%3D%7Cutmcnt%3D; CurrentLanguage=en; _abtest=34; languageSelected=en; .AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8JUh_GoNOjhBqUJ2d7OuCzRYYvAhjMppxcVPKRvux2-nTQufk06gRxnYVPDPG3UtPqsVVSimO6wvgPUJ1KOm6uK2GaewjP39mKdb2OCidOWZcTDpOmT5VyUoki-X9XEKFgHilNuoHYU-jywZr9VEsrU; _gcl_au=1.1.1467426715.1777004066; BHC=snQlgc4KhlhXnTIIiROlDIpnt; _carSearchType=1; _ga=GA1.1.1973035701.1777004067; vernacularPopupClose=1; _fbp=fb.1.1777004072626.40386743547474174; cebs=1; _ce.clock_data=245%2C45.114.65.131%2C1%2Cb87543ecbc0ba610d9f06f9f2c432a46%2CChrome%2CIN; _AsktheExperts=1; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22582d72f8-2280-4ab4-88b7-1899623bd7e3%5C%22%2C%5B1777004073%2C124000000%5D%5D%22%5D%5D%5D; FCNEC=%5B%5B%22AKsRol9m-I3Znkqtq9KzDQk4phKoHH1vOVIdjcomPYc71hjLO8dSwcY-imWm-QbyUUzggRreMbdW0A6V0tWdK-5CbTWxhC1c0EkQuXyHFzddgEOJ0XekIEsqra3Wqfe8ppJGfZ4lhi1yzzA03jMbobt1lqotPJPnww%3D%3D%22%5D%5D; _uetsid=1a89c6303f9411f195a1f58b655943bf; _uetvid=1a8aa5503f9411f192e721aece0df772; _ce.seg.targeting=N4IgbgpgTgzglgewHYgFwEYA0ICGBjPAVwFtCAbHAFwgBMBlSqiNUPMuPAazQG0BdbADMEUYgH0YhAEbE4MeMl4CQABzgAPCGTERISSkuwQ8CYsWh4IOvQdT9sAcwQ5tJpJFiIkMQyDYdOWjE8Rl8cbwB3aCDJKEgAT19iHHUxCJFKAAsWECQSKWg0AAZsIigoCCQ8RNQQAFU6ABEQAF8W7GTKPEzaOggHc30ASRofO2VCJHNKAGFkGjhKLzHgdpBpuaQFpeQVtqA%3D%3D%3D; __gads=ID=f694d49be826bc5e:T=1777004104:RT=1777004104:S=ALNI_Mbebl58GX3HkABuVOx-VY-8GKktcA; __gpi=UID=00001364715fd532:T=1777004104:RT=1777004104:S=ALNI_MaWryfvh0fSqHngnmiHahQKtrES6A; __eoi=ID=2fa9fb9ba0eff17a:T=1777004104:RT=1777004104:S=AA-AfjYRyPKBnVE6ZNfcykD5zoSn; _userModelHistory=2033; _ce.s=lcw~1777004152835~v~81b058c770dd5f4484cdf3f6b88534c28ae581f1~vir~new~lva~1777004072774~vpv~0~as~false~v11.cs~44156~v11.s~18d52e90-3f94-11f1-8adb-2bfbfcc33acb~v11.vs~81b058c770dd5f4484cdf3f6b88534c28ae581f1~v11.fsvd~eyJub3RNb2RpZmllZFVybCI6Imh0dHBzOi8vd3d3LmNhcndhbGUuY29tLyIsInVybCI6ImNhcndhbGUuY29tIiwicmVmIjoiIiwidXRtIjpbXX0%3D~v11.sla~1777004072955~v11.ss~1777004072960~v11ls~18d52e90-3f94-11f1-8adb-2bfbfcc33acb~lcw~1777004152837; quizSlug2={%222781%22:%22question%22}; _pageviews_modelid=2033; _cwv=snQlgc4KhlhXnTIIiROlDIpnt.snQlgc4KhlhXnTIIiROlDIpnt.1777004065.1777004204.1777004208.1; cebsp_=6; bhs_cw=snQlgc4KhlhXnTIIiROlDIpnt.8RslexG1zK.1777004065.1777004207.1777004209.1; _ga_Z81QVQY510=GS2.1.s1777004067$o1$g1$t1777004380$j60$l0$h0',
    }

    response = re.get(url, headers=headers,timeout=10)

    try:
        if response.status_code == 200:
            return response.text
        else:
            print("Status:", response.status_code)
    except Exception as e:
        print("Error:", e)