#==============================================================================#
#                                                                              #
#    Line Azimuth script                                                       #
#    A Python script for estimating the azimuth of a line considering          #
#    the side towards which the line is leaning using the coordinates          #
#    of the edge points and their heights                                      #
#                                                                              #
#    Copyright (c) 2016-present   Marco A. Lopez-Sanchez                       #
#                                                                              #
#    Licensed under the Apache License, Version 2.0 (the "License");           #
#    you may not use this file except in compliance with the License.          #
#    You may obtain a copy of the License at                                   #
#                                                                              #
#        http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                              #
#    Unless required by applicable law or agreed to in writing, software       #
#    distributed under the License is distributed on an "AS IS" BASIS,         #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#    See the License for the specific language governing permissions and       #
#    limitations under the License.                                            #
#                                                                              #
#    Version: 1.0                                                              #
#    For details see: https://github.com/marcoalopez/line_azimuth              #
#                                                                              #
#    Requirements:                                                             #
#        Python version 2.7.x or 3.4.x or higher                               #
#        Numpy version 1.5 or higher                                           #
#                                                                              #
#==============================================================================#


from __future__ import division  # avoid python 2.x - 3.x compatibility issues
from numpy import arctan, degrees

def get_azimuth(x_start, y_start, x_end, y_end, height_start, height_end, r=0):
    """Get the azimuth of a line considering the side towards it is leaning
    using the coordinates of the edge points and the heights of the points.
    Assumptions: x coordinates increased to the east and y coordinates increased
    to the north.
    
    INPUTS
    x_start: x (longitude) coordinate of start point
    y_start: y (latitude) coordinate of start point
    x_end: x (longitude) coordinate of end point
    y_end: y (latitude) coordinate of end point
    height_start: height of the start point
    height_end: height of the end point
    r: round the output to ndigits after the decimal point. It defaults to zero.    
    
    OUTPUT
    The azimuth in sexagesimal degrees(0-360)
    """
    
    # estimate angle, from -90 to 90 degrees
    try:
        angle = degrees(arctan((x_end - x_start)/(y_end - y_start)))
    except ZeroDivisionError:
        angle = None
    
    # correct angle for 0 - 360 degrees    
    if angle > 0:
        if x_end - x_start > 0:
            if height_start >= height_end:  # 1st quadrant
                return round(angle, 0)
            else:  # 3rd quadrant
                return round(180 + angle, r)
        else:
            if height_start >= height_end:  # 3rd quadrant
                return round(180 + angle, r)
            else:  # 1st quadrant
                return round(angle, 0)
    
    elif angle < 0:
        if x_end - x_start > 0:
            if height_start >= height_end:  # 2nd quadrant
                return round(180 + angle, r)
            else:  #4th quadrant
                return round(360 + angle, r)
        else:
            if height_start >= height_end:  #4th quadrant
                return round(360 + angle, r)
            else:  # 2nd quadrant
                return round(180 + angle, r)

    elif angle == 0:
        if y_end - y_start > 0:
            if height_start >= height_end:
                return angle
            else:
                return 180.0
        else:
            if height_start >= height_end:
                return 180.0
            else:
                return angle

    elif angle is None:
        if x_end - x_start > 0:
            if height_start >= height_end:
                return 90.0
            else:
                return 270.0
        else:
            if height_start >= height_end:
                return 270.0
            else:
                return 90.0
