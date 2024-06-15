import os
from dotenv import load_dotenv
load_dotenv()

from sai_content_curation_crew.crew import SaiContentCurationCrew ## From CrewBase class in crew.py

def run():
    inputs = {
        'company_name': 'Tesla' 
    }
    SaiContentCurationCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
