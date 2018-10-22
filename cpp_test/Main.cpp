#include <opencv2/opencv.hpp>
#include <iostream>
#include "ImageCap.cpp"
#include "ImageManipulation.cpp"


int main(int argc, char *argv[])
{
    ImageCap image = ImageCap(0);
    image.viewImage();


    return 0;
}
