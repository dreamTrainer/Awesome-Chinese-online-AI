

# LLM编排
|    | 项目     | 链接                                                       | 文档   | 引擎      | 内置模型中转功能                                                                                    |
|---:|:---------|:-----------------------------------------------------------|:-------|:----------|:----------------------------------------------------------------------------------------------------|
|  0 | dify     | https://github.com/langgenius/dify                         |        |           | 是                                                                                                  |
|  1 | fastgpt  | https://github.com/labring/FastGPT                         |        |           | 通过oneapi实现                                                                                      |
|  2 | flowise  | https://github.com/FlowiseAI/Flowise                       |        | langchain |                                                                                                     |
|  3 | langflow | https://github.com/langflow-ai/langflow                    |        | langchain |                                                                                                     |
|  4 | bisheng  | https://github.com/dataelement/bisheng/blob/main/README.md |        |           | 支持openai ， 各大ai平台api， 和本地模型https://dataelem.feishu.cn/wiki/MYIvwCtCtiIbvzkjkhacCrOQn9g |


# openai服务-模型中转
|    | 项目       | 链接                                                                                                           | 兼容 OpenAI 的 RESTful API   | 多模型支持   | openai api接入支持   | UI管理页面                                   | 简介                                                                |
|---:|:-----------|:---------------------------------------------------------------------------------------------------------------|:-----------------------------|:-------------|:---------------------|:---------------------------------------------|:--------------------------------------------------------------------|
|  0 | oneapi     | https://github.com/songquanpeng/one-api                                                                        | 是                           | 是           | 是                   | 有                                           | 支持各大ai平台的api接入和转发，服务格式为openai                     |
|  1 | ollama     | https://github.com/ollama/ollama                                                                               | 是                           | 是           | 否                   | 有，https://github.com/open-webui/open-webui | 支持本地模型启动，用的人比较多                                      |
|  2 | vllm       | https://github.com/vllm-project/vllm                                                                           | 是                           | 否           | 否                   |                                              | 支持本地模型启动                                                    |
|  3 | swift      | https://github.com/modelscope/swift/blob/main/docs/source/LLM/%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%8F%82%E6%95%B0.md | 是                           | 否           | 否                   | 有，一个简单的web页面                        | 支持本地模型启动                                                    |
|  4 | fastchat   | https://github.com/lm-sys/FastChat/blob/main/docs/openai_api.md                                                | 是                           | 是           | 否                   |                                              | 支持本地模型启动                                                    |
|  5 | xinference | https://github.com/xorbitsai/inference/blob/main/README_zh_CN.md                                               | 是                           | 是           | 否                   | 有                                           | 支持本地模型启动                                                    |
|  6 | 问问       | https://key.wenwen-ai.com/                                                                                     | 是                           | 是           | 否                   | 有                                           | 一个付费的服务网站，基本等于oneapi的商业版，但是只能使用gpt类的模型 |


# 数据分析
|    | 项目                     | 链接                                                       | 文档                                                        | 简介                                                            |
|---:|:-------------------------|:-----------------------------------------------------------|:------------------------------------------------------------|:----------------------------------------------------------------|
|  0 | metagpt/data interpreter | https://github.com/geekan/MetaGPT/tree/main/examples/di    |                                                             | 实现了类似openai code interpreter的功能，并且支持ai自动训练模型 |
|  1 | open code interpreter    | https://github.com/OpenCodeInterpreter/OpenCodeInterpreter |                                                             | 实现了类似openai code interpreter的功能                         |
|  2 | pandas-ai                | https://github.com/Sinaptik-AI/pandas-ai                   |                                                             | 实现了chatbi的功能， 可以快速接入pandas                         |
|  3 | dbgpt                    | https://github.com/eosphoros-ai/DB-GPT.git                 | https://www.yuque.com/eosphoros/dbgpt-docs/ew0kf1plm0bru2ga | 支持多种数据库                                                  |


# 知识库RAG
|    | 项目               | 链接                                                                            |
|---:|:-------------------|:--------------------------------------------------------------------------------|
|  0 | langchain-ChatChat | https://github.com/chatchat-space/Langchain-Chatchat                            |
|  1 | QAnything          | https://github.com/netease-youdao/QAnything?tab=readme-ov-file                  |
|  2 | RAGFLow            | https://github.com/infiniflow/ragflow                                           |
|  3 | maxkb              | https://github.com/1Panel-dev/MaxKB/wiki/1-%E5%AE%89%E8%A3%85%E9%83%A8%E7%BD%B2 |
