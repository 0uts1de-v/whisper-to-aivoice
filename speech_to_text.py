from audio_transcriber import AudioTranscriber
from audio_utils import display_valid_input_devices, get_valid_input_devices

def hoge():
    transcriber = AudioTranscriber()

    valid_devices = get_valid_input_devices()
    print("Valid Input Devices:")
    display_valid_input_devices(valid_devices)

    # 対象のDeviceIndexを入力
    selected_device_index = int(input("Select DeviceIndex: "))

    # 文字起こしを開始
    transcriber.start_transcription(selected_device_index)
