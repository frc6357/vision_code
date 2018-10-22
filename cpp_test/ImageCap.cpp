#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

class ImageCap
{
    private:
        Mat frame;

    public:
        ImageCap(int port)
        {
            capImage(port);
        }

        void capImage(int port)
        {
            VideoCapture cap(port);

            bool capSuccess = cap.read(frame);

            if (!capSuccess)
            {
                cout << "Error capturing image" << endl;
            }

            writeImage(frame);
        }

        void writeImage(Mat image)
        {
            bool isSuccess = imwrite("./capture.jpg", image);

            if (!isSuccess)
            {
                cout << "Failed to write image" << endl;
            }
        }

        void viewImage()
        {
            String windowName = "Saved Image";

            namedWindow(windowName);
            imshow(windowName, frame);
            waitKey(0);
            destroyWindow(windowName);
        }

        Mat getImage()
        {
            return frame;
        }

};