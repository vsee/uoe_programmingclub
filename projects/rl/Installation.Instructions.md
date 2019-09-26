1. Set up the virtual python environment

```
pyvenv rlfun # or whatever other name you like
```

2. Activate the virtual environment

```
source rlfun/bin/activate # enter the virtual environment
```

3. Install all dependencies inside the new environment

```
pip install --upgrade pip
pip install gym
pip install jupyter
pip install tensorflow
#pip install vizdoom # Does not work on DICE
```

4. Exit the virtual environment

```
deactivate #exit the virtual environment
```

5. Activate the virtual environment before opening the reinforcement learning notebooks

```
source rlfun/bin/activate
jupyter <anynotebook>
deactivate
```

