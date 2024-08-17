import base64
import torch
import io
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler


def generate_image_bytes(prompt: str) -> dict:
    """
    Generate an image bytes from a prompt using the Stable Diffusion model.

    Args:
    - prompt (str): The prompt to generate an image from.

    Returns:
    - dict: A dictionary containing the image bytes.
    """

    scheduler = EulerDiscreteScheduler.from_pretrained(
        "stabilityai/stable-diffusion-2", subfolder="scheduler"
    )
    pipe = StableDiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2",
        scheduler=scheduler,
        torch_dtype=torch.float16,
        cache_dir="model_cache/",
    )
    pipe = pipe.to(
        "cuda"
        if torch.cuda.is_available()
        else "mps" if torch.backends.mps.is_available() else "cpu"
    )

    image = pipe(prompt=prompt).images[0]

    bytes = io.BytesIO()
    image.save(bytes, format="PNG")

    return {"bytes": base64.b64encode(bytes.getvalue()).decode("utf-8")}
