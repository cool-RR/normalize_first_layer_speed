# normalize_first_layer_speed

Simplify3D script to make the first layer speed be constant.

This is useful because Simplify3D wants the first layer slowdown to be given as a percentage, which is stupid. Sometimes you change the default speed of your prints, and then you have to go and change the first layer underspeed percentage to keep the first layer speed slow enough to adhere, but not too slow.

This script solves this problem by keeping the first layer speed constant.

Command line usage:

    normalize_first_layer_speed.py your_gcode.gcode --speed 100
  
Only works for gcodes created by Simplify3D. This will replace the file in-place. Requires installing `python_toolbox` and `click`. 

You can omit the `--speed 100` part, 100 mm/s is the default.

Add this script to your post-processing settings in Simplify3D to make it work automatically when creating gcodes.
