``version: "2.0"

nlu:

- intent: request_event
  examples: |
    - 帮我查[林业植物检疫证书核发](event)
    - 帮我查[医师资格证书核发补证](event)
    - 查询[医师资格证书核发补证](event)
    - 查询[放射诊疗许可](event)
    - 查一下[林业植物检疫证书核发](event)
    - 帮我查[林业植物检疫证书核发](event)
    - 帮我查[医师资格证书核发补证](event)
    - 查询[医师资格证书核发补证](event)
    - 查询[放射诊疗许可](event)
    - 查询[开面馆](event)
    - 查询[开皮具美容店](event)
    - 查一下[经营高危险性体育项目审批](event)
    - 查询[食品经营许可证补证](event)
    - 查询[最低生活保障金的给付](event)
    - 查询[开面馆](event)
    - 查询[开皮具美容店](event)

- intent: request_legal_person
  examples: |
    - [法人](person)办理
    - [法人](person)

- intent: request_client
  examples: |
    - [委托人](person)办理
    - [委托人](person)


- intent: request_original_file_lost
  examples: |
    - [正本](file)丢弃
    - [正本](file)遗失
    - [正本](file)丢落
    - [正本](file)丢掉
    - [正本](file)找不到
    - [正本](file)不见了
    - [正本](file)消失了
    - [正本](file)失踪了

- intent: request_copy_file_lost
  examples: |
    - [副本](file)丢弃
    - [副本](file)遗失
    - [副本](file)丢落
    - [副本](file)丢掉
    - [副本](file)失踪了
    - [副本](file)找不到
    - [副本](file)不见了
    - [副本](file)消失了

- intent: out_of_scope
  examples: |
    - 你为什么要知道这些
    - 你为什么要问这个
    - 你为什么要这样