# WHISPER TO AIVOICE
Speech to Text to Speech.

# Usage
```sh
$ python -m venv .venv
$ .venv/Scripts/activate
$ pip install -r ./requirements.txt
$ python ./main.py
```
Probably you need to copy `cublas64_11.dll cublasLt64_11.dll cudnn_cnn_infer64_8.dll cudnn_ops_infer64_8.dll zlibwapi.dll` to `.venv/Lib/site-packages/ctranslate2/`