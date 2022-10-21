import shutil
import datetime
import os

def func_arh(destination_folder, arhive_name):  # передаем путь к папке, которую будем архивировать и имя для архива
    folder_with_archive_storage = 'F:\YandexDisk\Save_all'  # Папка, куда архивируем
    filename = arhive_name + '_save_backup_{:%Y_%b_%d_%H-%M}'.format(datetime.datetime.now())  # имя файла архива  с датой и временем
    shutil.make_archive(os.path.join(folder_with_archive_storage, filename), 'zip', destination_folder)  # процесс архивации
    print('Создан архив: ' + filename + '.zip')
# destination_folder = 'C:/Users/Magva/Documents/Hitman Blood Money 2/'  # Папка, которую архивируем

# архивируем сейвы гам, r в начале, чтобы не менять обычные слеши на обратные не было проблем :\ в пути
func_arh(r'C:\Users\Magva\Documents\My Games\Oblivion\Saves', 'Oblivion')
func_arh(r'C:\Users\Magva\Documents\Hitman Blood Money', 'Hitman_Blood_Money')
func_arh(r'C:\Users\Magva\Documents\SpaceRangersHD\Save', 'SpaceRangersHD')
func_arh(r'E:\Games\Minecraft_1.14.4\saves', 'Minecraft')
func_arh(r'C:\ProgramData\Socialclub\RLD!\271590', 'GTAV')
# func_arh('destination_folder', 'arhive_name')



print('Все бекапы проведены успешно =)')
