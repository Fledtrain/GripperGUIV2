import serial  # Import the serial module to communicate with Arduino
import customtkinter as ctk  # Import the customtkinter module to make the GUI look better
#Appearance of GUI--------------------------------------------------
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")
window = ctk.CTk()
window.title("The Cuh's Team Robot Claw GUI")
window.geometry("600x600")
frame = ctk.CTkFrame(master=window)
frame.pack(pady=40, padx=40, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Claw GUI!", font=("Arial", 20), )
label.pack(pady=12, padx=12)
#--------------------------------------------------------------------
# Connect to the Arduino---------------------------------------------
arduino_ready = True  # Set this to False if you don't have an Arduino connected
arduino = serial.Serial(port="/dev/cu.usbmodem142301",
                        baudrate=9600,
                        timeout=1)

# The servo angle variable
servo_angle = 0

# Functions to send angle to Arduino
def send_angle(angle):
    arduino.write(str(angle).encode())


# Functions to update the servo angle value
def update_servo_angle(angle):
    global servo_angle, txt
    servo_angle = angle
    txt = "Servo Angle: {}".format(int(servo_angle))
    label.configure(text=txt)


def set_servo_angle(angle):
    arduino.write(str(angle).encode())


# Open the claw button
def open_claw():
    arduino.write(b'o')  # Send the 'o' character to the Arduino to open the claw
    label.configure(text="Claw opened!")
    servo_angle = 180  # Update the servo angle variable
    slider.set(int(servo_angle))  # Update the slider value


# Close the claw button
def close_claw():
    arduino.write(b'c')  # Send the 'c' character to the Arduino to close the claw
    label.configure(text="Claw closed!")
    servo_angle = 0  # Update the servo angle variable
    slider.set(int(servo_angle))  # Update the slider value


# The slider widget
def slider_changed(value):
    update_servo_angle(value) #Label displays current angle
    arduino.write(str(int(value)).encode())
    servo_angle = value
    slider.set(int(servo_angle))



# Open the claw button
open_button = ctk.CTkButton(master=frame, text="Open Claw", font=("Sans Serif", 25), command=open_claw)
open_button.pack(pady=20, padx=20)

# Close the claw button
close_button = ctk.CTkButton(master=frame, text="Close Claw", font=("Sans Serif", 25), command=close_claw)
close_button.pack(pady=20, padx=20)

# The slider widget
slider = ctk.CTkSlider(master=frame, from_=0, to=180, command=slider_changed)
slider.pack(pady=20, padx=10)

window.mainloop()