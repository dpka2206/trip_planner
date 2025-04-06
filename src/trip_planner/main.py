#!/usr/bin/env python
import sys
import warnings

from datetime import datetime


from trip_planner.crew import TripPlanner

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

# def run():
#     """
#     Run the crew.
#     """
#     inputs = {
#         'destination': 'Japan',
#         'current_year': str(datetime.now().year),
#         'no_of_days': '7',
#         'no_of_people': '4',
#         'budget': '$10000',
#         'interests': 'lakeside views, hiking, local cuisine, technology, temples',
#     }
#     inputs = {
#             'destination': destination,
#             'current_year': str(datetime.now().year),
#             'no_of_days': no_of_days,
#             'no_of_people': no_of_people,
#             'budget': budget,
#             'interests': interests,
#         }
#     try:
#         TripPlanner().crew().kickoff(inputs=inputs)
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")

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
