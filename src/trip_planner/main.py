#!/usr/bin/env python
import sys
import warnings

from datetime import datetime


from trip_planner.crew import TripPlanner

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew with user-provided input.
    """
    print("Welcome to the Trip Planner!")
    
    try:
        destination = input("Enter your destination: ")
        no_of_days = input("How many days is your trip? ")
        no_of_people = input("How many people are going? ")
        budget = input("Enter your total budget (e.g., $10000): ")
        interests = input("What are your interests? (e.g., lakeside views, hiking, etc.): ")

        inputs = {
            'destination': destination,
            'current_year': str(datetime.now().year),
            'no_of_days': no_of_days,
            'no_of_people': no_of_people,
            'budget': budget,
            'interests': interests,
        }

        TripPlanner().crew().kickoff(inputs=inputs)
    
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
