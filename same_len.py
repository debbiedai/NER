import csv
from transformers import AutoTokenizer
import os
import shutil


def preprocess_same_len(max_len, model_name_or_path, read_file, write_file):
    save_data = open(write_file, 'w')
    subword_len_counter = 0

    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
    max_len -= tokenizer.num_special_tokens_to_add()
    
    with open(read_file, encoding="utf-8") as f_p:
        for line in f_p:
            line = line.rstrip()
            # if space, reset subword_len_counter

            if not line or '.xml' in line:
                save_data.write(line + '\n')
                subword_len_counter = 0
                continue

            token = line.split()[0]
            print(tokenizer.tokenize(token)[:])
            current_subwords_len = len(tokenizer.tokenize(token))


            if current_subwords_len == 0:
                continue

            if (subword_len_counter + current_subwords_len) > max_len:
                print("")
                save_data.write('\n')
                save_data.write(line + '\n')
                subword_len_counter = current_subwords_len
                continue

            subword_len_counter += current_subwords_len
            save_data.write(line + '\n')

def creat_train_data(train_fold_list, val_fold, test_fold, data_path, save_path):
    save_path_dir = os.path.join(save_path, "v"+str(val_fold)+"_t"+str(test_fold))
    if not os.path.exists(save_path_dir):
        os.mkdir(save_path_dir)
    val_data = os.path.join(data_path, "fold_"+str(val_fold)+".txt")
    test_data = os.path.join(data_path, "fold_"+str(test_fold)+".txt")
    devel = os.path.join(save_path_dir, "devel.txt")
    test = os.path.join(save_path_dir, "test.txt")
    shutil.copyfile(val_data, devel)
    shutil.copyfile(test_data, test)


    f = open(os.path.join(save_path_dir, "train_dev.txt"), 'w')
    for i in train_fold_list:
        dataset = data_path + "/fold_" + str(i) + ".txt"
        with open(dataset, "rt") as f_p:
            for line in f_p:
                line = line.rstrip()
                f.write(line + '\n')
        f.write('\n')

if __name__ == '__main__':
    # the path of 10 folds no_txt_name file, def [preprocess_same_len] truncate each setence to same length
    files = os.listdir('./split_fold_test/txt_name')
    for file in files:
        if file.endswith('.txt'):
            path = os.path.join('./split_fold_test/txt_name', file)
            preprocess_same_len(50, 'dmis-lab/biobert-base-cased-v1.1', path, './split_fold_test/txt_name/same_len/'+file)

    # create train_dev.txt, devel.txt, test.txt 
    val_list = [0,1,2,3,4,5,6,7,8,9]
    test_list = [1,2,3,4,5,6,7,8,9,0]
    for i in range(len(test_list)):
        val_num = val_list[i]
        test_num = test_list[i]
        train_num = [i for i in range(10)]
        train_num.remove(val_num)
        train_num.remove(test_num)
        print('train_num', train_num)
        creat_train_data(train_num, val_num, test_num, './split_fold_test/no_txt_name/same_len', './split_fold_test/no_txt_name/same_len')