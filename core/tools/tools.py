import webuiapi
#bash webui.sh --api 
from openai import OpenAI
api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


def chat_answer(messages):
    completion = client.chat.completions.create(
      model="TheBloke/dolphin-2.2.1-mistral-7B-GGUF",
      messages=messages,
      temperature=1.1,
      max_tokens=140 ,
    )
    return completion.choices[0].message.content


def generate_image(prompt):
    result = api.txt2img(prompt=prompt,
                    negative_prompt="(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation ",
                    seed=random.randint(0,10000),
                    steps=20,
                    sampler_index='DDIM',
                    enable_hr=True,
                    hr_scale=2,
                    hr_upscaler=webuiapi.HiResUpscaler.Latent,
                    hr_second_pass_steps=20,
                    hr_resize_x=300,
                    hr_resize_y=400,
                    denoising_strength=0.4,
                    cfg_scale=7,)
    image_path = 'generated_image.png'
    result.image.save(image_path)
    return image_path
