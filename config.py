# checkpoints
FLAT2D_PATH = "./models/flat2DAnimerge_v30"
TOONYOU_PATH = "./models/toonyou_beta6"
DELIBERATE_PATH = "./models/deliberate_v2"

# embeddings
BADHAND_PATH = "./embeddings/badhandv4.pt"
EASYNEGATIVE_PATH = "./embeddings/easynegative.pt"

# prompts
FIXED_PROMPT = ",((Best quality,Extremely detailed,Masterpiece)),(facial expression),(different hair color and style of Characters:1.7),(((All Characters exist in image)))"
NEGATIVE_PROMPT = "easynegative,badhandv4,(((same character))),poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, overexposed, bad art, distorted face,text,((extra hand)),((extra arm)),NSFW"

SAVE_PATH = "./outputs/"

# test
story = """내가 가장 활발하게 활동하는 동아리 개망나니 선배, 동기, 후배들 20명이랑 가평에 빠지를 갔다왔다.
대부분은 지하철로 이동했지만, 나는 준혁 오빠, 민준이와 준혁 오빠 차를 타고 이동했다.
우리 셋은 동네 근처 마트에서 술이랑 과자 등을 사서 출발했다. 차가 조금 막혔지만, 편하게 갈 수 있었다.
우리가 도착했을 때 다른 일행들은 이미 빠지에 입장한 뒤였다. 우리도 바로 옷을 갈아입고 갔고, 나는 보트 하나를 탔다.
보트를 타려고 대기하는 중에 진강오빠랑 한빈이, 민준이가 나를 빠트려서 물을 먹기도 했다.
짧지만 재미있었던 빠지를 끝내고 우리는 고기를 먹으러 갔다. 고기는 무제한으로 제공됐고, 우리는 술과 함께 맛있게 먹었다.
고기를 다 먹고 펜션으로 이동했고, 밤을 새서 술을 먹고 게임을 하며 놀았다.
지하철 첫 차를 타고 집에 오는데 너무 피곤해서 오는 내내 잠을 잤다.

'나누기', ((서현:20대 검정머리 소녀))
"""
PROMPT_EX = """
<Panel 1: Family Trip at Age 6>
(Yeonsoo went on a family vacation with her relatives. While the details remain somewhat fuzzy, she recalls playing on the tidal flats, likely along the West Sea.),
((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),
(Time: Childhood),
(Background: Tidal flats along the West Sea),
(Characters: Yeonsoo, Yeonsoo's mother, Yeonsoo's father, Yeonsoo's older sister),
(4 characters),
(Yeonsoo's family members are her mother, father, and older sister)

<Panel 2: Playtime with Sister>
(Yeonsoo and her older sister had a playful time together on the tidal flats. Both wore gray hooded t-shirts as they enjoyed the sandy expanse. In the distance, Yeonsoo's parents sat on a large rock, observing their joyful interactions.),
((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),
(Time: Sunny Day),
(Background: Tidal flats along the West Sea),
(Characters: Yeonsoo, Yeonsoo's older sister, Yeonsoo's mother, Yeonsoo's father),
(4 characters),
(Yeonsoo's family members are her mother, father, and older sister)

<Panel 3: Prank and Tears>
(While Yeonsoo and her sister were immersed in their laughter-filled play, Yeonsoo's sister decided to playfully tease her. Grasping a handful of mud, she aimed it at Yeonsoo's face and then darted away. Filled with a mix of frustration and sadness, Yeonsoo burst into tears.),
((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),
(Time: Sunny Day),
(Background: Tidal flats along the West Sea),
(Characters: Yeonsoo, Yeonsoo's older sister),
(2 characters),
(Yeonsoo's family members are her mother, father, and older sister)

<Panel 4: Laughter and Understanding>
(Yeonsoo, with tear-filled eyes, looked towards her parents for comfort, hoping to share her plight. However, what she found were her parents laughing heartily, finding humor in the situation. Her older sister, having successfully executed the prank, joined in the laughter and ran towards their parents. Despite the initial sorrow, Yeonsoo now understands the reasons behind her parents' smiles that day. It was all because of her endearing response.),
((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),
(Time: Sunny Day),
(Background: Tidal flats along the West Sea),
(Characters: Yeonsoo, Yeonsoo's older sister, Yeonsoo's mother, Yeonsoo's father),
(4 characters),
(Yeonsoo's family members are her mother, father, and older sister)
"""
TITLE_EX = "FamilyTrip"