# AutoRAG 한국어 튜토리얼

https://github.com/Marker-Inc-Korea/AutoRAG-tutorial-ko

위 코드를 기반으로 따라함

# 설치

```bash
# 가상 환경 생성 
conda create -n autorag 
conda activate autorag
```

```bash
pip install -r requirements.txt
```

## 빠른 시작 

Ollama 설치하고 

```bash
pip install llama_index.llms.ollama
```

아래 명령어로 로컬에서 모델을 돌린다.
```bash
python main.py --config ./config/compact_local_simple_ollama_ko.yaml

```

아래 명령어로 평가지표들을 살핀다. 

```bash
autorag dashboard --trial_dir ./benchmark/0
```

------


## 준비 

1. `.env.template` 파일을 복사하여 `.env` 파일을 만들고 저장합니다. 반드시 본인의 OpenAI api key를 이 파일에 적어주세요. `OPENAI_API_KEY` 를 환경변수로 설정합니다.



## 기존 데이터 확인하기 

1. `raw_docs`에서 원본 문서를 확인합니다. 이 튜토리얼에서는 세 개의 pdf 문서를 이용하고자 합니다.

2. `read_data.ipynb` 로 .parquet 데이터 확인 

## 내 데이터 만들기 

1. `make_corpus.py`를 실행합니다. 
```bash
python make_corpus.py 
```
3. `data` 폴더에 생성된 `corpus_new.parquet`을 확인할 수 있습니다. `pandas`로 직접 살펴보면 더욱 좋습니다.

5. `make_qa.py`를 실행하여 질의 응답 데이터셋을 제작합니다. 
6. `qa_new.parquet` 파일을 확인합니다. 직접 데이터셋을 검토해보고, 별로인 질문을 수정 혹은 삭제합니다.
7. 더 좋은 데이터셋 생성을 위해 `make_qa.py`의 프롬프트를 수정합니다.

# 프로젝트 구동

## main.py 이용


2. 아래처럼 main.py를 실행하여 AutoRAG를 구동하세요.
```bash
python3 main.py --config ./config/tutorial_ko.yaml
```
3. benchmark 폴더가 생성되면 거기서 결과를 확인할 수 있습니다.

## cli 이용

1. `benchmark` 폴더를 만들어 줍니다.
2. `OPENAI_API_KEY`를 환경변수로 설정합니다. `export OPENAI_API_KEY=sk-xxxx` 
3. 아래 cli 명령을 실행하여 AutoRAG 최적화를 시작합니다.
```bash
autorag evaluate --qa_data_path ./data/qa.parquet --corpus_data_path ./data/corpus.parquet \
  --config ./config/tutorial_ko.yaml --project_dir ./benchmark
```
위 데이터셋 튜토리얼에서 제작한 데이터셋으로 실행하려면, 
`corpus.parquet`을 `corpus_new.parquet`, `qa.parquet`을 `qa_new.parquet`으로 바꿔주세요.
4. benchmark 폴더가 생성되면 거기서 결과를 확인할 수 있습니다.

# 대시보드 실행

아래 명령을 실행하여 대시보드를 로드합니다. 대시보드를 통해 결과를 아주 쉽게 검토할 수 있습니다.

```bash
autorag dashboard --trial_dir ./benchmark/0
```

# streamlit 실행
streamlit을 실행하여 직접 최적화된 RAG를 사용해 볼 수 있습니다. 
아래 명령을 실행하세요.

```bash
autorag run_web --trial_path ./benchmark/0
```

### 이런 질문을 해보세요.
- 야후가 NFL 팬을 위해 도입한 기능은 뭐야?
- 핀테크 혁신 투자로 기업이 성장한 회사들은 어디가 있어?
- 부동산 대출 연체가 늘어나면 어떻게 되나요?


-------------

현재 config/tutorial_ko.yaml 에서 bert_score는 주석 처리 되어있는데 
새 야물파일 만들어서 bert_score도 사용해서 실험해보고 다양하게 실험해 보자. 


아래와 같은 에러가 발생한다. 

![image](https://github.com/khw11044/AutoRAG-tutorial-mine/assets/51473705/7f1051a2-f6c9-44de-91ba-c9ff43849352)

```bash
RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for gpt-3.5-turbo in organization org-gfkziyhMDatLfCvKBtEcO7oE on tokens per min (TPM): Limit 60000, 
                             Used 59787, Requested 1683. Please try again in 1.47s. Visit https://platform.openai.com/account/rate-limits to learn more.', 'type': 'tokens', 'param': None, 'code':
                             'rate_limit_exceeded'}}
```

openai api키를 사용해서 그런듯 