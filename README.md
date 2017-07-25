# MyoGrapher
The graph plotter from dzhu's myo-raw refactored into a class to be used independently

```python
drawLines = True & curve = False
```
![](https://github.com/RaquenaTeam/MyoGrapher/raw/master/pictures/MyoGrapher1.png)

```python
drawLines = False
```
![](https://github.com/RaquenaTeam/MyoGrapher/raw/master/pictures/MyoGrapher2.png)

# How to install
`python setup.py install`
and if you have to install it as root use
`sudo -H python setup.py install` if you don't use the `-H` flag you'll only be able to import it as root.

# How to use
```python
from MyoGrapher import MyoGrapher
mg = MyoGrapher()
#for generic use
mg.plot(values, drawLines=False, curve=True)
#for myo use
mg.emg_plot(values, drawLines=False, curve=True)
```
You can either use a list of floating numbers as values, or even a single floating number value. MyoGrapher splits the screen accordingly.
