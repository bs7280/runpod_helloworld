import base64
import runpod
import io
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

runpod_api_key = os.environ.get("RUNPOD_API_KEY")
runpod_endpoint_id = os.environ.get("RUNPOD_ENDPOINT_ID")

runpod.api_key = runpod_api_key
endpoint = runpod.Endpoint(runpod_endpoint_id)
input = {"input": {"prompt": "a photo of an astronaut riding a horse on mars"}}

try:
    run_request = endpoint.run_sync(request_input=input, timeout=120)
    image_bytes = run_request["bytes"]
    bytes = base64.b64decode((image_bytes.encode("utf-8")))
    image = Image.open(io.BytesIO(bytes))
    # image.save("output.png")

    # Create a Tkinter window
    root = tk.Tk()

    # Convert the image to a format that Tkinter can display
    tk_image = ImageTk.PhotoImage(image)

    # Create a label widget to display the image
    label = Label(root, image=tk_image)
    label.pack()

    # Run the Tkinter event loop
    root.mainloop()

except TimeoutError:
    print("Job timed out.")
