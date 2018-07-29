import os
import shutil

tar_path='C:\\Users\\dyk\\Desktop\\share\\trian_pic\\lianjia'
save_path='C:\\Users\\dyk\\Desktop\\share\\trian_pic\\lianjiaxml'

for i in os.listdir(tar_path):
    shutil.copy('C:\\Users\\dyk\\Desktop\\share\\trian_pic\\2.xml',
                os.path.join(save_path,os.path.splitext(i)[0]+'.xml')
                )

print('done!')