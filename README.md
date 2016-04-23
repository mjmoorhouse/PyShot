# PyShot

## Introduction, Background

The repo relates to a fantasy / demonstration of video and audio processing modules in Python.  The fantasy is that one might use this in some sort of 'Laser Targeting' setup to improve sporting performance.  In goals it mimics commercial system such as those sold by [SCATT](http://scatt.com).
_*Note:* No affiliation or endorsement in either direction implied or stated to any other system commericial or otherwise.  The code base and concepts used for this repo were created without access to any priveleged information or even access to any commercial system_.

## Technical Summary

This repo demonstrates some of the features of the [SimpleCV](http://simplecv.org/) Python module (a simplified binding to the [OpenCV](http://opencv.org/) package) and concepts in the field of vision analysis, specifically the detection of 'registration marks' on a sheet of paper, transformation of these into a plane with truely orthogonal dimensions and the tracking a laser spot around this.
Also included in this repo is the use of the [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) module for detection of 'taps' using a standard teleconferencing headset microphone plugged into a PC's jack socket.  This is a modified version of a classical solution to this problem taken from the pages of Stack Overflow.
The presentation gives demonstrates an idealised physical setup of the hardware equipment used (WebCam, Headset, Laser Pointer/Bore Sighter).

## Original Presentation of Material

The original material was presented at the April Meeting of the Toronto, Canada *Python Meetup* group [see](http://www.meetup.com/Python-Toronto/events/229959373/).  This original material is archived on the Meetup WWW site including the 20 slide presentation and videos referenced in it.


Future plans include the detection of audio and video events together and taking actions based upon these and improvement of the 'skew' correction of the image.
