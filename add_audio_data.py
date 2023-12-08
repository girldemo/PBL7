def add_wav_info_to_txt(txt_file_path, wav_file_name, wav_file_path, speaker_name):
    with open(txt_file_path, 'a') as txt_file:
        # Thêm thông tin mới vào cuối tệp
        new_line = f"\n{wav_file_name}\t{wav_file_path}\t{speaker_name}"
        txt_file.write(new_line)

# Thêm thông tin cho một file WAV mới
add_wav_info_to_txt('audio_data_list.txt', 'Phuc_data', 'data_audio\Phuc_data.wav', 'Phuc')
