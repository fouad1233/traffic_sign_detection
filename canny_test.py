{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "usage: ipykernel_launcher.py [-h] [--input INPUT]\n",
      "ipykernel_launcher.py: error: unrecognized arguments: --f=/Users/fuad/Library/Jupyter/runtime/kernel-v3526778a0a80daa82e48436705993f1ff3d57355d.json\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "2",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 2\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/fuad/Library/Python/3.11/lib/python/site-packages/IPython/core/interactiveshell.py:3585: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from __future__ import print_function\n",
    "import cv2 as cv\n",
    "import argparse\n",
    "max_lowThreshold = 100\n",
    "window_name = 'Edge Map'\n",
    "title_trackbar = 'Min Threshold:'\n",
    "ratio = 3\n",
    "kernel_size = 3\n",
    "def CannyThreshold(val):\n",
    "    low_threshold = val\n",
    "    img_blur = cv.blur(src_gray, (3,3))\n",
    "    detected_edges = cv.Canny(img_blur, low_threshold, low_threshold*ratio, kernel_size)\n",
    "    mask = detected_edges != 0\n",
    "    dst = src * (mask[:,:,None].astype(src.dtype))\n",
    "    cv.imshow(window_name, dst)\n",
    "parser = argparse.ArgumentParser(description='Code for Canny Edge Detector tutorial.')\n",
    "parser.add_argument('--input', help='Path to input image.', default='fruits.jpg')\n",
    "args = parser.parse_args()\n",
    "src = cv.imread(cv.samples.findFile(args.input))\n",
    "if src is None:\n",
    "    print('Could not open or find the image: ', args.input)\n",
    "    exit(0)\n",
    "src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)\n",
    "cv.namedWindow(window_name)\n",
    "cv.createTrackbar(title_trackbar, window_name , 0, max_lowThreshold, CannyThreshold)\n",
    "CannyThreshold(0)\n",
    "cv.waitKey()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
