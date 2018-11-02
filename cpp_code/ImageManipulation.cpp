#include <iostream>
#include <opencv2/opencv.hpp>
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

using namespace cv;
using namespace std;

class ImageManipulation
{
    private:
        Mat origImage;
        Mat manipImage;

        // Hue
        const int iLowH = 64;
        const int iHighH = 84;

        // Saturation
        const int iLowS = 90;
        const int iHighS = 255;

        // Value
        const int iLowV = 20;
        const int iHighV = 255;

    public:
        ImageManipulation(Mat frame)
        {
            origImage = frame;

            // Create blank image with the same size as the camera image
            manipImage = Mat::zeros(origImage.size(), CV_8UC3);
        }

        void threshold()
        {
            Mat imgHSV;
            int width = 10;
            int height = 10;


            cvtColor(origImage, imgHSV, COLOR_BGR2HSV);

            inRange(imgHSV, Scalar(iLowH, iLowS, iLowV), Scalar(iHighH, iHighS, iHighV), manipImage);

            //morphological opening (remove small objects from the foreground
            erode(manipImage, manipImage, getStructuringElement(MORPH_ELLIPSE, Size(width, height)));
            dilate(manipImage, manipImage, getStructuringElement(MORPH_ELLIPSE, Size(width, height)));

            //morphological closing (fill small holes in the foreground)
            dilate(manipImage, manipImage, getStructuringElement(MORPH_ELLIPSE, Size(width, height)));
            erode(manipImage, manipImage, getStructuringElement(MORPH_ELLIPSE, Size(width, height)));
        }

        void canny()
        {
            Canny(manipImage, manipImage, 100, 150);
        }

        void viewImage()
        {
            String windowName = "Changed Image";

            namedWindow(windowName);
            imshow(windowName, manipImage);
            waitKey(0);
            destroyWindow(windowName);
        }

        Mat getOrigionalImage()
        {
            return origImage;
        }

        Mat getMaipulatedImage()
        {
            return manipImage;
        }
};