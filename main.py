import requests
import json
import csv
import time
import random

def get_jd_comments(url, headers, num_pages, output_file):
    try:

        #    with open(output_file, 'a', encoding='gbk') as csv_file:
        #       csv_file.write("评论内容,地区信息\n")  # 写入CSV文件的表头
        # 只能读取30页
        l = 1
        r = 10
        for page in range(l,r):
            # 更新URL中的page参数
            page_url = url.replace('&page=0', f'&page={page}')

            response = requests.get(page_url, headers=headers, verify=False)
            print(response.text)
            with open('res.txt', 'w', encoding='utf-8') as f:
                f.write(str(response.text))

            if response.status_code == 200:
                # 解析JSON数据
                data = json.loads(response.text)

                # 获取评论列表
                comments = data.get('comments', [])
                num = 0
                # 遍历评论列表并输出评论内容和地区信息
                for comment in comments:
                    content = comment.get('content', '')
                    location = comment.get('location', '')
                    with open(output_file, 'a', encoding='utf-8-sig') as csv_file:
                          csv_file.write(f'"{content}","{location}"\n')  # 写入每条评论到CSV文件
                    print(f"评论内容: {content}")
                    print(f"地区信息: {location}")
                    print('-' * 50)
                    num = num+1
                print(f'加入评论数{num}\n')

                time.sleep(random.random() * 3)

            else:
                print(f"请求失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"发生异常: {e}")


if __name__ == "__main__":
    url = "https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1703744775173&loginType=3&uuid=181111935.16652186012671133573876.1665218601.1703210891.1703744355.27&productId=100018768506&score=2&sortType=6&page=0&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield="
    header = {
        'Cookie': 'shshshfpa=1d08115b-2d03-e35e-c7dc-21cd8a21f431-1667275794; shshshfp=06b495367025f28ef128d7148002d434; shshshfpx=1d08115b-2d03-e35e-c7dc-21cd8a21f431-1667275794; __jdu=16652186012671133573876; __jdv=76161171|cn.bing.com|-|referral|-|1702555669737; mt_xid=V2_52007VwMVVVlbUlMYSBlfAmEDElBfXFRYFk8ebARlB0FaDl8GRhgZGVkZYlQRBkEIUQ8fVR9dBG9WFFEOC1NcTHkaXQZlHxJRQVhXSxxIEl0CbAAaYl1oUmofThlcBW8FGlBVUWJeG0ob; TrackID=185YrK-0xkD7rRutVJ-sat7H3100vO9hy33kKwwP7UKs8uPc82bBESG9PFWwE1dX8rTTGu2w8b7ahTgP1_IcIeXeZqi_0JBveWYS8orihCotz8xF8IZWmCCBwDmWTawET; pinId=79cFfYVvFHXP19pNrjHuDA; pin=jd_tvzMkGDJdrBZ; unick=jd_tvzMkGDJdrBZ; _tp=RsVMHKzNLn%2Fbze17DXsIOQ%3D%3D; _pst=jd_tvzMkGDJdrBZ; PCSYCityID=CN_310000_310100_0; mba_muid=16652186012671133573876; wlfstk_smdl=t9o7jxonrlz8xeymbzhs6kpqnnkhipxc; logintype=qq; npin=jd_tvzMkGDJdrBZ; thor=6B46FBBC8A4F4C73FA3A8102CC0387117A47DA4CA3C00EE3409C0E470130B14289D945536F1A7E576D016B6601C7E85D4A7D79B3335805348454BBD413DBE49901D9FBE6D42F68BD8BB893739CBDFE60523E254F950A2973E84830B409D3B755BB2E33984D99B234611EA8245E13EEEAAFCE0740909B4A4023C803BBBBB4AF37268A90AD6C76B587D71DC778FCE369D92AED0844CB2042501C51BB5EA36456CC; flash=2_uih93d0XyLnZIsIUiyWThMiNR496Z2B5gZ6gZbPftezcznJNvbcHz6HdOnT_OtVtLsfXaXm1YFdar86EbO5i6QjzuU3MlMgMyjW0DyPyIWh*; jsavif=0; shshshsID=4b261b8e572ed58f9bcb29f86d145546_1_1703744380780; areaId=2; 3AB9D23F7A4B3C9B=IQFAUZXF7KNGGA3ZNCLO44HCWIP3IXSVMWTLRQJBM4KPUBKLNUAU57A7NYX7CNYYCHV57B6KY6H3L4WM3BLGRRSLRE; token=b12a5c6c91a4c9fcd1ecd4b144053665,3,946524; __tk=1716e5e1a7f436c84eb1359e87b0a6b6,3,946524; __jda=181111935.16652186012671133573876.1665218601.1703210891.1703744355.27; __jdc=181111935; ipLoc-djd=2-2826-51944-0; __jdb=181111935.7.16652186012671133573876|27.1703744355; shshshfpb=AAlMJGK-MEggRWy0D417H3CHNiiH0MRZnJ1eUfwAAAAA; 3AB9D23F7A4B3CSS=jdd03IQFAUZXF7KNGGA3ZNCLO44HCWIP3IXSVMWTLRQJBM4KPUBKLNUAU57A7NYX7CNYYCHV57B6KY6H3L4WM3BLGRRSLREAAAAMMV4MAVNQAAAAADA6ZCFT373KMMYX; _gia_d=1',
        'Referer': 'https://item.jd.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    }
    num_pages = 5  # 设置要爬取的页数
    output_csv_file = 'jd_comments_2.csv'

    get_jd_comments(url, header, num_pages, output_csv_file)