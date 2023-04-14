import os
import clr
import time

def connect_to_editor():
    _editor_dir = os.environ['ProgramW6432'] + '\\AI\\AIVoice\\AIVoiceEditor\\'

    if not os.path.isfile(_editor_dir + 'AI.Talk.Editor.Api.dll'):
        print("A.I.VOICE Editor not found.")
        exit()

    clr.AddReference(_editor_dir + "AI.Talk.Editor.Api")
    from AI.Talk.Editor.Api import TtsControl, HostStatus

    tts_control = TtsControl()

    host_name = tts_control.GetAvailableHostNames()[0]
    tts_control.Initialize(host_name)

    if tts_control.Status == HostStatus.NotRunning:
        tts_control.StartHost()

    tts_control.Connect()
    host_version = tts_control.Version
    print(f"Connected to {host_name} (v{host_version}) .")

    return tts_control


def disconnect_from_editor(tts_control):
    host_name = tts_control.GetAvailableHostNames()[0]
    host_version = tts_control.Version
    tts_control.Disconnect()
    print(f"Disconnected from {host_name} (v{host_version}) .")


def speech(tts_control, text):
    tts_control.Text = text
    play_time = tts_control.GetPlayTime()
    tts_control.Play()
    time.sleep((play_time + 500) / 1000)
