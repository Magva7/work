import shutil
import datetime
import os


def func_arh(destination_folder, arhive_name):  # source folder to archive
    folder_with_archive_storage = r'F:\YandexDisk\Save_all'  # archive folder
    filename = arhive_name + '_save_backup_{:%Y_%b_%d_%H-%M}'.format(
        datetime.datetime.now())  # file name and date with time
    shutil.make_archive(os.path.join(folder_with_archive_storage, filename),
                        'zip', destination_folder)  # archive process
    print('Создан архив: ' + filename + '.zip')


# r for no change \ to /
func_arh(r'C:\Users\Magva\Documents\My Games\Oblivion\Saves', 'Oblivion')
func_arh(r'C:\Users\Magva\Documents\Hitman Blood Money', 'Hitman_Blood_Money')
func_arh(r'C:\Users\Magva\Documents\SpaceRangersHD\Save', 'SpaceRangersHD')
func_arh(r'E:\Games\Minecraft_1.14.4\saves', 'Minecraft')
func_arh(r'C:\ProgramData\Socialclub\RLD!\271590', 'GTAV')
# func_arh('destination_folder', 'arhive_name')

print('Все бекапы проведены успешно =)')
