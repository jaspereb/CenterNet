# Load the produced JSON results file, turn this into a txt file that can be used with the VOC eval script in matlab
# The JSON file is in the COCO results format, so the bounding boxes are [top left corner x, top left corner y, width, height]

import json
import os


dirPath = '/home/jasper/git/CEIG/CenterNet/results/CenterNet-104-DayTransferPlums/180000/test'
filePath = os.path.join(dirPath, 'results.json')
outFile = os.path.join(dirPath, 'detections.txt')

print("Loading results file {}".format(filePath))
print("And saving results file {}".format(outFile))

with open(filePath, 'r') as f:
    data = json.load(f)

with open(outFile, 'w') as f:
    for i in range(0, len(data)):
        datai = data[i]

        bb = datai.get('bbox')
        xmin = int(bb[0])
        ymin = int(bb[1])
        xmax = int(bb[0] + bb[2])
        ymax = int(bb[1] + bb[3])

        if(ymax > 480 or xmax > 640 or ymin < 0 or xmin < 0):
            print("Got detection outside image!!!")
            continue

        if(datai.get('score') < 0.01):
            continue

        imgName = "{:04d}".format(datai.get('image_id'))
        dataLine = imgName + ' ' + str(datai.get('score')) + ' ' + str(xmin) + ' ' + str(ymin) + ' ' + str(xmax) + ' ' + str(ymax) + '\n'
        # print(dataLine)

        f.write(dataLine)

print("Done~!")
