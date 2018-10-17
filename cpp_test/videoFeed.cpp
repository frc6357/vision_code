
#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char *argv[])
{
    //open the video file for reading
    VideoCapture cap(0);

    // if not success, exit program
    if (cap.isOpened() == false)
    {
        cout << "Cannot open the video file" << endl;
        cin.get(); //wait for any key press
        return -1;
    }

    //Define names of the window
    String windowName = "Video Feed";

    // Create a window with above names
    namedWindow(windowName, WINDOW_NORMAL);

    while (true)
    {
        Mat frame;
        bool bSuccess = cap.read(frame); // read a new frame from video
        if (bSuccess == false)
        {
            cout << "Found the end of the video" << endl;
            break;
        }

        //show the frames in the created windows
        imshow(windowName, frame);

        //wait for for 10 ms until any key is pressed.
        //If the 'Esc' key is pressed, break the while loop.
        //If the any other key is pressed, continue the loop
        //If any key is not pressed withing 10 ms, continue the loop
        if (waitKey(10) == 27)
        {
            cout << "Esc key is pressed by user. Stoppig the video" << endl;
            break;
        }
    }

    return 0;
}