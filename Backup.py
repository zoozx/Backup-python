import os
import time
import zipfile

#source = ['d:\\test1', 'd:\\test2'] #получается ток для одного каталога делать архив, нужно чтобы ввел неск.  путей и он на все сделал зип
forzip = input('Укажите путь архивируемой папки в формате d:\\Мои_аудиозаписи --> ') #могу только 1 папку за раз архивировать
target_dir =input('Укажите путь для бэкапа, по умолчанию - d:\\Backup --> ')         #путь для сохранения архива

if len(target_dir) == 0:                                                             #проверка ввел ли пользователь что то, если нет то каталог по умолчанию
    target_dir = ('d:\\Backup')
else:
    target_dir = target_dir.replace()

today = target_dir + os.sep + time.strftime('%Y%m%d')                                #названике для католого кажддневного

now = time.strftime('%H%M%S')                                                        #название для архива посекудного

comment = input('Введите коментарии --> ')                                           #возможность добавить комментарии к названию архива
if len(comment) == 0:                                                                #проверка ввел ли пользователь коммент
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):                                                        #проверка создан ли уже сегодняшний катало или нет и его создание
    os.mkdir(today)
print('Каталог успешно создан', today)
print('Идет архивация... ')

z = zipfile.ZipFile(target, "w")                                                     #собственно сама архивация выбранного каталога и всех папко и файлов внутри
for root, dirs, files in os.walk(forzip):
    for file in files:
        z.write(os.path.join(root, file))
z.close()

if zipfile.is_zipfile(target):                                                       #проверка создался ли архив в каталоге и информирование об усапехе или фейле
    print('Резервная копия успешна создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
