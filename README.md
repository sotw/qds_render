---
title: A python utility for loading 3d file and visualization
date: 2017-03-08 17:00:00
tags: QDS
---
![](http://sotw.servebeer.com:8086/img/nasa3ds.png)

##A python utility for loading 3d file and visualization

Get your copy from

```
git clone https://github.com/sotw/qds_render.git
```

Simply issue install and make sure 

```
~/bin/sh is existed inside your bashrc $PATH variable
```

[refer1](https://gist.github.com/Hodapp87/8874941)

#### Dependency
You will need to make sure your python can import everything.
for example: vtk

#### Note

I noticed that NASA recently release many interesting 3D resource from
[Nasa 3D](https://nasa3d.arc.nasa.gov)

Some of them are 3d models and it's all .3ds file.
After taking time to survey, I found .3ds is also supported by vtk.
Thus I decide to extend [qds_loader_stl](https://github.com/sotw/qds_loader_stla) to support .3ds as well.

Here is what I made.

A infrastructure design makes user can issue 

```
$ qds_render xxx.stl or xxx.3ds
```
from anywhere.

So he/her can put all image file in a folder and use this utility to see the result.

qds_loader_stl will be replaced by this one and if there will be another interesting 3d format I will extend this python tool.

#### First sample : A brain skull (stl)

![](http://sotw.servebeer.com:8086/img/brainSkull.png)

For this sample, it runs well

#### Second sample : Hairy Einstien (stl)

![](http://sotw.servebeer.com:8086/img/hairyEinstien.png)

For this one, I realize that maybe I do need a machine with right graphic card.
Einstien's hair looks bad.

#### Third sample : A space man (3ds)

![](http://sotw.servebeer.com:8086/img/nasa3ds.png)

Salute to the pioneer!


