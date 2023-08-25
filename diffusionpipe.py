from diffusers import DiffusionPipeline,DPMSolverSinglestepScheduler
import transformers
import torch


#sampling = DPM++ SDE Karras which is very similiar to DPM++ 2s a Karras
DPM = DPMSolverSinglestepScheduler.from_pretrained(r'C:\Users\1\Desktop\SKT FLY AI\SKTproject\sdmodel', use_karras_sigmas=True,subfolder='scheduler')

#CLIP SKIP
clip_skip=2
text_encoder = transformers.CLIPTextModel.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    subfolder = "text_encoder",
    num_hidden_layers = 12 - (clip_skip - 1))

pipeline = DiffusionPipeline.from_pretrained(
    r'C:\Users\1\Desktop\SKT FLY AI\SKTproject\sdmodel'
    ,custom_pipleline = "lpw_stable_diffusion"
    ,safety_checker = None
    ,requires_safety_checker = False
    ,scheduler=DPM
    ,text_encoder = text_encoder
)

#embeddings
pipeline.load_textual_inversion(r'embeddings\badhandv4.pt')
pipeline.load_textual_inversion(r'embeddings\easynegative.pt')



pipeline.to("cuda")
pipeline.enable_xformers_memory_efficient_attention()

prompt = """
1girl
"""
neg_prompt = """NSFW"""

generator = torch.Generator("cuda").manual_seed(-1)
#images = []
image = pipeline(prompt,
                 negative_prompt=neg_prompt,
                 generator = generator,
                 num_inference_steps = 23,
                guidance_scale = 8,
                width = 768,
                height = 512,
                ).images[0]

#num_images_per_prompt=3
image.save(r'output\result3.png')