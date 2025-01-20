### 5차시 실습

- 이번 실습에서는 간단한 벡터 데이터베이스 실습을 진행합니다.
- 벡터 데이터베이스의 기초 설명은 [VectorDB_RAG.pdf](./VectorDB_RAG.pdf)에 포함되어 있습니다.

<br/>

- 실습에서는 벡터 데이터베이스로 ChromaDB를 사용하며, 2025년 1월 20일 기준으로 Google Colab에서 실행 가능한 ipynb 파일을 제공합니다.
(사용 환경: Python 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0])

ChromaDB 공식 문서: https://docs.trychroma.com/getting-started
ChromaDB 실습 자료:
[chromadb_getting_started.ipynb](./chromadb_getting_started.ipynb), [chromadb_RAG.ipynb](./chromadb_RAG.ipynb)

- 또한, 기존 예시처럼 문서 내용을 직접 문자열로 삽입하는 대신, CSV 파일 내 블로그 글을 파싱하여 벡터 데이터베이스에 저장하는 방법은 별도의 폴더에 있으니, 관심있으신 분은 따라해보시기 바랍니다. ([실습 파일](./RAG_example/exercise.ipynb))
- 해당 예시는 RAG_example 폴더에서 제공되며, PostgreSQL의 pgvector 확장을 이용해 벡터를 저장하는 방식도 참고 자료로 포함되어 있습니다.