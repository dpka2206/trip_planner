from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool



# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class TripPlanner():
    """TripPlanner crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def itinerary_planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['itinerary_planner_agent'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def accommodation_finder_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['accommodation_finder_agent'],
            verbose=True,
            tools=[SerperDevTool()]
        )
    
    @agent
    def budget_management_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['budget_management_agent'],
            verbose=True,
            tools=[SerperDevTool()]
        )
    
    @agent
    def activity_recommendation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['activity_recommendation_agent'],
            verbose=True,
            tools=[SerperDevTool()]
        )
    
    @agent
    def transportation_optimization_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['transportation_optimization_agent'],
            verbose=True,
            tools=[SerperDevTool()]
        )
    
    @agent
    def local_expert_ai_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['local_expert_ai_agent'],
            verbose=True,
            tools=[SerperDevTool()]
        )
    
    @agent
    def weather_and_conditions_monitoring_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_and_conditions_monitoring_agent'],
            verbose=True,
            tools=[SerperDevTool()]
        )


    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def itinerary_planner_task(self) -> Task:
        return Task(
            config=self.tasks_config['itinerary_planner_task'],
            output_file='itinerary_planner_task.md'
        )

    @task
    def accommodation_finder_task(self) -> Task:
        return Task(
            config=self.tasks_config['accommodation_finder_task'],
            output_file='accommodation_finder_task.md'
        )
    
    @task
    def budget_management_task(self) -> Task:
        return Task(
            config=self.tasks_config['budget_management_task'],
            output_file='budget_management_task.md'
        )
    
    @task
    def activity_recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config['activity_recommendation_task'],
            output_file='activity_recommendation_task.md'
        )
    
    @task
    def transportation_optimization_task(self) -> Task:
        return Task(
            config=self.tasks_config['transportation_optimization_task'],
            output_file='transportation_optimization_task.md'
        )
    
    @task
    def local_expert_ai_task(self) -> Task:
        return Task(
            config=self.tasks_config['local_expert_ai_task'],
            output_file='local_expert_ai_task.md'
        )
    
    @task
    def weather_conditions_monitoring_task(self) -> Task:
        return Task(
            config=self.tasks_config['weather_conditions_monitoring_task'],
            output_file='weather_conditions_monitoring_task.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TripPlanner crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )