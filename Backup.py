import os
import time
import zipfile

source = ['d:\\test1', 'd:\\test2'] #получается ток для одного каталога делать архив, нужно чтобы ввел неск.  путей и он на все сделал зип

target_dir = 'd:\\Backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Введите коментарии --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
print('Каталог успешно создан', today)

z = zipfile.ZipFile(target, "w")
for root, dirs, files in os.walk('d:\\test1'):
    for file in files:
        z.write(os.path.join(root, file))
z.close()

if zipfile.is_zipfile(target):
    print('Резервная копия успешна создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')