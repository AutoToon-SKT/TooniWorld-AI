#-*- coding:utf-8 -*-
#import openai
import config
import gpt_config
from preprocess import input_preprocess, prompt_preprocess
#from prompt import Prompt
from diffusionpipe import generate_image, save_image

input = "누구와 : 친구\n장소 : SK 인재개발원\n분위기 : 즐거운, 활기찬\n날씨 : 비\n그림체 : 웹툰\n이야기 : 소나기가 내리는 날, 2023년 6월 29일. SK 인재개발원은 웃음과 활기로 가득한 장소로 변모했다. 이날 나와 친구는 웹툰 속 주인공처럼 환상적인 순간을 만들기 위해 모였다.건물 입구에서 우산을 펴며 만남을 앞두릴 때, SK 인재개발원 창문 밖으로 펼쳐진 푸른 잔디와 햇살을 받는 나무들은 비 내림을 맞이하며 더욱 빛나고 있었다. SK 인재개발원 내부로 들어가 자리에 앉았을 때, 갑작스러운 소나기가 창문을 두드리며 들어왔다. 우리는 깜짝 놀란 뒤, 비 내림을 단숨에 잊고 밖으로 나가 소나기 놀이를 즐겼다.우리의 웃음소리와 발소리가 비 내림과 어우러져 멋진 하모니를 이루었다. 대나무 숲 사이로 비 내림이 조용히 스며들어오는 장소에서, 우리는 웹툰처럼 화보 같은 사진을 찍었다. 그 순간, 친구의 웃음과 비 내림의 소리가 어우러져 환상적인 분위기를 낳았다. 소나기가 그치고 나니 하늘은 맑게 개었고, 우리는 웹툰 속 주인공처럼 감동을 안겨주는 하루를 보냈다. 이 활기찬 추억은 늘 우리의 마음속에 담겨, 어떤 날에도 따뜻한 웃음과 함께 떠올릴 수 있을 것이다."

if __name__ == "__main__":
    #openai.api_key = gpt_config.API_KEY
    # 인풋에서 이야기 추출
    story = input_preprocess(input)
    print(story[:10])

    # gpt api로 이야기를 4컷으로 분할 후 각각에 대한 프롬프트 생성
    # pt = Prompt(story)
    # answer = pt.generate()
    # prompts = prompt_preprocess(answer)
    prompts = prompt_preprocess(config.PROMPT_EX)

    # 각 컷에 대해 이미지 3장씩 생성
    for i in range(len(prompts)):
        images = generate_image(prompts[i])
        save_image(images, config.TITLE_EX, str(i))

