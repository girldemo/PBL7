import os

# Đường dẫn đến thư mục chứa các tệp âm thanh
audio_directory = "data_audio"

# Tạo danh sách để lưu thông tin về tên và đường dẫn
audio_list = []

# Lặp qua các tệp trong thư mục
for root, dirs, files in os.walk(audio_directory):
    for file in files:
        # Đường dẫn đầy đủ đến tệp âm thanh
        file_path = os.path.join(root, file)
        
        # Tên tệp âm thanh
        file_name = os.path.basename(file_path)
        
        # Thêm thông tin vào danh sách
        audio_list.append({"file_name": file_name, "file_path": file_path})

# Lưu thông tin vào tệp văn bản
output_file_path = "audio_data_list.txt"

with open(output_file_path, "w", encoding="utf-8") as output_file:
    for audio_info in audio_list:
        output_file.write(f"{audio_info['file_name']}\t")
        output_file.write(f"{audio_info['file_path']}\n")
print(f"Thông tin đã được lưu vào tệp: {output_file_path}")
