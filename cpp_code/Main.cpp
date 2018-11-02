#include <opencv2/opencv.hpp>
#include <iostream>
#include "ImageCap.cpp"
#include "ImageManipulation.cpp"
#include "ImageProcessing.cpp"


int main(int argc, char *argv[])
{
    // ImageCap image = ImageCap(1);
    // image.viewImage();

    ImageManipulation thresh = ImageManipulation(imread("./test_input.jpg"));
    thresh.threshold();
    thresh.canny();
    thresh.viewImage();

    ImageProcessing hough = ImageProcessing(thresh.getMaipulatedImage(), thresh.getOrigionalImage());
    hough.houghTransform();
    hough.viewImage();

    return 0;
}
