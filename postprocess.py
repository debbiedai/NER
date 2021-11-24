import os
from collections import defaultdict
import numpy as np

# add text name in test_predictions.txt 
def add_pred_name(val_num, test_num, text_name_dir, pred_dir, save_path):
    # val_num = 0
    # test_num = 1
    txt_name_file = os.path.join(text_name_dir, "fold_" + str(test_num) + ".txt")
    pred_file = os.path.join(pred_dir, 'test_predictions_v' + str(val_num) + '_t' + str(test_num) + '.txt')

    if not os.path.exists(save_path):
        os.mkdir(save_path)
    save_file = open(os.path.join(save_path, "add_pred_name_v" + str(val_num) + '_t' + str(test_num) + ".txt"), 'w')

    dict_ = {}
    count = 0
    tmp_name = '123'
    count_txt = 0
    with open(txt_name_file, encoding="utf-8") as f_p:
        for line in f_p:
            if '.xml' in line:
                count_txt += 1           
                txt_name = str(line.split("\\")[0])
                print(txt_name, count_txt)
                
                if txt_name != tmp_name:
                    dict_[tmp_name] = count
                    dict_[txt_name] = 0
                    tmp_name = txt_name
                    # count = 0
                continue   
            count += 1
        dict_[txt_name] = count
            

    del dict_['123']        
    print(dict_)
    print(len(dict_))    

    f = open(pred_file, 'r')
    lines = f.readlines()

    tmp_v = 0
    for k, v in dict_.items():
        print(k)
        save_file.write(k)
        for i, line in enumerate(lines[tmp_v: v]):
            save_file.write(line)
        tmp_v = v

# extract the word of gene name by model prediction
def postprocess(name, add_pred_name_path, save_path):
    # name = 'v0_t1' means validation data is fold0, test data is fold1
    dataset = os.path.join(add_pred_name_path, "add_pred_name_" + str(name) + ".txt" )
    pred = defaultdict(list)
    count = 0
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    save_file = os.path.join(save_path, 'pred_' + str(name) + '.txt')
    with open(dataset, encoding="utf-8") as f_p:
        for line in f_p:
            line = line.rstrip()
            count += 1
            if '.xml' in line:
                count = 0
                text_name = line
                continue  
            if not line:
                count = 0
                continue   

            token = line.split()[0]
            tag = line.split()[1]
            if tag == "B" or tag == "I":
                pred[text_name].append((tag, count, token ))
                
    # print(pred)
    save_list = []
    for k, v in pred.items():
        print('text_name:', k)
        with open(save_file, 'a') as f:
            f.write(str(k) + '\n')
        find = []
        tmp_tag, tmp_count, tmp_word = '', 0, ''
        for n, i in enumerate(v):
            (tag, count, word) = i
            if count == tmp_count + 1:
                word = tmp_word + ' ' + word
                tmp_word, tmp_count, tmp_tag = word, count, tag
                if n == len(v)-1:
                    find.append(tmp_word[0])
                continue
            if count != tmp_count + 1:
                find.append(tmp_word[0])
            if n == len(v)-1:
                find.append(word[0])
            tmp_tag, tmp_count, tmp_word = tag, count, word
        
        print(find[1:])

        with open(save_file, 'a') as f:
            genes = ", ".join(find[1:])
            f.write(genes+'\n')



if __name__ == '__main__':
    # val_num = 0, test_num = 1
    add_pred_name(0, 1, './example_data/preprocessed/name/same_len/', './example_data/pred/biobert_output/', './example_data/pred/add_pred_name/')
    # name = 'v0_t1'
    postprocess('v0_t1', './example_data/pred/add_pred_name/', './example_data/result/')
