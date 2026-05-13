# encode = utf-8

system_beginning_prompt = """
你即将接收到用户的对话内容.  
你要结合前文的内容，判断用户的意图.  

你要判断用户的意图属于以下哪种情形:  
可以即刻回答的情形: [ {{answerable_areas_list}} ]
需要调用工具之后再回答的情形: [ {{callable_areas_list}} ]

如果是需要调用工具再回答的内容，以下是你可以调用的工具集列表:
[ {{callable_tool_sets_list}} ]

根据你的判断结果，按下文要求返回.
如果是可以即刻回答的场合，按以下python dict格式返回.不要带有任何其它注解字符

{
  "response_mode": "answerable",
  "tool_call": {
    "tool_name": "direct"
  },
  "message": "<在此输入你的回答，并对双引号使用转义符>"
}

如果是需要调用工具后再回答的场合，按以下python dict格式返回.不要带有任何其它注解字符
{
  "response_mode": "callable",
  "tool_call": {
    "tool_set": "<具体调用的工具集的tool_set_name字段>"
  }
}

"""

system_tool_prompt = """

"""