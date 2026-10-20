import os
import shutil

def organize_folder(folder_path):
    FILE_CATEGORIES = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx'],
        'Spreadsheets': ['.xlsx', '.xls', '.csv'],
        'Archives': ['.zip', '.rar', '.7z', '.tar'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Audio': ['.mp3', '.wav']
    }

    if not os.path.exists(folder_path):
        print("[!] please check")
        return

    print(f"[*] جاري تنظيم الملفات داخل: {folder_path}")

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                category_dir = os.path.join(folder_path, category)
                os.makedirs(category_dir, exist_ok=True)
                
                shutil.move(file_path, os.path.join(category_dir, filename))
                print(f"[+] تم نقل: {filename} -> {category}/")
                moved = True
                break

        if not moved and file_ext != '':
            others_dir = os.path.join(folder_path, 'Others')
            os.makedirs(others_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(others_dir, filename))
            print(f"[+] تم نقل: {filename} -> Others/")

    print("[+] اكتمل تنظيم الفولدر بنجاح!")

if __name__ == "__main__":
    target_dir = input("put the path: ").strip('"')
    organize_folder(target_dir)