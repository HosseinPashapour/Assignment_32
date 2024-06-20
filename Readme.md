# Assigment 32


# 1.Convolution_2D
+ In this project, applied 5 different kernels on input image to see the difference of kernels. here is list of kernels:

    ```
    # 1. Edge detection filter
        kernel = np.array([[-1 , -1 , -1],
                           [-1 ,  8 , -1],
                           [-1 , -1 , -1]])

        # 2. Sharpening filter
        kernel = np.array([[0  , -1 ,  0],
                           [-1 ,  5 , -1],
                           [0  , -1 ,  0]])
 
        # 3. Emboss filter
        kernel = np.array([[-2 , -1 ,  0],
                           [-1 ,  1 ,  1],
                           [0  ,  1 ,  2]])

        # 4. Identity filter
        kernel = np.array([[0  ,  0 ,  0],
                           [0  ,  1 ,  0],
                           [0  ,  0 ,  0]])

        # 5. Your filter
        kernel = # what ever you want```

## How to Install
Run following command:
```
pip install -r requirments.txt
```


## How to Run
Execute this command in terminal:

```
python 1_Convolution_2D.ipynb
```
## Input

![input](https://github.com/HosseinPashapour/Assignment_32/blob/main/Input/Sheep.jpeg)


# Results
 ## Edge detection filter
![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/Edges_Sheep.jpeg)
## Sharpening filter
![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/Sharped_Sheep.jpeg)
## Emboss filter
![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/Embossed_Sheep.jpeg)
## Identity filter
![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/Identity_Sheep.jpeg)
## Edge_image_Sheep
![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/Edge_image_Sheep.jpeg)

------------------------------------------------------

# 2.Average Filter
+ In this project, applied median kernels in different size (3,5,7,9) on input image to reduce the noise of them, also median filter applied twice if needed.

## How to Install
Run following command:
```
pip install -r requirments.txt
```

## How to Run
Execute this command in terminal :
```
python 2_Average_Filter.ipynb
```

# Results

![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/Magic.png)

-----------------------------------------
# 3.Median_Filter
+ In these projects we use median filter to remove salt-and-pepper noise on some images.
there is a function in python for this operation call medianBlur.

## How to Install
Run following command:
```
pip install -r requirments.txt
```

## How to Run
Execute this command in terminal :
```
python 3_Median_Filter
```

# Results
## Before
![Input](https://github.com/HosseinPashapour/Assignment_32/blob/main/Input/body.png)
## After
![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/result_Body.png)
## Before
![Input](https://github.com/HosseinPashapour/Assignment_32/blob/main/Input/elec.png)
## After
![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/result_Elec.png)
## Before
![Input](https://github.com/HosseinPashapour/Assignment_32/blob/main/Input/circle.png)
## After
![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/result_Circle.png)
## Before
![Input](https://github.com/HosseinPashapour/Assignment_32/blob/main/Input/party.png)
## After
![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/result_Party.png)
## Before
![Input](https://github.com/HosseinPashapour/Assignment_32/blob/main/Input/woman.png)
## After
![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/result_Woman.png)
## Before
![Input](https://github.com/HosseinPashapour/Assignment_32/blob/main/Input/things.png)
## After
![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/result_Things.png)

-----------------------------------------
# 4.Histogram

+ Its an operation in image processing to enhance contrast of an image.
if the histogram of your image focus in black area or white area, then equalizeHist function can solve your problem.
But if your histograms picture is not focus in black or white area you van use CLAHE to solve your problem and 
don't lose details too.

## How to Install
Run following command:
```
pip install -r requirments.txt
```

## How to Run
Execute this command in terminal :
```
python 4_Histogram_Equalize
```


## Results
![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/Equalize1.png)
![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/Equalize2.png)
![output](https://github.com/HosseinPashapour/Assignment_32/blob/main/Output/Equalize_clahe.png)

-----------------------------------------
