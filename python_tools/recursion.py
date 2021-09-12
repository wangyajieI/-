# ------------递归拷贝文件，拷贝到一个文件夹或和原有目录树一样拷贝到其他文件夹-----------------
import time
import os
import shutil
import argparse

# 记录拷贝次数
num = 0
copy_file_type = ('.c', '.cpp', '.txt')


def readargs():
    parser = argparse.ArgumentParser(description='Tool for recursion copy a dir to another one.')
    parser.add_argument('-i', '--indir', type=str, required=True, help='recursion input directory')
    parser.add_argument('-o', '--outdir', type=str, default="./recursed_dir", help='recursion output directory')
    args = parser.parse_args()
    return args.indir, args.outdir


def cp(orig, dest):
    '''
    :param type: 拷贝文件
    :param cide: 目标文件（相对路径　）
    :return:
    '''
    global num
    if os.path.isfile(orig) and os.path.basename(orig).endswith(copy_file_type):
        with open(orig, 'rb') as cp:
            rb = cp.read()
            with open(dest, 'wb') as down:
                down.write(rb)
                num += 1
                print('拷贝第%d个' % num)
        print(f"拷贝{orig}>>>>>{dest}")


# 对目录以及目录内文件拷贝和递归创建目录
def cp_mkdir(original, dest):
    """
    :param original: 被拷贝的目录
    :param dest: 拷贝到
    :return:
    """
    # 深度
    # 记录深度
    s = os.listdir(original)

    if not os.path.exists(dest):
        os.mkdir(dest)
    print(f"创建文件{dest}")
    for item in s:
        if '.' in item:
            # 文件名递归拼接
            type_new = original+'/'+item
            mkdir_new = dest+'/'+item
            cp(type_new, mkdir_new)
        else:
            # 目录递归拼接
            type_new = original + '/' + item
            mkdir_new = dest+'/'+item
            cp_mkdir(type_new, mkdir_new)


def copyFile(sourcePath, savePath):
    '''
    not used currently. 递归将文件拷贝到一个文件夹内，没有如上的递归拷贝
    :param sourcePath:
    :param savePath:
    :return:
    '''
    image_end = ('.cpp')
    if not os.path.exists(savePath):
        os.mkdir(savePath)
    for dir_or_file in os.listdir(sourcePath):
        filePath = os.path.join(sourcePath, dir_or_file)
        if os.path.isfile(filePath):  # 判断是否为文件
            # if os.path.splitext(os.path.basename(filePath))[1] in image_end:  # 如果文件是图片，则复制，
            # 如果都是同一种图片类型也可以用这句：if os.path.basename(filePath).endswith('.jpg'):
            if os.path.basename(filePath).endswith(image_end):
                print('this copied file name is ' + os.path.basename(filePath))  # 拷贝文件到自己想要保存的目录下
                shutil.copyfile(filePath, os.path.join(savePath, os.path.basename(filePath)))
            else:
                continue
        elif os.path.isdir(filePath):  # 如果是个dir，则再次调用此函数，传入当前目录，递归处理。
            copyFile(filePath, savePath)
        else:
            print('not file and dir ' + os.path.basename(filePath))


# 文件拷贝入口
if __name__ == '__main__':
    # 记录时间
    down_time = time.time()
    orignal, dest = readargs()
    if not os.path.exists(dest):
        os.mkdir(dest)
    cp_mkdir(orignal, dest)
    up_time = time.time()
    print(up_time - down_time)
