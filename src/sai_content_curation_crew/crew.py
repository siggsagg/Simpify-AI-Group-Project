from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq


@CrewBase
class SaiContentCurationCrew():
    """Describe the Crew here"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.groq_llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

    # Add agent functions below

    @agent
    def agent_name_from_yaml_file(self) -> Agent:
        return Agent(
            config = self.agents_config['agent_name_from_yaml_file'],
            llm=self.groq_llm
        )
    
    # Add more agents here

    # Add task functions below
    @task
    def task_name_from_yaml_file(self) -> Task:
        return Task(
            config = self.tasks_config['task_name_from_yaml_file'],
            agent = self.agent_name_from_yaml_file()
        )
    
    # Add more task functions here

    # Define the crew below
    @crew
    def crew(self) -> Crew:
        """Describe the crew here"""
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = 2
        )

## You must add the crews main.py run function to the pyproject.toml file under [tool.poetry.scripts] Like this:
##
## [tool.poetry.scripts]
## crew_root_folder_name = "crew_root_folder_name.main:run"