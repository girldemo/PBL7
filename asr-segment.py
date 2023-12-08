import whisper
from pyannote.audio import Pipeline
from pyannote_whisper.utils import diarize_text
import torchaudio

path_file = "test.wav"
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.0",
                                    use_auth_token="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")
model = whisper.load_model("base")
asr_result = model.transcribe(path_file)
waveform, sample_rate = torchaudio.load(path_file)
diarization_result = pipeline({"waveform": waveform, "sample_rate": sample_rate})
final_result = diarize_text(asr_result, diarization_result)

for seg, spk, sent in final_result:
    line = f'{seg.start:.2f} {seg.end:.2f} {spk} {sent}'
    print(line)