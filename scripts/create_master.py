import csv, os, shutil

def create_master(data_path, destination_path, label_file, type):
    os.chdir(data_path)
    file_num = 0
    with open(label_file, "a") as f:
        writer = csv.writer(f)
        for item in os.listdir():
            for file in os.listdir(os.path.abspath(item)):
                fname = str(file_num) + "_{}.jpg".format(type)
                shutil.move(os.getcwd() + "/{}/".format(item) + file, dest_dir + fname)
                writer.writerow([fname, item])
                file_num += 1


#data_path = "/home/nate/Downloads/blood-cells/dataset2-master/dataset2-master/images/TRAIN/"
#dest_dir = "/home/nate/Desktop/school/ml_assignments/final/master_dataset/"
#label_file = "/home/nate/Desktop/school/ml_assignments/final/master_train_label.csv"

#data_path = "/home/nate/Downloads/blood-cells/dataset2-master/dataset2-master/images/TEST/"
#dest_dir = "/home/nate/Desktop/school/ml_assignments/final/test_master_dataset/"
#label_file = "/home/nate/Desktop/school/ml_assignments/final/master_test_label.csv"

data_path = "/home/nate/Downloads/blood-cells/dataset2-master/dataset2-master/images/TEST_SIMPLE/"
dest_dir = "/home/nate/Desktop/school/ml_assignments/final/test_simple_master_dataset/"
label_file = "/home/nate/Desktop/school/ml_assignments/final/test_simple_master_label.csv"
create_master(data_path, dest_dir, label_file, "test_simple")
