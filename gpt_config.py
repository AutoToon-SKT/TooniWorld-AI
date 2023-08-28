API_KEY = "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"
GPT_MODEL = "gpt-3.5-turbo" # "gpt-4"

SYSTEM = "You are a helpful assistant"
USER1 = """이야기를 만화로 만들거야.만화로 만들기 위해선 이야기를 부분으로 나누어야 돼.
최대한 내용이 보존되게 4개의 부분으로 나누어줘.
한 부분은 패널이라고 지칭할게. 그리고 나누기기 위해 입력한 이야기는 입력이야기라고 지칭할게.

'한 패널의 형식의 예시'를 들면 이런 형식이야.

<Panel 1: Start of Study Abroad in Canada>

(Seungho begins a homestay with 3 Korean friends in a local host's house in Canada.)
,((Seungho: a 20's boy with black hair))
,(Time: Morning)
,(Background: Canadian airport),
,(Characters: Seungho,3 Korean friends)
,(4 Characters)

그리고 한 패널에는 6개에 항목이 있고 각 항목들에 대해 설명해줄게.

1번째 항목은 situation이고 나눈 패널의 상황에 대한 묘사를 하는 항목이다.
'한 패널의 형식의 예시' 에서는  (Seungho begins a homestay with 3 Korean friends in a local host's house in Canada.)가 situation이다.

situation을 작성할때는 이야기의 내용을 바꾸는 창작은 하지 말고 입력된 이야기가 최대한 보존하면서 분위기와 느낌을 추가해서 작성하기
그리고 situation을 작성할때 입력이야기의 I는 주인공이름으로
My는 주인공이름's로,
me는 주인공이름으로 바꾸어서 작성한다.
'한 패널의 형식의 예시'에서 주인공의 이름은 Seungho이다.
그리고 situation을 작성할때 대명사,1인칭표현 사용은 최대한 자제한다.
그리고 situation에 등장하는 캐릭터 이름과 Characters항목에 등장하는 이름이 같게 한다.
지금 문장으로 부터 위에 7줄에 나와있는 situation 작성시 고려사항을 반영하여 각 패널당 situation은 최대 75 의미토큰으로 작성한다.

2번째 항목은 주인공에 대한 특징 항목이다.
'한 패널의 형식의 예시' 에서는 ((Seungho: a 20's boy with black hair))가 주인공에 대한 특징 항목
입력이야기와 함께 ((주인공이름:주인공의 나이,성별,헤어스타일.특징을 묘사하는 문장))을 입력할거야.
그리고 주인공의 나이가 20살에서 29살사이 혹인 20대라면 주인공에 대한 특징 항목에서 20's라는 표현을 써줘.

만약 situation에 주인공이 등장한다면 situation항목뒤에 ,((주인공이름:주인공의 나이,성별,헤어스타일,특징을 묘사하는 문장))을 추가한다.

3번째 항목은 situation의 시간대에 대한 항목인 (Time:)이다.
'한 패널의 형식의 예시'에서는 (Time: Morning)이 (Time:)이다.
(Time:)항목을 작성할때에는 morning,afternoon,evening,night,dawn과 같이 명확한 시간대를 알수 있는 표현을 위주로 사용한다.
이전 패널의 (Time:)항목을 고려해서 시간순서에 위배되지 않게 한다.

4번째 항목은 situation의 배경에 대한 항목인 (Background:)이다.
'한 패널의 형식의 예시'에서는 (Background: Canadian airport)이 (Background:)이다.
situation에 등장하는 배경장소에 대한 이름과 Characters항목에 등장하는 이름이 같게 한다.
입력이야기를 기반으로 날씨에 대한 표현을 추가할 수 도 있다.

5번째 항목은 situation의 등장하는 캐릭터에 대한 항목이다.
'한 패널의 형식의 예시'에서는 (Characters: Seungho,3 Korean friends)이 (Background:)이다.
그리고 situation에 등장하는 캐릭터 이름과 Characters항목에 등장하는 이름이 같게 한다.

6번째 항목은 situation의 등장하는 캐릭터의 수이다.
'한 패널의 형식의 예시'에서는 (4 Characters)이다.
'한 패널의 형식의 예시'에서 (4 Characters)인 이유는 (Characters: Seungho,3 Korean friends)에서 등장하는 캐릭터가 총 4명이므로 (4 Characters)이다.
위와 같은 방식으로 등장하는 캐릭터의 수를 표시한다.
만약 (1 Characters)인 경우, (1 Characters)대신 (Solo)를 추가한다.

다음으로 패널 작성시에 추가 고려사항에 대해 알려주겠다.

1.

입력 이야기의 주인공(protagonist)의 가족 등장시
주인공의 가족 명칭 앞에 주인공이름's 추가
2.
만약 입력이야기의 가족 등장시 입력이야기에 등장하는 각 패널의 주인공의 가족 구성원에 대한 설명 항목 추가
설명문장은 각 패널 모두 동일한 문장을 사용한다.
예를들어
(Yeonsoo's family members are her mother, father, and older sister)
그러나 패널의 (Characters:)의 주인공만 등장한다면 추가하지 않는다.
3.
각 패널들의 항목들간에 의미 중복되는 단어 사용 자제
예를들어
한 패널의 항목들에 (Around the age of 6, Yeonsoo went on a family vacation with her relatives. While the details remain somewhat fuzzy, she recalls playing on the tidal flats, likely along the West Sea.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair))는
(Yeonsoo went on a family vacation with her relatives. While the details remain somewhat fuzzy, she recalls playing on the tidal flats, likely along the West Sea.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair))로 수정되어야한다.
4.
각 패널들의 항목들은 ,로 연결되어있다.
5.
각 패널 제목과 항목들은 영어로 출력

각 패널들의 항목들은 ,로 연결되어 있다.
패널제목에 볼드체 사용금지

위와 같은 기능을 수행하는 함수를 '나누기'라고 정한다.

'나누기'함수에 대한 출력예시를 알려주겠다.

예를 들어

6살 때즈음에 이야기인데, 가족들과 함께 가족여행을 갔다.

자세한 것들은 기억이 나지 않지만 갯벌에서 놀았다고 하니 서해였을 것이다.

나는 회색 이 있으 입고 있었고 언니랑 같이 놀고 있었다.

엄마랑 아빠는 저 멀리 커다란 돌 위에 앉아 있었다.

언니랑 재밌게 놀던 와중에 언니가 나한테 장난을 친다고 뻘을 한 주먹 집더니 내 얼굴에 던지고 도망갔다.

나는 화가 나고 서러워서 엉엉 울었다.

엄마한테 당장 이르고 싶어서 뻘 때문에 잘 보이지 않는 눈을 게슴츠레 뜨고 엄마를 쳐다보았는데,

엄마랑 아빠가 나를 보며 깔깔 웃고 있었다.

그런 엄마랑 아빠를 향해 언니는 깔깔 웃으며 달려가고 있었다.

당시에는 매우 서러웠지만 지금은 부모님이 웃으신 이유를 알 것 같다.

다 내가 귀엽기 때문!

'나누기',((연수:회색 후드티를 입은 검정 묶은 머리의 6살 여자아이))

가 입력되면 너의 답변은

<Panel 1: Family Trip at Age 6>
(Yeonsoo went on a family vacation with her relatives. While the details remain somewhat fuzzy, she recalls playing on the tidal flats, likely along the West Sea.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Childhood), (Background: Shoreline),
(Characters: Yeonsoo, Yeonsoo's mother, Yeonsoo's father, Yeonsoo's older sister), (4 characters),
(Yeonsoo's family members are her mother, father, and older sister)

<Panel 2: Playtime with Sister>
(Under the warm sunlight of the day, Yeonsoo and her older sister reveled in amusing pastimes across the expansive tidal flats. The radiant sunlit expanse stretched ahead, while Yeonsoo's parents enjoyed their relaxation on a distant, sizable rock.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Sunny Day), (Background: Expansive Tidal Flats),
(Characters: Yeonsoo, Yeonsoo's older sister), (2 characters),
(Yeonsoo's family members are her mother, father, and older sister)

<Panel 3: A Prank and Unexpected Tears>
(Out of the blue, Yeonsoo's older sister played a prank on Yeonsoo, throwing a handful of mud at Yeonsoo's face before fleeing. Caught off guard, Yeonsoo was left with mixed emotions, transitioning from laughter to tears.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Sunny Day), (Background: Expansive Tidal Flats),
(Characters: Yeonsoo), (Solo)

<Panel 4: Shared Laughter Amidst Tears>
(Yeonsoo's watery eyes met Yeonsoo's parents' and Yeonsoo's older sister's chuckles as they witnessed Yeonsoo's adorable reaction to the playful prank. In that heartwarming moment on the expansive tidal flats, mutual understanding and shared laughter brought Yeonsoo's family closer.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Sunny Day), (Background: Expansive Tidal Flats),
(Characters: Yeonsoo, Yeonsoo's mother, Yeonsoo's father, Yeonsoo's older sister), (4 characters),
(Yeonsoo's family members are her mother, father, and older sister)

이다.

항목은 전부 영어로 출력.

그 동안 내가 알려준 기능을 '나누기'로 기억하고 사용한다.

입력이야기와

'나누기',((주인공이름:주인공의 나이,성별,헤어스타일,특징을 묘사한 문장))

을 입력하면 답변은 일반텍스트 형태의 오직 4개의 패널만 해준다 너의 설명은 필요없어. 파이썬 함수를 원하는게 아님.
"""
USER2 = """'나누기'의 답변결과는 4개의 패널만이야.너의 설명은 필요없어
"""
USER3 = """6살 때즈음에 이야기인데, 가족들과 함께 가족여행을 갔다.

자세한 것들은 기억이 나지 않지만 갯벌에서 놀았다고 하니 서해였을 것이다.

나는 회색 이 있으 입고 있었고 언니랑 같이 놀고 있었다.

엄마랑 아빠는 저 멀리 커다란 돌 위에 앉아 있었다.

언니랑 재밌게 놀던 와중에 언니가 나한테 장난을 친다고 뻘을 한 주먹 집더니 내 얼굴에 던지고 도망갔다.

나는 화가 나고 서러워서 엉엉 울었다.

엄마한테 당장 이르고 싶어서 뻘 때문에 잘 보이지 않는 눈을 게슴츠레 뜨고 엄마를 쳐다보았는데,

엄마랑 아빠가 나를 보며 깔깔 웃고 있었다.

그런 엄마랑 아빠를 향해 언니는 깔깔 웃으며 달려가고 있었다.

당시에는 매우 서러웠지만 지금은 부모님이 웃으신 이유를 알 것 같다.

다 내가 귀엽기 때문!

'나누기',((연수:회색 후드티를 입은 검정 묶은 머리의 6살 여자아이))
"""
ASSISTANT1 = """네, 이해했습니다. 주어진 기능과 형식을 기반으로 주어진 입력 이야기를 4개의 패널로 나누어 보겠습니다. 입력된 이야기에 대한 내용을 최대한 보존하면서 각 항목을 작성하도록 하겠습니다.

**입력 이야기:**

6살 때즈음에 이야기인데, 가족들과 함께 가족여행을 갔다.

자세한 것들은 기억이 나지 않지만 갯벌에서 놀았다고 하니 서해였을 것이다.

나는 회색 이 있으 입고 있었고 언니랑 같이 놀고 있었다.

엄마랑 아빠는 저 멀리 커다란 돌 위에 앉아 있었다.

언니랑 재밌게 놀던 와중에 언니가 나한테 장난을 친다고 뻘을 한 주먹 집더니 내 얼굴에 던지고 도망갔다.

나는 화가 나고 서러워서 엉엉 울었다.

엄마한테 당장 이르고 싶어서 뻘 때문에 잘 보이지 않는 눈을 게슴츠레 뜨고 엄마를 쳐다보았는데,

엄마랑 아빠가 나를 보며 깔깔 웃고 있었다.

그런 엄마랑 아빠를 향해 언니는 깔깔 웃으며 달려가고 있었다.

다 내가 귀엽기 때문!

**나누기:**

<Panel 1: Family Trip at Age 6>
(Yeonsoo went on a family vacation with her relatives. While the details remain somewhat fuzzy, she recalls playing on the tidal flats, likely along the West Sea.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Childhood), (Background: Shoreline),
(Characters: Yeonsoo, Yeonsoo's mother, Yeonsoo's father, Yeonsoo's older sister), (4 characters),
(Yeonsoo's family members are her mother, father, and older sister)

<Panel 2: Playtime with Sister>
(Under the warm sunlight of the day, Yeonsoo and her older sister reveled in amusing pastimes across the expansive tidal flats. The radiant sunlit expanse stretched ahead, while Yeonsoo's parents enjoyed their relaxation on a distant, sizable rock.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Sunny Day), (Background: Expansive Tidal Flats),
(Characters: Yeonsoo, Yeonsoo's older sister), (2 characters),
(Yeonsoo's family members are her mother, father, and older sister)

<Panel 3: A Prank and Unexpected Tears>
(Out of the blue, Yeonsoo's older sister played a prank on Yeonsoo, throwing a handful of mud at Yeonsoo's face before fleeing. Caught off guard, Yeonsoo was left with mixed emotions, transitioning from laughter to tears.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Sunny Day), (Background: Expansive Tidal Flats),
(Characters: Yeonsoo), (Solo)

<Panel 4: Shared Laughter Amidst Tears>
(Yeonsoo's watery eyes met Yeonsoo's parents' and Yeonsoo's older sister's chuckles as they witnessed Yeonsoo's adorable reaction to the playful prank. In that heartwarming moment on the expansive tidal flats, mutual understanding and shared laughter brought Yeonsoo's family closer.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Sunny Day), (Background: Expansive Tidal Flats),
(Characters: Yeonsoo, Yeonsoo's mother, Yeonsoo's father, Yeonsoo's older sister), (4 characters),
(Yeonsoo's family members are her mother, father, and older sister)

위의 '나누기' 함수를 사용하여 주어진 입력 이야기를 4개의 패널로 나누었습니다. 필요한 정보와 상황이 모두 보존되도록 하였습니다.
"""
ASSISTANT2 = """<Panel 1: Family Trip at Age 6>
(Yeonsoo went on a family vacation with her relatives. While the details remain somewhat fuzzy, she recalls playing on the tidal flats, likely along the West Sea.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Childhood), (Background: Shoreline),
(Characters: Yeonsoo, Yeonsoo's mother, Yeonsoo's father, Yeonsoo's older sister), (4 characters),
(Yeonsoo's family members are her mother, father, and older sister)

<Panel 2: Playtime with Sister>
(Under the warm sunlight of the day, Yeonsoo and her older sister reveled in amusing pastimes across the expansive tidal flats. The radiant sunlit expanse stretched ahead, while Yeonsoo's parents enjoyed their relaxation on a distant, sizable rock.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Sunny Day), (Background: Expansive Tidal Flats),
(Characters: Yeonsoo, Yeonsoo's older sister), (2 characters),
(Yeonsoo's family members are her mother, father, and older sister)

<Panel 3: A Prank and Unexpected Tears>
(Out of the blue, Yeonsoo's older sister played a prank on Yeonsoo, throwing a handful of mud at Yeonsoo's face before fleeing. Caught off guard, Yeonsoo was left with mixed emotions, transitioning from laughter to tears.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Sunny Day), (Background: Expansive Tidal Flats),
(Characters: Yeonsoo), (Solo)

<Panel 4: Shared Laughter Amidst Tears>
(Yeonsoo's watery eyes met Yeonsoo's parents' and Yeonsoo's older sister's chuckles as they witnessed Yeonsoo's adorable reaction to the playful prank. In that heartwarming moment on the expansive tidal flats, mutual understanding and shared laughter brought Yeonsoo's family closer.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Sunny Day), (Background: Expansive Tidal Flats),
(Characters: Yeonsoo, Yeonsoo's mother, Yeonsoo's father, Yeonsoo's older sister), (4 characters),
(Yeonsoo's family members are her mother, father, and older sister)
"""
ASSISTANT3 = """<Panel 1: Family Trip at Age 6>
(At around the age of 6, Yeonsoo went on a family trip with her relatives. Although the specifics are hazy in her memory, she recalls playing on the tidal flats, likely along the West Sea.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Childhood), (Background: Tidal Flats),
(Characters: Yeonsoo, Yeonsoo's family), (4 characters)

<Panel 2: Playtime with Sister>
(While frolicking on the tidal flats with her older sister under the warm sun, Yeonsoo donned a gray hooded t-shirt and tied-up black hair. In the distance, her parents sat atop a large rock, enjoying the view.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Daytime), (Background: Expansive Tidal Flats),
(Characters: Yeonsoo, Yeonsoo's older sister, Yeonsoo's parents), (4 characters)

<Panel 3: Prank and Tears>
(During their playful activities, Yeonsoo's older sister suddenly played a prank on her, playfully tossing a handful of mud onto her face and then darting away. Overwhelmed with mixed emotions, Yeonsoo went from laughter to teary-eyed sadness.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Daytime), (Background: Expansive Tidal Flats),
(Characters: Yeonsoo), (Solo)

<Panel 4: Laughter in the Family>
(Teary-eyed, Yeonsoo looked toward her parents with her disheveled hair and tried to convey her frustration. However, instead of sympathy, she found her parents chuckling heartily at her predicament. Even her older sister was gleefully approaching them, all sharing a moment of laughter and understanding amidst the emotions.),((Yeonsoo: A 6-year-old girl with a gray hooded t-shirt and tied-up black hair)),(Time: Daytime), (Background: Expansive Tidal Flats),
(Characters: Yeonsoo, Yeonsoo's older sister, Yeonsoo's parents), (4 characters)
"""