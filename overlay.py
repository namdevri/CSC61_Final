import os, cv2
import xml.etree.ElementTree as ET

#slight modification of example in visualize.py
#parameters
#  img=image file path
#  ann=annotation file path

def parse_single(img, ann):
    image = cv2.imread(img)
    tree = ET.parse(ann)
    for elem in tree.iter():
        if 'object' in elem.tag or 'part' in elem.tag:
                for attr in list(elem):
                        if 'name' in attr.tag:
                                name = attr.text
                        if 'bndbox' in attr.tag:
                                for dim in list(attr):
                                        if 'xmin' in dim.tag:
                                                xmin = int(round(float(dim.text)))
                                        if 'ymin' in dim.tag:
                                                ymin = int(round(float(dim.text)))
                                        if 'xmax' in dim.tag:
                                                xmax = int(round(float(dim.text)))
                                        if 'ymax' in dim.tag:
                                                ymax = int(round(float(dim.text)))
                                if name[0] == "R":
                                        cv2.rectangle(image, (xmin, ymin),
                                                                (xmax, ymax), (0, 255, 0), 1)
                                        cv2.putText(image, name, (xmin + 10, ymin + 15),
                                                        cv2.FONT_HERSHEY_SIMPLEX, 1e-3 * image.shape[0], (0, 255, 0), 1)
                                if name[0] == "W":
                                        cv2.rectangle(image, (xmin, ymin),
                                                                (xmax, ymax), (0, 0, 255), 1)
                                        cv2.putText(image, name, (xmin + 10, ymin + 15),
                                                        cv2.FONT_HERSHEY_SIMPLEX, 1e-3 * image.shape[0], (0, 0, 255), 1)
                                if name[0] == "P":
                                        cv2.rectangle(image, (xmin, ymin),
                                                                (xmax, ymax), (255, 0, 0), 1)
                                        cv2.putText(image, name, (xmin + 10, ymin + 15),
                                                        cv2.FONT_HERSHEY_SIMPLEX, 1e-3 * image.shape[0], (255, 0, 0), 1)
    return image



#create a directory containing all images with overlayed annotations
#parameters
#  annotations_dir= directory containing annotations
#  image_dir = directory containing images
#  write_dir = directory to write new images

def overlay_annotations(annotations_dir, image_dir, write_dir):
    #rename each file so we can sort
    for file in os.listdir(annotations_dir):
        os.rename(annotations_dir + file, annotations_dir + file.split("_")[1])
    for file in os.listdir(image_dir):
        os.rename(image_dir + file, image_dir + file.split("_")[1])
    #get list of files
    images = [file for file in os.listdir(image_dir)]
    annotations = [file for file in os.listdir(annotations_dir)]
    #sort files
    images.sort()
    annotations.sort()

    #iterate over annotations and images together
    for ann, img in zip(annotations, images):
        #overlay the border box
        bordered_img = parse_single(image_dir + img, annotations_dir + ann)
        #write to outdir
        cv2.imwrite("{}/{}_annotated.jpg".format(write_dir, img), bordered_img)


#example usage
annotations_dir = "/home/nate/Desktop/school/ml_assignments/final/BCCD_Dataset/BCCD/Annotations/"
image_dir = "/home/nate/Desktop/school/ml_assignments/final/BCCD_Dataset/BCCD/JPEGImages/"
write_dir = "/home/nate/Desktop/school/ml_assignments/final/modified"
overlay_annotations(annotations_dir, image_dir, write_dir)
