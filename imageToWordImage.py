# import osmnx as ox
# bounds = [31.2433, 30.0596, 105.3520, 103.1960]
# north, south, east, west = bounds[0], bounds[1], bounds[2], bounds[3]
# G = ox.graph_from_bbox(north, south, east, west, network_type='drive')
# ox.save_graphml(G,'chengdu.graphml')
"""
author:呼噜呼噜~
date: 2021年09月20日
"""
# import sys
from PIL import Image, ImageDraw, ImageFont

origin_name=r"C:\Users\Administrator\Desktop\H`JU(GZAGM~UT[5LORM~P$R.jpg"#原图片名
dst_name='output.jpg'#目标图片名


CHILD_W = CHILD_H = 16
txt = '要替换的文字'
font = ImageFont.truetype(r"C:\Windows\Fonts\AdobeHeitiStd-Regular.otf", CHILD_W)  # 字体及大小

if __name__ == '__main__':
    imgSrc = Image.open(origin_name)  # 打开原图像
    w, h = imgSrc.size  # 原图像宽高

    imageChild = Image.new("RGB", (CHILD_W, CHILD_H))  # 新建子图
    imageDst = Image.new("RGB", (CHILD_W * w, CHILD_H * h))  # 新建子图

    textW, textH = font.getsize("迷")  # 取单个文字的宽高信息
    offsetX = (CHILD_W - textW) >> 1  # 居中
    offsetY = (CHILD_H - textH) >> 1

    charIndex = 0  # 记录文字下标
    draw = ImageDraw.Draw(imageChild)  # 取最小绘图对象，用于绘制文字

    for y in range(h):
        for x in range(w):
            draw.rectangle((0, 0, CHILD_W, CHILD_H), fill="lightgray")

            draw.text((offsetX, offsetY), txt[charIndex], font=font, fill=imgSrc.getpixel((x, y)))
            imageDst.paste(imageChild,(x*CHILD_W,y*CHILD_H) )

            charIndex=(charIndex+1)%len(txt)

    imageDst.save(dst_name)
