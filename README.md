Image Cropping Program : Data Preprocessing for CNN(Convolution Neural Network)
===

***

1 . Using Language : Python(add PATH)

2 . Version : 3.7

3 . Work in OS : Windows 10 Pro

4 . Working Tool : [JetBrain Pycharm](https://www.jetbrains.com/pycharm/)(Community, 2019.1 , as Virtual Environment)

5 . Operation Time : 6hr

6 . Module & Package in used

    - PIL(Python Image Library)
    - io
    - os
    - cv2(OpenCV, Vision)
    - glob
    - sys
    - platform
    - numpy
7 . Way to install Packages not supported by Python by default(Recommend : Your Python needs to be added to PATH)

    - If your PC has Python2 use command 'pip3'
    1 . PIL
        - pip3 install image   
    2 . Numpy
        - pip3 install numpy
    3 . CV2
        - If only main module : pip3 install opencv-python
        - Use Extra module : pip3 install opencv-contrib-python

8 . Supporting OS : Windows, Linux, Mac OS

9 . Supporting image format : **.jpg**, **.png**
***

## How it Works

1 . Firstly let's say there is one photo for example

![Example](/img/1.jpg)

2 . From Now I will tell  you the process to use this program.(This is only Python Command Version. GUI Version Will update soon)

- First get your image's directory

![ex1](/img/2.jpg)

- Put your directory in to first input line and write down image format you want to crop. You need to write only one type between .jpg & .png. In this example I will use .jpg format.

![ex2](/img/3.jpg)

- Then Program will show you the directory and the list of file name.

![ex3](/img/4.jpg)

- Next enter width height value in pixels to crop image.(Default set as only pixel)

![ex4](/img/5.jpg)

- Next if you need to overlap your photo, enter percentage of overlap degree.

![ex5](/img/7.jpg)

- When you finish these process program will show you the picture's pixel value of width and height, and show the directory that cropped image has been saved.

![ex6](/img/8.jpg)

- When you go to stored directory you can see that the same file was created as the name of the picture you cropped.

![ex7](/img/9.jpg)
![ex8](/img/10.jpg)

        
