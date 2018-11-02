#include <iostream>
#include <opencv2/opencv.hpp>
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

using namespace cv;
using namespace std;

class ImageProcessing
{
    private:
        Mat manipImage;
        Mat origImage;

    public:
        ImageProcessing(Mat manip, Mat orig)
        {
            manipImage = manip;
            origImage = orig;
        }

        void houghTransform()
        {
            vector<Vec2f> lines;
            HoughLines(manipImage, lines, 1, CV_PI/180, 100);

            for(size_t i = 0; i < lines.size(); i++)
            {
              float rho = lines[i][0], theta = lines[i][1];
              Point pt1, pt2;
              double a = cos(theta), b = sin(theta);
              double x0 = a*rho, y0 = b*rho;
              pt1.x = cvRound(x0 + 1000*(-b));
              pt1.y = cvRound(y0 + 1000*(a));
              pt2.x = cvRound(x0 - 1000*(-b));
              pt2.y = cvRound(y0 - 1000*(a));
              line(origImage, pt1, pt2, Scalar(0, 0, 255), 2, CV_AA);
            }
        }

        void pHoughTransform()
        {
            vector<Vec4i> lines;
            HoughLinesP(manipImage, lines, 1, CV_PI/180, 50, 50, 10);

            for(size_t i = 0; i < lines.size(); i++)
            {
                Vec4i l = lines[i];
                line(origImage, Point(l[0], l[1]), Point(l[2], l[3]), Scalar(0, 0, 255), 3, CV_AA);
            }
        }

        void viewImage()
        {
            String windowName = "Hough";

            namedWindow(windowName);
            imshow(windowName, origImage);
            waitKey(0);
            destroyWindow(windowName);
        }
};