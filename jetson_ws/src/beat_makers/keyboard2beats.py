#!/usr/bin/env python

from rospy import init_node, is_shutdown, Time, Publisher
from beat_msgs.msg import Beat

if __name__ == '__main__':

    init_node('key_to_beats')
    beat_pub =Publisher('beats', Beat, queue_size=10)

    a_beat=Beat()
    a_beat.beat=True

    print("Tap ENTER with beats") # press x to break")

    while not is_shutdown():
        key = raw_input()
        a_beat.mark=Time.now()
        beat_pub.publish(a_beat)
