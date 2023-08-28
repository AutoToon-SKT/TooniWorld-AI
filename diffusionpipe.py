from diffusers import DiffusionPipeline,DPMSolverSinglestepScheduler
import config
import transformers
import torch
import warnings
warnings.filterwarnings('ignore')

def generate_image(prompt):
    #sampling = DPM++ SDE Karras which is very similiar to DPM++ 2s a Karras
    DPM = DPMSolverSinglestepScheduler.from_pretrained(config.FLAT2D_PATH, use_karras_sigmas=True,subfolder='scheduler')

    #CLIP SKIP
    clip_skip=2
    text_encoder = transformers.CLIPTextModel.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        subfolder = "text_encoder",
        # torch_dtype = torch.float16,
        num_hidden_layers = 12 - (clip_skip - 1))

    pipeline = DiffusionPipeline.from_pretrained(
        config.FLAT2D_PATH #flat2D
        ,custom_pipleline = "lpw_stable_diffusion"
        # ,torch_dtype = torch.float16
        ,safety_checker = None
        ,requires_safety_checker = False
        ,scheduler=DPM
        ,text_encoder = text_encoder
    )

    #embeddings
    pipeline.load_textual_inversion(config.BADHAND_PATH)
    pipeline.load_textual_inversion(config.EASYNEGATIVE_PATH)



    pipeline.to("cuda")
    pipeline.enable_xformers_memory_efficient_attention()

    generator = torch.Generator("cuda").manual_seed(-1)
    #images = []
    image = pipeline(prompt+config.FIXED_PROMPT,
                    negative_prompt=config.NEGATIVE_PROMPT,
                    generator = generator,
                    num_inference_steps = 23,
                    guidance_scale = 8,
                    width = 768,
                    height = 512,
                    num_images_per_prompt = 3
                    ).images

    return image

def save_image(image, title, image_no):
    #num_images_per_prompt=3
    for i in range(len(image)):
        image[i].save("./outputs/"+title+image_no+f'-{i}.png')