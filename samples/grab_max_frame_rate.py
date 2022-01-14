# Grab_UsingGrabLoopThread.cpp
# This sample illustrates how to grab and process images using the grab loop thread
# provided by the Instant Camera class.

from pypylon import genicam
from pypylon import pylon

import time

frame_counter = 0
current_max_rate = 156
time_last = 3
frame_count = current_max_rate * time_last
bExit = False


# Example of an image event handler.
class SampleImageEventHandler(pylon.ImageEventHandler):
    def OnImageGrabbed(self, camera, grabResult):
        global frame_counter,bExit
        frame_counter +=1
        if frame_counter >= frame_count - 1:
            bExit = True

if __name__ == '__main__':
    try:
        # Create an instant camera object for the camera device found first.
        camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

        # For demonstration purposes only, register another image event handler.
        camera.RegisterImageEventHandler(SampleImageEventHandler(), pylon.RegistrationMode_Append, pylon.Cleanup_Delete)

        # Start the grabbing using the grab loop thread, by setting the grabLoopType parameter
        # to GrabLoop_ProvidedByInstantCamera. The grab results are delivered to the image event handlers.
        # The GrabStrategy_OneByOne default grab strategy is used.
        camera.StartGrabbing(pylon.GrabStrategy_OneByOne, pylon.GrabLoop_ProvidedByInstantCamera)

        time_start = time.time()
        # Wait for user input to trigger the camera or exit the program.
        # The grabbing is stopped, the device is closed and destroyed automatically when the camera object goes out of scope.
        while not bExit:
            pass
        time_cost = time.time() - time_start
        print(f"{frame_count} frame cost:{time_cost} s")
        camera.StopGrabbing()
    except genicam.GenericException as e:
        # Error handling.
        print("An exception occurred.", e.GetDescription())
