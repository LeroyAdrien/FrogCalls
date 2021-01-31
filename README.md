
# FrogCalls
### :frog: *Can we infer the genus of frogs from their call ?* :frog: :ear:


This project relies on the [Anuran Calls (MFCCs) Data Set](https://archive.ics.uci.edu/ml/datasets/Anuran+Calls+%28MFCCs%29) to predict genus from frog calls.

## Files

* Data :  ```Anuran_Calls/```
* Notebooks :  ```notebooks/```
* references ```references/```
* virtual environment : ```env_frog/```

> **Note:** Repository is still under construction.

## How to use env

**Set new source**

```bash
source FrogCalls/env_frog/bin/activate
```

**Check that python is now 3.8**
```bash
python3 --version 
```

**Add env to Jupyter Notebooks**

```bash
cd FrogCalls/
python3 -m ipykernel install --name=env_frog
```

**Change the kernel in Jupyter notebook to be env_frog**


![Change kernel](/images/tuto1.png)


**Check that your kernel has successfully changed**

![Change kernel](/images/tuto2.png)

you can also run ```pip3 list```to see if all the packages are here