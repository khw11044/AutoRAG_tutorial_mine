import os

import click
from autorag.evaluator import Evaluator
from dotenv import load_dotenv

import autorag
from llama_index.llms.ollama import Ollama
autorag.generator_models["ollama"] = Ollama

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# autorag.generator_models['kosimcse'] = HuggingFaceEmbedding("BM-K/KoSimCSE-roberta-multitask")


root_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(root_path, 'data')


@click.command()
@click.option('--config', type=click.Path(exists=True))
@click.option('--qa_data_path', type=click.Path(exists=True), default=os.path.join(data_path, 'qa.parquet'))
@click.option('--corpus_data_path', type=click.Path(exists=True), default=os.path.join(data_path, 'corpus.parquet'))
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

# python main.py --config ./config/config_korean_openai_huggigface.yaml
# python main.py --config ./config/compact_local_huggingface.yaml
# python main.py --config ./config/compact_local_simple_ollama.yaml

# autorag dashboard --trial_dir ./benchmark/0

# autorag run_web --trial_path ./benchmark/0