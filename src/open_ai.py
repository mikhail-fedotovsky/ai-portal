from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.memory import ChatMessageHistory


def create_chain(model: str, base_url: str, temp: float):
    llm = ChatOpenAI(
        model=model,
        base_url=base_url,
        api_key='ollama',
        temperature=temp
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content="You're a cool assistant. Answer in Russian."),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{input}")
        ]
    )

    chain = prompt | llm | StrOutputParser()
    chat_history_for_chain = ChatMessageHistory()

    return RunnableWithMessageHistory(
        chain,
        lambda session_id: chat_history_for_chain,
        input_messages_key="input",
        history_messages_key="chat_history",
    )
