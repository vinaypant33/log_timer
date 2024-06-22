import tkinter as tk
from tkinter import ttk
import ttkbootstrap as btk

from pubsub import pub
# from tkinter import messagebox
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.dialogs.dialogs import Messagebox
import ttkbootstrap.icons
from ttkbootstrap.tooltip import ToolTip






main_window  = btk.Window()

# App Constants and General Parts : 
main_window.title("Time Logger")
window_width  = 500
window_height  = 700
x_location = ( main_window.winfo_screenwidth() //2 ) - (window_width // 2)
y_location  = (main_window.winfo_screenheight() //2) - (window_height  // 2)

main_window.resizable(0 , 0)
main_window.geometry(f"{window_width}x{window_height}+{x_location}+{y_location}")


# Other App Constants  :
frame_width  = window_width
bottom_frame_height  = 30
frame_width  = window_width - 10
frame_height  = 300

play_icon  = '\u25B6'
pause_icon  = ''
play_text  = "  Start Focus Session"
pause_text = "  Pause Focus Session"




############## Defining Controls ##################
bottom_frame  = btk.Frame(main_window , width=window_width , height=bottom_frame_height , bootstyle  = "info")

canvas  = tk.Canvas(main_window)
scrollbar  = ttk.Scrollbar(main_window , orient=tk.VERTICAL , command=canvas.yview)
controls_frame = ttk.Frame(canvas)

timer_frame = btk.Frame(controls_frame , width=frame_width , height = frame_height , bootstyle  = "warning")
task_frame   = btk.Frame(controls_frame , width=frame_width , height = frame_height , bootstyle  = "info")
analytics_frame  = btk.Frame(controls_frame  , width=frame_width , height = frame_height , bootstyle = "primary")
text  = btk.Label(timer_frame , text="Select time to start focus session !!!")
play_pause_button  = btk.Button(timer_frame , text=f"{play_icon}{play_text}")

############## Configuring Controls #################
canvas.configure(yscrollcommand=scrollbar)
timer_frame.pack_propagate(0)
task_frame.pack_propagate(0)
analytics_frame.pack_propagate(0)


############### Binding Controls ####################
canvas.bind("<Configure>" , lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0) , window=controls_frame , anchor='nw')


#################### Packing Controls ###############
bottom_frame.pack(side=tk.BOTTOM)
canvas.pack(side=tk.LEFT , fill=tk.BOTH , expand=True)
scrollbar.pack(side=tk.RIGHT , fill=tk.Y)
timer_frame.pack()
task_frame.pack()
analytics_frame.pack()
text.pack(pady=(15 , 0))
play_pause_button.pack(pady=(15,0))


main_window.mainloop()