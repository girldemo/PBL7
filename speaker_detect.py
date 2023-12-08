import random

import numpy as np
import wav_handle as wh
from deep_speaker.audio import read_mfcc
from deep_speaker.batcher import sample_from_mfcc
from deep_speaker.constants import SAMPLE_RATE, NUM_FRAMES
from deep_speaker.conv_models import DeepSpeakerModel
from deep_speaker.test import batch_cosine_similarity

# Reproducible results.
np.random.seed(123)
random.seed(123)

# Define the model here.
model = DeepSpeakerModel()
model.m.load_weights('model_checkpoint_265.h5', by_name=True)

audio_path = "test_wavfile\Phuc2.wav"
file_path = "audio_data_list.txt"

# Tạo danh sách để lưu thông tin
audio_list = []

# Đọc dữ liệu từ tệp văn bản
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        # Tách thông tin sử dụng dấu cách hoặc tab
        parts = line.strip().split()
        
        # Lấy thông tin từ các phần tách
        file_name = parts[0]
        file_path = parts[1]
        person_name = " ".join(parts[2:])

        # Thêm thông tin vào danh sách
        audio_list.append({"file_name": file_name, "file_path": file_path, "person_name": person_name})

wh.convert_sample_rate_in_place(audio_path) #convert to 16000Hz sample rate
mfcc_input = sample_from_mfcc(read_mfcc(audio_path, SAMPLE_RATE), NUM_FRAMES)
predict_input = model.m.predict(np.expand_dims(mfcc_input, axis=0))

output_value = []
for audio_info in audio_list:
    mfcc_data = sample_from_mfcc(read_mfcc(audio_info['file_path'], SAMPLE_RATE), NUM_FRAMES)
    predict_data = model.m.predict(np.expand_dims(mfcc_data, axis=0))
    print(batch_cosine_similarity(predict_input, predict_data))
    output_value.append(batch_cosine_similarity(predict_input, predict_data))
max_output_value_index = output_value.index(max(output_value))
print(audio_list[max_output_value_index]['person_name'])



