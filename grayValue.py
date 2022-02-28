import cv2,os
import numpy as np
def calImage(pathes):
    file_names = []
    avg_grayes = []
    for path in pathes:
        img_path_code = np.fromfile(path, dtype=np.uint8)  # 含有中文路径时
        img = cv2.imdecode(img_path_code, 0)
        name = os.path.split(path)[-1]
        avg_val = round(np.mean(img),3)
        file_names.append(name)
        avg_grayes.append(avg_val)
    return file_names,avg_grayes