import subprocess
import os
import shutil

def exists(path):
    return os.path.exists(path)

game_number = 281990
game_name = "Stellaris"

current_dir = os.getcwd()
steamdownload = os.path.join(current_dir, "steamdownload")
game_mods_location = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents', 'Paradox Interactive', game_name, 'mod')
mods_folder_path = os.path.join(steamdownload, "steamapps", "workshop", "content", f"{game_number}")


with open("modlist.txt", 'r', encoding='utf-8-sig') as modlist:
    mods = [line.strip() for line in modlist.readlines() if line.strip() and not line.strip().startswith('#')]


for mod in mods:
    print("downloading ", mod)
    subprocess.run(["./steamcmd/steamcmd.exe" ,
                    "+force_install_dir", steamdownload,
                    "+login", "anonymous",  
                    "+workshop_download_item", f"{game_number}", f"{mod}",
                    "+quit"])

print("Mods downloaded")

for mod in mods:
    print("installing ", mod)
    mod_path = os.path.join(mods_folder_path, mod)
    new_mod_path = os.path.join(game_mods_location, mod)
    shutil.copytree(mod_path, new_mod_path, dirs_exist_ok = True)
    descriptor_path = os.path.join(new_mod_path, "descriptor.mod")
    
    if os.path.exists(descriptor_path):
        with open(descriptor_path, "r", encoding='utf-8-sig') as descriptor_file:
            lines = descriptor_file.readlines()
    else:
        lines = []

    path_line = f'\npath="{new_mod_path.replace(os.sep, '/')}"\n'
    path_updated = False
    for i, line in enumerate(lines):
        lines[i] = line.strip()
        if line.startswith("path="):
            lines[i] = path_line
            path_updated = True
            break
    if not path_updated:
        lines.append(path_line)

    mod_descriptor_new_path = os.path.join(game_mods_location, f"{mod}.mod")
    with open(mod_descriptor_new_path, "w", encoding='utf-8-sig') as descriptor_file:
        descriptor_file.writelines(lines)
    
print("Mods installed")
    # shutil.copy2(descriptor_path, mod_descriptor_new_path)
