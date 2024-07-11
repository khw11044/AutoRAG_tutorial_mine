import os

import click
import pandas as pd
from dotenv import load_dotenv

from llama_index.llms.openai import OpenAI
from autorag.data.qacreation import generate_qa_llama_index, make_single_content_qa

root_path = os.path.dirname(os.path.realpath(__file__))
from prompt import prompt


@click.command()
@click.option('--corpus_path', type=click.Path(exists=True),
              default=os.path.join('my_data', 'corpus_new.parquet'))
@click.option('--save_path', type=click.Path(exists=False, dir_okay=False, file_okay=True),
              default=os.path.join('my_data', 'qa_new.parquet'))
@click.option('--qa_size', type=int, default=200)        # qa_size개의 실험 데이터셋 만들기
def main(corpus_path, save_path, qa_size):
    load_dotenv()

    corpus_df = pd.read_parquet(corpus_path, engine='pyarrow')
    llm = OpenAI(model='gpt-4o', temperature=0.4)
    
    qa_df = make_single_content_qa(corpus_df, content_size=qa_size, qa_creation_func=generate_qa_llama_index,
                                   llm=llm, prompt=prompt, question_num_per_content=1)  # 하나의 컨텐츠 당 생성할 질문과 응답 수 
    # 해당 자료와 관련이 없는 질문 및 응답 데이터는 제거 
    qa_df = qa_df.loc[~qa_df['query'].str.contains('해당 자료와 관련이 없습니다.')]
    qa_df.reset_index(drop=True, inplace=True)
    qa_df.to_parquet(save_path)


if __name__ == '__main__':
    main()
