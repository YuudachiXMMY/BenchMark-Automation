# -*- coding: utf-8 -*-
import aircv

def matchImg(imgsrc, imgobj, confidence=0.2):
    """
    图片对比识别imgobj在imgsrc上的相对位置（批量识别统一图片中需要的部分）
    :param imgsrc: 原始图片路径(str)
    :param imgobj: 待查找图片路径（模板）(str)
    :param confidence: 识别度（0<confidence<1.0）
    :return: None or dict({'confidence': 相似度(float), 'rectangle': 原始图片上的矩形坐标(tuple), 'result': 中心坐标(tuple)})
    """
    imsrc = aircv.imread(imgsrc)
    imobj = aircv.imread(imgobj)

    match_result = aircv.find_template(imsrc, imobj,
            confidence) # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0]) # 0为高，1为宽

    return match_result

matchImg("TombRaider/tar.png", "TombRaider/start.png")