# OPENVINO TODO
- tool.py to parse wav files & export it to json / npy
- import dataset to model => train it with new_raw
- compare performance raw vs new_raw 

## openvino runtime method
- download model => convert model
- source env variables

## noise cancellation
- very effective => completely wiped bird sound

## packaging command

- activate conda environment

```bash
mo --saved_model_dir <model saved directory (pb and other variable files location)> --model_name <name of the model> --input_shape "[?, 20, 128]"
```
