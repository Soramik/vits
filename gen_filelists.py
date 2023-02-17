# -*- coding: UTF-8 -*-
import argparse
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-I", "--index", default=127, type=int, help="=-1时为单人训练，=0-803时为多人训练，默认为127")
    parser.add_argument("-F", "--filelists", type=str, default="filelists/SoraVoice_filelist.txt", help="文件列表，默认为 filelists/SoraVoice_filelist.txt")
    parser.add_argument("-W", "--wav_place", type=str, default="wav/Sora", help="wav的位置，默认为 wav/Sora")

    args = parser.parse_args()

    with open(args.filelists, mode="r", encoding="utf-8") as rf, \
            open(args.filelists.replace('.txt', '_train.txt'), mode="w", encoding="utf-8") as wf_train, \
            open(args.filelists.replace('.txt', '_val.txt'), mode="w", encoding="utf-8") as wf_val:
        write_train_contents = []
        write_val_contents = []
        contents = rf.readlines()
        for content in contents:
            content_list = content.split("|")
            content_list[0] = args.wav_place + ('/' if args.wav_place[-1] != '/' else '') + content_list[0]
            if args.index != -1:
                content_list.insert(1, f'{args.index}')
            if random.random() < 0.8:
                write_train_contents.append('|'.join(content_list))
            else:
                write_val_contents.append('|'.join(content_list))
        wf_train.writelines(write_train_contents)
        wf_val.writelines(write_val_contents)
