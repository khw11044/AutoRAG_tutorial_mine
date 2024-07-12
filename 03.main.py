import os

import click
from autorag.evaluator import Evaluator
from dotenv import load_dotenv

import autorag
from llama_index.llms.ollama import Ollama
autorag.generator_models["ollama"] = Ollama

from llama_index.embeddings.openai import OpenAIEmbedding, OpenAIEmbeddingModelType
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

autorag.generator_models['kosimcse'] = HuggingFaceEmbedding("BM-K/KoSimCSE-roberta-multitask")
autorag.embedding_models["text-embedding-3-small"] = OpenAIEmbedding(model="text-embedding-3-small")
autorag.embedding_models["bge-m3"] = HuggingFaceEmbedding("BAAI/bge-m3")
autorag.embedding_models["ko-sroberta-multitask"] = HuggingFaceEmbedding("jhgan/ko-sroberta-multitask")
autorag.embedding_models["ko-sbert-nli"] = HuggingFaceEmbedding("jhgan/ko-sbert-nli")
autorag.embedding_models['kosimcse'] = HuggingFaceEmbedding("BM-K/KoSimCSE-roberta-multitask")
autorag.embedding_models['sroberta'] = HuggingFaceEmbedding("bespin-global/klue-sroberta-base-continue-learning-by-mnr")
# config yaml파일에 sroberta 이름으로 이제 사용할 수 있음 

root_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(root_path, 'my_data')


@click.command()
@click.option('--config', type=click.Path(exists=True))
@click.option('--qa_data_path', type=click.Path(exists=True), default=os.path.join(data_path, 'qa_new.parquet'))
@click.option('--corpus_data_path', type=click.Path(exists=True), default=os.path.join(data_path, 'corpus_new.parquet'))
@click.option('--project_dir', type=click.Path(exists=False), default=os.path.join(root_path, 'benchmark'))
def main(config, qa_data_path, corpus_data_path, project_dir):
    # load_dotenv()
    # if os.getenv('OPENAI_API_KEY') is None:
    #     raise ValueError('OPENAI_API_KEY environment variable is not set')
    # if not os.path.exists(project_dir):
    #     os.makedirs(project_dir)
        
    evaluator = Evaluator(qa_data_path, corpus_data_path, project_dir=project_dir)
    evaluator.start_trial(config)


if __name__ == '__main__':
    main()

# 저는 가장 위에거 했어요. 
# python main.py --config ./config/compact_local_simple_ollama_ko.yaml

# openai 모델 사용은 아래 명령어로 해도 오류 없이 작동하게 만들었어요.
# python main.py --config ./config/tutorial_ko.yaml

# python main.py --config ./config/config_korean_openai_huggigface.yaml
# python main.py --config ./config/compact_local_huggingface.yaml
# python main.py --config ./config/compact_local_simple_ollama.yaml

# 평가지표 대시보드로 시각화된 자료 보기 
# autorag dashboard --trial_dir ./benchmark/0

# 윈도우에서는 아래 코드가 무조건 오류뜸, 맥이나 리눅스는 오류 안뜸 
# autorag run_web --trial_path ./benchmark/0