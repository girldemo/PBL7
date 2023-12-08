from pydub import AudioSegment

# Chuyen ve tan so 16000H va dinh dang .wav
def convert_sample_rate_in_place(file_path, target_sr=16000):
    # Đọc file âm thanh
    audio = AudioSegment.from_file(file_path)

    # Chuyển đổi tần số lấy mẫu
    audio = audio.set_frame_rate(target_sr)

    # Ghi đè vào file ban đầu
    audio.export(file_path, format="wav")

# # Đường dẫn của file âm thanh cần chuyển đổi
# file_path = 'path/to/your/file.wav'

# # Gọi hàm chuyển đổi và ghi đè vào file ban đầu
# convert_sample_rate_in_place(file_path)
