import runpod
from sd_model import generate_image_bytes

# If your handler runs inference on a model, load the model here.
# You will want models to be loaded into memory before starting serverless.


def handler(job):
    """Handler function that will be used to process jobs."""
    prompt = job["input"]["prompt"]

    return generate_image_bytes(prompt)


runpod.serverless.start({"handler": handler})
