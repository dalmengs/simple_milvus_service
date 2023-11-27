<h1>Milvus(Vector DB) Practice</h1>

This is simple milvus practice project to simplify vector database operations.<br><br>
Although its name contains 'simple', it doesn't mean it is valueless.<br>
You can identify and understand of vector DB's operations.<br>
Also, this project has core functionalities: insert data, search similar data.<br><br>
So, I am looking forward to apply this structure and codes to our main project!<br><br>
In 'structure.png', you can overall structure of this project.<br>
Below is brief descriptions of structure.
- User can access vector DB service only.
- Vector DB service accesses vector DB connector which has responsibilities of processing main logics.
- Milvus server is running on docker, listening port 19530.

<hr>
<h1>Milvus(벡터 데이터베이스) 토이 프로젝트</h1>
이 프로젝트는 벡터 DB의 구조와 동작을 파악하기 위해 진행한 간단한 프로젝트입니다.<br><br>
이 프로젝트는 매우 간단하지만 매우 중요한 가치를 가지고 있습니다.<br>
벡터 DB의 구조를 계층적으로 파악할 수 있고, 핵심 동작을 쉽게 파악할 수 있습니다.<br>
1. 데이터 찾기<br>
2. 유사한 데이터 검색하기<br><br>
따라서 이 코드를 조금만 변형하면 바로 프로젝트에 사용할 수 있습니다.<br><br>
'structure.png' 파일에는 이 프로젝트의 전체적인 구조가 담겨 있습니다.<br>
1. 사용자는 서비스 계층에만 접근할 수 있습니다.<br>
2. 서비스 계층은 주요 로직을 처리하는 Connector에 접근합니다.<br>
3. Milvus 서버는 19530 포트의 도커에서 돌아가고 있습니다.
