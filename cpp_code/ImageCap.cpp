#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

class ImageCap
{
    private:
        Mat image;

    public:
        ImageCap(int port)
        {
            capImage(port);
        }

        void capImage(int port)
        {
            VideoCapture cap(port);

            bool capSuccess = cap.read(image);

            if (!capSuccess)
            {
                cout << "Error capturing image" << endl;
            }

            writeImage(image, "capture.jpg");
        }

        void writeImage(Mat image, String filename, String path = "./")
        {
            bool isSuccess = imwrite(path + filename, image);

            if (!isSuccess)
            {
                cout << "Failed to write image" << endl;
            }
        }

        void viewImage()
        {
            String windowName = "Saved Image";

            namedWindow(windowName);
            imshow(windowName, image);
            waitKey(0);
            destroyWindow(windowName);
        }

        Mat getImage()
        {
            return image;
        }

};