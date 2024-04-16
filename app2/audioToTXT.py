import faster_whisper
import os
model_size = "large-v3"

class Translate:
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def dir_node(self):
        model = faster_whisper.WhisperModel(model_size, device="cpu", compute_type="int8")
        for root, dirs, files in os.walk(self.input):
            for file_name in files:
                if file_name.endswith(('.ogg', '.wav', '.mp3')):
                    print(file_name)
                    audio_file_path = os.path.join(root, file_name)
                    segments, info = model.transcribe(audio_file_path, beam_size=5)
                    output_file_name = os.path.splitext(file_name)[0] + ".txt"
                    output_file_path = os.path.join(self.output, output_file_name)
                    with open(output_file_path, 'w') as output_file:
                        for segment in segments:
                            output_file.write(segment.text)


